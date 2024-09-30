from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/tools")
def tools():
    return render_template("tools.html")

# New routes for About and Contact pages
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
