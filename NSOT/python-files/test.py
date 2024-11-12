import os
import re
import subprocess
import time
import requests

# Function to get the latest ngrok URL from the log file
def get_latest_ngrok_url(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()

        # Traverse lines from the end to find the last occurrence of a URL
        for line in reversed(lines):
            match = re.search(r"url=(https://[a-zA-Z0-9-]+\.ngrok-free\.app)", line)
            if match:
                print("Ngrok URL found:", match.group(1))  # Debugging print statement
                return match.group(1)  # Return the captured ngrok URL

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
        # Add all files, commit, and push
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-config push"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to Git successfully.")
        
        # Wait for 10 seconds after pushing
        time.sleep(10)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
        return False

# Function to trigger Jenkins job
def trigger_jenkins_job():
    # Fetch the latest ngrok URL from the log file
    log_file_path = "/home/student/Desktop/Advanced-Netman/ngrok.log"
    jenkins_base_url = get_latest_ngrok_url(log_file_path)
    if not jenkins_base_url:
        print("Unable to retrieve ngrok URL for Jenkins.")
        return "Failed"

    job_name = "robocontrol"  # Set to the specific job name you're working with
    jenkins_user = "admin"
    jenkins_token = "admin"

    # Construct URLs for job trigger and job info
    job_url = f"{jenkins_base_url}/job/{job_name}"
    build_trigger_url = f"{job_url}/buildWithParameters"

    # Trigger Jenkins job
    response = requests.post(build_trigger_url, auth=(jenkins_user, jenkins_token))
    if response.status_code == 201:
        print("Jenkins job started successfully.")
    else:
        print("Failed to start Jenkins job.")
        return "Failed"

    # Wait and get the latest build number dynamically
    time.sleep(5)  # Initial wait before polling
    latest_build_number = None
    try:
        job_info_response = requests.get(f"{job_url}/api/json", auth=(jenkins_user, jenkins_token))
        if job_info_response.status_code == 200:
            job_info = job_info_response.json()
            latest_build_number = job_info.get("lastBuild", {}).get("number")
            print("Latest Build Number:", latest_build_number)  # Debugging output
        else:
            print("Failed to retrieve job information.")
            return "Failed"
    except Exception as e:
        print(f"Error retrieving latest build number: {e}")
        return "Failed"

    # Poll Jenkins for the latest build completion
    if latest_build_number:
        jenkins_build_url = f"{job_url}/{latest_build_number}/api/json"
        try:
            while True:
                time.sleep(10)
                build_response = requests.get(jenkins_build_url, auth=(jenkins_user, jenkins_token))
                if build_response.status_code == 200:
                    build_info = build_response.json()
                    if not build_info.get("building", True):  # Check if the job is no longer building
                        last_build_result = build_info.get("result", "UNKNOWN")
                        last_build_url = build_info.get("url", "No URL found")
                        print("Last Build Result:", last_build_result)
                        print("Last Build URL:", last_build_url)
                        return last_build_result
                    print("Waiting for Jenkins job to complete...")
                else:
                    print("Failed to fetch the last build information.")
                    return "Failed"

        except Exception as e:
            print(f"An error occurred while fetching Jenkins job status: {e}")
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
