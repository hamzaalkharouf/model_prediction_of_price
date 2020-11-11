from flask import Flask,request,jsonify
import pickle
import argparse
import numpy as np
import json
import pandas as pd

from Write_Csv import Write_Csv
app = Flask(__name__)
#append data(from url) to list
def Data_append(x1,x2,x3,x4,x5,x6):
    list_data=[]
    list_data.append(x1)
    list_data.append(x2)
    list_data.append(x3)
    list_data.append(x4)
    list_data.append(x5)
    list_data.append(x6)
    return list_data

#take model
#Calculate price from scikit
def path():
    parser = argparse.ArgumentParser()
    parser.add_argument("-path","--path",type = str)
    args = parser.parse_args()
    # './model.pickle'
    return args.path


def scikit_learn():
    transaction_date=float(request.args.get('transaction_date'))
    house_age=float(request.args.get('house_age'))
    distance_to_the__nearest_MRT_station=float(request.args.get('distance_to_the__nearest_MRT_station'))
    number_of_convenience_stores=float(request.args.get('number_of_convenience_stores'))
    latitude=float(request.args.get('latitude'))
    longitude=float(request.args.get('longitude'))

    list_data=[]
    list_data=Data_append(transaction_date,house_age,distance_to_the__nearest_MRT_station,number_of_convenience_stores,latitude,longitude)
    return list_data
#route /
#take data from url then send them to scikit_learn of Calculate price from scikit
#return information
@app.route('/')
def hello():
    return "<p>hello</p><p>http://127.0.0.1:5060/model?transaction_date=2017.917&house_age=10&distance_to_the__nearest_MRT_station=306.59470&number_of_convenience_stores=15&latitude=24.98034&longitude=121.53951</p>"


@app.route('/model', methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":
        list_data=scikit_learn()
        x = np.array(list_data).reshape(1,6)
        price = loaded_model.predict(x)
        if x.shape[0] == 1:
            price = price[0]
            list_data.append(price)
            Write_Csv(list_data)
        #price=scikit_learn.path(list_data)
        #list_data.append(price)
        #Write_Csv.Write_Csv(list_data)
        return jsonify({
        "transaction date" : list_data[0],
         "house age": list_data[1],
        "distance to the nearest MRT station": list_data[2],
        "number of convenience stores":list_data[3],
        "latitude":list_data[4],
        "longitude": list_data[5],
        "price" :price
        })
    elif   request.method == "GET":
        list_data=scikit_learn()
        x = np.array(list_data).reshape(1,6)
        price = loaded_model.predict(x)
        if x.shape[0] == 1:
            price = price[0]
            list_data.append(price)
            Write_Csv(list_data)
        #price=scikit_learn.path(list_data)
        #list_data.append(price)
        #Write_Csv.Write_Csv(list_data)
        return jsonify({
        "transaction date" : list_data[0],
         "house age": list_data[1],
        "distance to the nearest MRT station": list_data[2],
        "number of convenience stores":list_data[3],
        "latitude":list_data[4],
        "longitude": list_data[5],
        "price" :price,
        "pickle.format_version":pickle.format_version
        })


#to run servier => py app.py -path ./model.pickle
if __name__ == '__main__':

    args_path=path()
    loaded_model = pickle.load(open(args_path, 'rb'))
    app.run(debug=True, use_reloader=False, host='0.0.0.0')
# http://127.0.0.1:5060/model?transaction_date=2017.917&house_age=10&distance_to_the__nearest_MRT_station=306.59470&number_of_convenience_stores=15&latitude=24.98034&longitude=121.53951
