from flask import Flask, request
from flask import render_template
from datetime import time

import statsmodels.api as sm
from fbprophet import Prophet
from fbprophet.serialize import model_to_json, model_from_json

with open('model/serialized_model.json', 'r') as fin:
    m = model_from_json(fin.read())  # Load model

data = sm.datasets.co2.load_pandas()
df = data.data

df_prophet  = df.dropna().reset_index()
df_prophet.columns = ['ds', 'y']




app = Flask(__name__)


@app.route("/simple_chart",  methods=['POST', 'GET'])
def chart():
    legend = 'Monthly Data'
    labels = df_prophet.ds.tolist()
    values = df_prophet.y.tolist()
    if request.method == 'GET':
        return render_template('chart.html', values=values, labels=labels, legend=legend)
    if request.method == 'POST':
        n = request.form['n']
        n = int(n)

        future = m.make_future_dataframe(periods=n)
        forecast = m.predict(future)
        forecast = forecast.dropna()
        values = forecast['yhat'].tolist()
        labels = forecast['ds'].tolist()



        return render_template('chart.html', values=values, labels=labels, legend=legend)


@app.route("/line_chart")
def line_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
             '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
             '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
    return render_template('line_chart.html', values=temperatures, labels=times, legend=legend)


@app.route("/time_chart")
def time_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = [time(hour=11, minute=14, second=15),
             time(hour=11, minute=14, second=30),
             time(hour=11, minute=14, second=45),
             time(hour=11, minute=15, second=00),
             time(hour=11, minute=15, second=15),
             time(hour=11, minute=15, second=30),
             time(hour=11, minute=15, second=45),
             time(hour=11, minute=16, second=00),
             time(hour=11, minute=16, second=15),
             time(hour=11, minute=16, second=30),
             time(hour=11, minute=16, second=45),
             time(hour=11, minute=17, second=00),
             time(hour=11, minute=17, second=15),
             time(hour=11, minute=17, second=30),
             time(hour=11, minute=17, second=45),
             time(hour=11, minute=18, second=00),
             time(hour=11, minute=18, second=15),
             time(hour=11, minute=18, second=30)]
    return render_template('time_chart.html', values=temperatures, labels=times, legend=legend)


if __name__ == "__main__":
    app.run(debug=True)
