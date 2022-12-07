from flask import Flask, render_template
import requests,json

app = Flask(__name__)
@app.route("/student.html")
def home():
    res = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    data = json.loads(res.text)
    context = {'students':data['data']}
    return render_template("student.html", **context)
app.run(debug=True)