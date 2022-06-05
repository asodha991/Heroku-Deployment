import pickle
from flask import Flask, request, app, jsonify,url_for, render_template
import numpy as np
import pandas as pd
# import sklearn as sns

app = Flask (__name__)

model_c = pickle.load(open('model.pkl', "rb"))

@app.route("/")

def home():
    return render_template('home.html')

@app.route('/predict', methods= ['POST'])

def predict():
    
    # data = request.json['data']
    data = [float(x) for x in  request.form.values()]
    print(data)
    new_data = [np.array(data)]
    print(new_data)
    output = model_c.predict(new_data)[0]
    print (output)
    return render_template('home.html', prediction_text = 'Flower is .{}'.format(output) )
    # return jsonify("output")


if __name__ == "__main__":
    app.run(debug=True)