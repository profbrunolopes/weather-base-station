#! /usr/bin/env python3

import time
import sqlite3
import RPi.GPIO as GPIO
import threading

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from struct import *
from RF24 import *
from RF24Network import *


def create_database():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS weather(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TIMESTAMP,
            station INTEGER,
            temp REAL,
            humi REAL,
            alti REAL,
            pres REAL
        )""")
    conn.close()

def insert_wheater_data(conn, params):
    cursor = conn.cursor()
    sqlite_insert_with_param = """INSERT INTO weather 
        (date, station, temp, humi, alti, pres) VALUES (?, ?, ?, ?, ?, ?)"""
    cursor.execute(sqlite_insert_with_param, params)
    conn.commit()

def start_radio_capture():
    radio = RF24(22,0)
    network = RF24Network(radio)

    conn = sqlite3.connect("weather.db")

    octlit = lambda n:int(n, 8)

    # Address of our node in Octal format (01, 021, etc)
    this_node = octlit("00")

    # Address of the other node
    other_node = octlit("01")

    radio.begin()
    radio.setDataRate(RF24_250KBPS)

    time.sleep(0.1)

    network.begin(120, this_node)    # channel 120
    radio.printDetails()

    while 1:
        network.update()
        while network.available():
            header, payload = network.read(16)
            temp, humi, pres, alti = unpack('<ffff', bytes(payload))

            data_tuple = (datetime.now(), header.from_node, temp, humi, alti, pres)
            insert_wheater_data(conn, data_tuple)
            print(f'[{data_tuple[0]}] (Station: {data_tuple[1]}, Temp: {temp:.2f}, Humi: {humi:.2f}, Pres: {pres:.2f}, Alti: {alti:.2f})')
            time.sleep(5)



if __name__ == "__main__": 
    create_database()

    radioThread = threading.Thread(target=start_radio_capture)
    radioThread.start()
    time.sleep(1)

    app = Flask(__name__)
    CORS(app)
    #app.config["DEBUG"] = True

    @app.route("/weather", methods=["GET"])
    def get_wheater_data():
        if 'station' in request.args:
            station = int(request.args["station"])
        else:
            return jsonify({"error": "The station variable must be passed on the request"})

        if 'limit' in request.args:
            limit = int(request.args["limit"])
        else:
            limit = 1

        weather_select_query = """SELECT * FROM weather WHERE station = ? ORDER BY date DESC LIMIT ?"""
        conn = sqlite3.connect("weather.db")

        results = []

        cursor = conn.cursor()
        cursor.execute(weather_select_query, (station, limit,))
        records = cursor.fetchall()

        for row in records:
            result = {
                    "id":row[0],
                    "date": row[1],
                    "station": row[2],
                    "temp": row[3], 
                    "humi": row[4],
                    "alti": row[5],
                    "pres": row[6]}
            results.append(result)

        cursor.close()

        return jsonify(results)


    app.run(host="0.0.0.0", port=5000)
