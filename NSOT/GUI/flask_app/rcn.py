import os
import sys
from flask import Flask, render_template, request, redirect, url_for

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up two levels and into the 'python-files' directory
python_files_dir = os.path.join(current_dir, '..', '..', 'python-files')

# Add 'python-files' to the system path
sys.path.append(os.path.abspath(python_files_dir))

# Import your custom modules from 'python-files'
from ping import ping_local, ping_remote
from goldenConfig import generate_configs

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/dashboard")
def dashboard():
    # Embed your Grafana dashboard in the dashboard template
    return render_template("dashboard.html")

@app.route("/add-device", methods=['GET', 'POST'])
def add_device():
    if request.method == 'POST':
        device_name = request.form['device_name']
        ip_address = request.form['ip_address']
        # Add logic to handle the device configuration or database insert
        return redirect(url_for('homepage'))
    return render_template("add_device.html")

@app.route("/configure-device", methods=['GET', 'POST'])
def configure_device():
    if request.method == 'POST':
        device_id = request.form['device_id']
        configuration = request.form['configuration']
        # Add logic to configure the device
        return redirect(url_for('homepage'))
    return render_template("configure_device.html")

@app.route("/tools", methods=["GET", "POST"])
def tools():
    ping_result = None
    config_result = None

    # Handling Ping Test
    if request.method == "POST" and "source" in request.form and "destination" in request.form:
        source = request.form["source"]
        destination = request.form["destination"]
        
        if source == "localhost":
            success, output = ping_local(destination)
        else:
            username = request.form.get('username', 'root')
            password = request.form.get('password', 'password')
            success, output = ping_remote(source, destination, username, password)

        if success:
            ping_result = f'<span style="color:green;">Ping successful!</span><br><pre>{output}</pre>'
        else:
            ping_result = f'<span style="color:red;">Ping failed.</span><br><pre>{output}</pre>'

    # Handling Golden Config Generator
    if request.method == "POST" and ("device" in request.form or "select_all" in request.form):
        select_all = request.form.get('select_all', 'off')
        hostname = request.form.get("device")

        if select_all == 'on':
            filenames = generate_configs(select_all=True)
        elif hostname:
            filenames = generate_configs(select_all=False, hostname=hostname)

        if filenames:
            config_result = f"<h3>Generated Config Files:</h3><ul>"
            for file in filenames:
                config_result += f"<li>{file}</li>"
            config_result += "</ul>"

    return render_template("tools.html", ping_result=ping_result, config_result=config_result)

# New routes for About and Contact pages
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
