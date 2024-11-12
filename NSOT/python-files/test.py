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

        # Traverse lines from the end to find the last occurrence of a URL
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


# Function to push to Git
def git_push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-config push"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to Git successfully.")
        time.sleep(5)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
        return False


def get_jenkins_crumb(jenkins_base_url, user, token):
    crumb_url = f"{jenkins_base_url}/crumbIssuer/api/json"
    response = requests.get(crumb_url, auth=(user, token))
    if response.status_code == 200:
        crumb_data = response.json()
        return {crumb_data["crumbRequestField"]: crumb_data["crumb"]}
    else:
        print("Failed to fetch Jenkins crumb.")
        return None


def trigger_jenkins_job():
    # Fetch the latest ngrok URL from the log file
    log_file_path = "/home/student/Desktop/Advanced-Netman/ngrok.log"
    jenkins_base_url = get_latest_ngrok_url(log_file_path)
    if not jenkins_base_url:
        print("Unable to retrieve ngrok URL for Jenkins.")
        return "Failed"

    job_name = "robocontrol"
    jenkins_user = "admin"
    jenkins_token = "admin"

    # Construct URLs
    job_url = f"{jenkins_base_url}/job/{job_name}"
    build_trigger_url = f"{job_url}/buildWithParameters"

    # Fetch CSRF crumb
    crumb_header = get_jenkins_crumb(jenkins_base_url, jenkins_user, jenkins_token)
    if not crumb_header:
        return "Failed to fetch Jenkins crumb"

    # Trigger Jenkins job with the crumb
    headers = crumb_header
    response = requests.post(
        build_trigger_url, auth=(jenkins_user, jenkins_token), headers=headers
    )
    if response.status_code == 201:
        print("Jenkins job started successfully.")
    else:
        print(f"Failed to start Jenkins job. Response: {response.text}")
        return "Failed"

    # Get the latest build number dynamically
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
            print("Latest Build URL:", latest_build_url)  # Debugging output
        else:
            print("Failed to retrieve job information.")
            return "Failed"
    except Exception as e:
        print(f"Error retrieving latest build number: {e}")
        return "Failed"


# Combined function to push and trigger Jenkins
def push_and_run_jenkins():
    if git_push():
        return trigger_jenkins_job()
    return "Git push failed"


# Run this function standalone for testing
if __name__ == "__main__":
    result = push_and_run_jenkins()
    print("Final result:", result)


# Combined function to push and trigger Jenkins
def push_and_run_jenkins():
    if git_push():
        return trigger_jenkins_job()
    return "Git push failed"


# Run this function standalone for testing
if __name__ == "__main__":
    result = push_and_run_jenkins()
    print("Final result:", result)
