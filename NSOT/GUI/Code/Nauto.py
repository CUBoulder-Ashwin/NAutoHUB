from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from validateIP import doubleCheck
from connectivity import check_ping
from runnConf import runConf
from diffConf import difConf
from ospfPush import push
from ospfPush import thrdTask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sshUsers.db'
db = SQLAlchemy(app)

#db model
class sshUsers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device = db.Column(db.String(10), nullable = False)
    username = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)
    loopback = db.Column(db.String(50), nullable = True)
    processId = db.Column(db.String(50), nullable = True)
    areaId = db.Column(db.String(50), nullable = True)
    cost = db.Column(db.String(50), nullable = True)

    def __repr__(self):
        return '<Device %r>' % self.id

@app.route("/")
def homepage(): 
    return render_template("homepage.html")

@app.route("/validIp", methods=['POST', 'GET'])
def validate(): 
    if request.method == "POST":
        IP = request.form.get('IPv4', '').strip()

        if IP:
            valid = doubleCheck(IP)
            if valid:
                return render_template("validateIP.html", val = "valid")
            else:
                return render_template("validateIP.html", val = "invalid")
        else:
            print("No IP entered")


    return render_template("validateIP.html", val = None)

    

@app.route("/runn-conf", methods = ['POST', 'GET'])
def runnConf(): 

    devices = sshUsers.query.all()

    if request.method == "POST":
        dvc = request.form.get('device', '').strip()
        ip = request.form.get('IPv4', '').strip()
        dvc_exist = db.session.query(sshUsers).filter_by(device = dvc).first()

        if dvc_exist:
            usr = dvc_exist.username
            pwd = dvc_exist.password

            try:
                msg = runConf(ip, usr, pwd)
            except Exception as e:
                msg = e

            return render_template("runningConfig.html", m=msg)
        else:
            return render_template("runningConfig.html", m="NA")
    return render_template("runningConfig.html", m=" ")

    

@app.route("/diff", methods = ['POST', 'GET'])
def diffConf(): 

    devices = sshUsers.query.all()

    if request.method == "POST":
        dvc = request.form.get('device', '').strip()
        ip = request.form.get('IPv4', '').strip()
        dvc_exist = db.session.query(sshUsers).filter_by(device = dvc).first()

        if dvc_exist:
            usr = dvc_exist.username
            pwd = dvc_exist.password
            try:
                msg = difConf(ip, usr, pwd)
            except Exception as e:
                msg = e
            return render_template("diffComp.html", m=msg)
        else:
            return render_template("diffComp.html", m="NA")
    return render_template("diffComp.html", m=" ")






@app.route("/ssh", methods=['POST','GET'])
def sshDb():
    devices = sshUsers.query.all()
    print(request.method)

    if request.method == "POST":

        action = request.form.get('action')

        if action == 'clear_db':
            try:
                sshUsers.query.delete()
                db.session.commit()
                devices = []
                return render_template('sshDb.html', dev=devices)
            except Exception as e:
                print(e)
                return "Error clearing database"
               
        dvc = request.form.get('device', '').strip()
        usr = request.form.get('username', '').strip()
        pwd = request.form.get('password', '').strip()

        if dvc and usr and pwd:
            dvc_exist = db.session.query(sshUsers).filter(sshUsers.device == dvc).scalar() is not None

            if not dvc_exist:
                new_sshUser = sshUsers(device=dvc, username=usr, password=pwd)
                try:
                    db.session.add(new_sshUser)
                    db.session.commit()
                    devices = sshUsers.query.all()
                except:
                    return "Error adding user"
            else:
                print("User already exist")
        else:
            print("No input entered. Value cannot be empty to submit")
    
    return render_template('sshDb.html', dev = devices)



@app.route("/ospf-push", methods=['POST','GET'])
def ospfPush():
    devices = sshUsers.query.all()

    if request.method == "POST":

        dvc = request.form.get('device', '').strip()
        ip = request.form.get('IPv4', '').strip()
        dvc_exist = db.session.query(sshUsers).filter_by(device = dvc).first()

        if dvc_exist:
            usr = dvc_exist.username
            pwd = dvc_exist.password
            loop = dvc_exist.loopback
            PID = dvc_exist.processId
            AID = dvc_exist.areaId
            cost = dvc_exist.cost
            try:
                msg = push(ip, usr, pwd, PID, AID, loop, dvc, cost)
            except Exception as e:
                print("Exception")
            return render_template("ospfPush.html", m=msg)
        else:
            return render_template("ospfPush.html", m="NA")
    return render_template("ospfPush.html", m=" ")



@app.route("/ospf", methods=['POST','GET'])
def ospf():
    devices = sshUsers.query.all()
    if request.method == "POST":

        act = request.form.get('prepare')  
        if act == "prepare":
            return render_template("ospfPush.html", m=" ")
        

        action = request.form.get('action')
        #print(action)
        if action =="hide_db":
            devices = sshUsers.query.all()
            render_template("ospf.html", dev=devices)
        elif action == "show_db":
            devices = []
            render_template("ospf.html", dev=devices)

        act = request.form.get('submit') 
        #print(act)
        if act == "save":
            dvc = request.form.get('device', '').strip()
            process_ID = request.form.get('PID', '').strip()
            area_ID = request.form.get('AID', '').strip()
            loopback = request.form.get('LIP', '').strip()
            cost = request.form.get('cost', '').strip()

            if dvc and process_ID and area_ID and loopback:
                    
                    dvc_exist = db.session.query(sshUsers).filter_by(device = dvc).first()
                    if dvc_exist:
                        dvc_exist.loopback = loopback
                        dvc_exist.processId = process_ID
                        dvc_exist.areaId = area_ID
                        dvc_exist.cost = cost
                        try:
                            db.session.commit()
                        except:
                            return "Error adding OSPF config details"
                    else:
                        print("Device does not exist","error")



    return render_template("ospf.html", dev=devices)



if __name__ == "__main__":
    app.run(host="localhost", port="8000",debug=True)