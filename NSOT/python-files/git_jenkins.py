import subprocess
import time
import requests


# Function to push to Git
def git_push():
    try:
        # Add all files, commit, and push
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-config push"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to Git successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")
        return False


# Function to trigger Jenkins job and fetch result
def trigger_jenkins_job():
    jenkins_url = "http://your_jenkins_server/job/your_job_name/buildWithParameters"
    jenkins_status_url = (
        "http://your_jenkins_server/job/your_job_name/lastBuild/api/json"
    )
    jenkins_user = "your_username"
    jenkins_token = "your_api_token"

    # Trigger Jenkins job
    response = requests.post(jenkins_url, auth=(jenkins_user, jenkins_token))
    if response.status_code == 201:
        print("Jenkins job started successfully.")
    else:
        print("Failed to start Jenkins job.")
        return "Failed"

    # Poll Jenkins for completion
    while True:
        time.sleep(10)
        job_response = requests.get(
            jenkins_status_url, auth=(jenkins_user, jenkins_token)
        ).json()
        if job_response["building"] is False:
            job_result = job_response.get("result", "UNKNOWN")
            print(f"Jenkins job completed with status: {job_result}")
            return job_result
        print("Waiting for Jenkins job to complete...")


# Combined function to push and trigger Jenkins
def push_and_run_jenkins():
    if git_push():
        return trigger_jenkins_job()
    return "Git push failed"
