from flask import Flask, request, render_template, url_for, redirect, session
app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")

def index():
    return render_template("set_wifi.html", errors = session["message"])

@app.route("/set-wifi", methods = ["POST", "GET"])

def handle_form_post():
    validate(request.form)
    write_wpa_supplicant(request.form['ssid'], request.form["password"], request.form['priority'])
    session["message"] = "Successful. Restart your Pi to hae "
    return redirect("/")

def validate(form):
    for field, value in form.iteritems():
        if not value:
            session["message"] = "Please fill out the form below"
            return redirect("/")

def write_wpa_supplicant(ssid, password, priority):
    # Write to wpa_supplicant
    wpa = open("/Users/llamicron/temp_wpa", "a")
    wpa.write("\nnetwork={\n\tssid=\"%s\"\n\tpsk=\"%s\"\n\tpriority=%s\n}" % (ssid, password, priority))
