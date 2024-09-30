from flask import Flask, render_template, request, redirect, url_for
from ping import ping_local, ping_remote  # Import the ping functions

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
    result = None
    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]
        
        # If source is localhost, use local ping
        if source == "localhost":
            success, output = ping_local(destination)
        else:
            # For remote ping, add SSH username and password to the form
            username = request.form.get('username', 'root')  # Default to root
            password = request.form.get('password', 'password')  # Default password
            success, output = ping_remote(source, destination, username, password)
        
        # Format the output with green for success and red for failure
        if success:
            result = f'<span style="color:green;">Ping successful!</span><br><pre>{output}</pre>'
        else:
            result = f'<span style="color:red;">Ping failed.</span><br><pre>{output}</pre>'

    return render_template("tools.html", result=result)

# New routes for About and Contact pages
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
