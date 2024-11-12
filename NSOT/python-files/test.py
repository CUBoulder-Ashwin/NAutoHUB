import re
import subprocess
import time
import requests
import json

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
        time.sleep(10)  # Wait longer to give Jenkins time to start the build
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
        return False

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

# Function to get the latest build number using Jenkins API
def get_latest_build_number(jenkins_base_url, user, token):
    try:
        url = f"{jenkins_base_url}/job/robocontrol/api/json?tree=lastBuild%5Bnumber%5D"
        print("Fetching latest build number from URL:", url)
        response = requests.get(url, auth=(user, token))
        response_data = response.json()
        latest_build_number = response_data.get("lastBuild", {}).get("number")
        if latest_build_number:
            print("Latest Build Number:", latest_build_number)
            return latest_build_number
        else:
            print("Failed to retrieve the latest build number from response.")
            return None
    except Exception as e:
        print(f"Error fetching latest build number: {e}")
        return None

# Function to check build result for the latest build
def check_build_result(jenkins_base_url, latest_build_number, user, token):
    build_url = f"{jenkins_base_url}/job/robocontrol/{latest_build_number}/api/json"
    print("Checking build result from URL:", build_url)
    response = requests.get(build_url, auth=(user, token))
    if response.status_code == 200:
        build_info = response.json()
        result = build_info.get("result")
        print(f"Build result for build {latest_build_number}: {result}")
        return result
    else:
        print(f"Failed to retrieve build status for build {latest_build_number}.")
        return None

# Function to monitor the build status until completion
def monitor_jenkins_job():
    log_file_path = "/home/student/Desktop/Advanced-Netman/ngrok.log"
    jenkins_base_url = get_latest_ngrok_url(log_file_path)
    if not jenkins_base_url:
        print("Unable to retrieve ngrok URL for Jenkins.")
        return "Failed"

    jenkins_user = "admin"
    jenkins_token = "admin"

    # Fetch the latest build number
    latest_build_number = get_latest_build_number(
        jenkins_base_url, jenkins_user, jenkins_token
    )
    if not latest_build_number:
        return "Failed to retrieve the latest build number"

    # Monitor build status until it completes
    while True:
        build_result = check_build_result(
            jenkins_base_url, latest_build_number, jenkins_user, jenkins_token
        )
        if build_result == "SUCCESS":
            print("Jenkins job completed successfully.")
            return "SUCCESS"
        elif build_result == "FAILURE":
            print("Jenkins job failed.")
            return "FAILURE"
        elif build_result is None:
            print("Failed to get build status. Exiting.")
            return "Failed"
        else:
            print("Jenkins job is still in progress. Checking again in 10 seconds...")
            time.sleep(10)

# Combined function to push to Git and monitor Jenkins job
def push_and_monitor_jenkins():
    if git_push():
        return monitor_jenkins_job()
    return "Git push failed"

# Run this function standalone for testing
if __name__ == "__main__":
    result = push_and_monitor_jenkins()
    print("Final result:", result)
