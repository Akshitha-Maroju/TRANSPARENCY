import os
from flask import Flask, render_template

app = Flask(__name__)

# Sample ICU patient data (demo data)
patient = {
    "name": "Patient A",
    "heart_rate": 82,
    "oxygen": 96,
    "ventilator": "Active",
    "doctor_update": "Patient condition stable"
}

# Medical timeline events
timeline = [
    "10:00 AM - Patient admitted to ICU",
    "10:30 AM - CT scan completed",
    "12:00 PM - Neurologist consultation",
    "02:00 PM - Brain activity test conducted",
    "03:30 PM - Doctor update: Stable condition"
]

@app.route("/")
def dashboard():
    return render_template("index.html", patient=patient)

@app.route("/timeline")
def show_timeline():
    return render_template("timeline.html", timeline=timeline)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render requires this
    app.run(host="0.0.0.0", port=port)