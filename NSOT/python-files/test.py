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
                ngrok_url = match.group(1)
                print("Ngrok URL found:", ngrok_url)  # Debugging print statement
                return ngrok_url  # Return the captured ngrok URL

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
        
        # Brief wait after pushing to allow Jenkins job to start
        time.sleep(5)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
        return False

# Function to trigger Jenkins job and fetch the output once done
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
    print("Triggering Jenkins job at:", build_trigger_url)
    response = requests.post(build_trigger_url, auth=(jenkins_user, jenkins_token))
    print("Trigger response code:", response.status_code)
    
    if response.status_code == 201:
        print("Jenkins job started successfully.")
    else:
        print("Failed to start Jenkins job.")
        return "Failed"

    # Get the latest build number dynamically
    latest_build_number = None
    try:
        job_info_url = f"{job_url}/api/json"
        print("Fetching job info from:", job_info_url)
        job_info_response = requests.get(job_info_url, auth=(jenkins_user, jenkins_token))
        
        if job_info_response.status_code == 200:
            job_info = job_info_response.json()
            latest_build_number = job_info.get("lastBuild", {}).get("number")
            latest_build_url = f"{job_url}/{latest_build_number}" if latest_build_number else "Not available"
            print("Latest Build URL:", latest_build_url)  # Debugging output
        else:
            print("Failed to retrieve job information. Status code:", job_info_response.status_code)
            return "Failed"
    except Exception as e:
        print(f"Error retrieving latest build number: {e}")
        return "Failed"

    # Poll Jenkins for the latest build completion and fetch output
    if latest_build_number:
        jenkins_build_url = f"{job_url}/{latest_build_number}/api/json"
        console_output_url = f"{job_url}/{latest_build_number}/consoleText"
        try:
            while True:
                print("Checking build status at:", jenkins_build_url)
                build_response = requests.get(jenkins_build_url, auth=(jenkins_user, jenkins_token))
                print("Build response code:", build_response.status_code)
                
                if build_response.status_code == 200:
                    build_info = build_response.json()
                    print("Build info received:", build_info)  # Debugging print
                    
                    if not build_info.get("building", True):  # Check if the job is no longer building
                        last_build_result = build_info.get("result", "UNKNOWN")
                        print("Jenkins job completed with status:", last_build_result)
                        
                        # Fetch and print the console output
                        output_response = requests.get(console_output_url, auth=(jenkins_user, jenkins_token))
                        print("Console output response code:", output_response.status_code)
                        
                        if output_response.status_code == 200:
                            print("Jenkins Console Output:\n", output_response.text)
                        else:
                            print("Failed to retrieve console output.")
                        return last_build_result
                    print("Waiting for Jenkins job to complete...")
                else:
                    print("Failed to fetch the last build information.")
                    return "Failed"
                time.sleep(10)  # Wait before polling again

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
