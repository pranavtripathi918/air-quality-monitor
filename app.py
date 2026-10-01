from flask import Flask, render_template, request
from aqi_api import get_aqi
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    city = request.form.get("city")
    data = get_aqi(city)

    remark = None

    if data:
        aqi = data["aqi"]
        if aqi >= 0 and aqi <= 50:
            remark = "Air is clean, safe to go outside"
        elif aqi >= 51 and aqi <= 100:
            remark = "Acceptable, sensitive people should take care"
        elif aqi >= 101 and aqi <= 200:
            remark = "Moderate, limit outdoor activity"
        else:
            remark = "Poor air, stay inside"

    return render_template("result.html", data=data, city=city, remark=remark)


if __name__ == "__main__":
    app.run(debug=True)