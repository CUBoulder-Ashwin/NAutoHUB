import os
import re
import subprocess
import time
import requests


# Function to get the latest ngrok URL from the log file
def get_latest_ngrok_url(log_file_path):
    try:
        with open(log_file_path, "r") as file:
            lines = file.readlines()
        for line in reversed(lines):
            match = re.search(r"url=(https://[a-zA-Z0-9-]+\.ngrok-free\.app)", line)
            if match:
                ngrok_url = match.group(1)
                print("Ngrok URL found:", ngrok_url)
                return ngrok_url
        print("No ngrok URL found in the log.")
        return None
    except FileNotFoundError:
        print(f"Log file not found: {log_file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to check if there are any changes to commit
def has_changes_to_commit():
    result = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True
    )
    return bool(result.stdout.strip())


# Function to push to Git
def git_push():
    if not has_changes_to_commit():
        print("No changes to commit.")
        return False

    try:
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-config push"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to Git successfully.")
        time.sleep(5)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
        return False


# Function to get Jenkins crumb for CSRF protection
def get_jenkins_crumb(jenkins_base_url, user, token):
    crumb_url = f"{jenkins_base_url}/crumbIssuer/api/json"
    response = requests.get(crumb_url, auth=(user, token))
    if response.status_code == 200:
        crumb_data = response.json()
        print("Jenkins crumb retrieved successfully.")
        return {crumb_data["crumbRequestField"]: crumb_data["crumb"]}
    else:
        print("Failed to fetch Jenkins crumb.")
        return None


# Function to trigger Jenkins job and check status
def trigger_jenkins_job():
    log_file_path = "/home/student/Desktop/Advanced-Netman/ngrok.log"
    jenkins_base_url = get_latest_ngrok_url(log_file_path)
    if not jenkins_base_url:
        print("Unable to retrieve ngrok URL for Jenkins.")
        return "Failed"

    job_name = "robocontrol"
    jenkins_user = "admin"
    jenkins_token = "admin"

    job_url = f"{jenkins_base_url}/job/{job_name}"
    build_trigger_url = f"{job_url}/buildWithParameters"

    # Get CSRF crumb for Jenkins
    crumb_header = get_jenkins_crumb(jenkins_base_url, jenkins_user, jenkins_token)
    if not crumb_header:
        return "Failed to fetch Jenkins crumb"

    # Trigger Jenkins job with crumb
    headers = crumb_header
    response = requests.post(
        build_trigger_url, auth=(jenkins_user, jenkins_token), headers=headers
    )
    if response.status_code == 201:
        print("Jenkins job started successfully.")
    else:
        print(f"Failed to start Jenkins job. Response: {response.text}")
        return "Failed"

    # Poll Jenkins for job completion
    latest_build_number = None
    try:
        job_info_response = requests.get(
            f"{job_url}/api/json", auth=(jenkins_user, jenkins_token), headers=headers
        )
        if job_info_response.status_code == 200:
            job_info = job_info_response.json()
            latest_build_number = job_info.get("lastBuild", {}).get("number")
            latest_build_url = (
                f"{job_url}/{latest_build_number}"
                if latest_build_number
                else "Not available"
            )
            print("Latest Build URL:", latest_build_url)
        else:
            print("Failed to retrieve job information.")
            return "Failed"
    except Exception as e:
        print(f"Error retrieving latest build number: {e}")
        return "Failed"

    # Poll for job status
    if latest_build_number:
        jenkins_build_url = f"{job_url}/{latest_build_number}/api/json"
        console_output_url = f"{job_url}/{latest_build_number}/consoleText"
        try:
            while True:
                build_response = requests.get(
                    jenkins_build_url,
                    auth=(jenkins_user, jenkins_token),
                    headers=headers,
                )
                if build_response.status_code == 200:
                    build_info = build_response.json()
                    if not build_info.get("building", True):
                        last_build_result = build_info.get("result", "UNKNOWN")
                        print("Jenkins job completed with status:", last_build_result)

                        # Fetch and print the console output
                        output_response = requests.get(
                            console_output_url,
                            auth=(jenkins_user, jenkins_token),
                            headers=headers,
                        )
                        if output_response.status_code == 200:
                            print("Jenkins Console Output:\n", output_response.text)
                        else:
                            print("Failed to retrieve console output.")
                        return last_build_result
                    print("Waiting for Jenkins job to complete...")
                else:
                    print("Failed to fetch the last build information.")
                    return "Failed"
                time.sleep(10)
        except Exception as e:
            print(f"An error occurred while fetching Jenkins job status: {e}")
            return "Failed"


# Combined function to push and run Jenkins
def push_and_run_jenkins():
    if git_push():
        return trigger_jenkins_job()
    return "Git push failed"


# Run this function standalone for testing
if __name__ == "__main__":
    result = push_and_run_jenkins()
    print("Final result:", result)
