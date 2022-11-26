#!/bin/python3
from flask import Flask, jsonify
import sys
import os
import time

app = Flask(__name__)

def exec(script: str) -> int:
    return os.system(script)

def getData(filename: str) -> float:
    file = open("Pipes/{}".format(filename))
    return float(file.readline().strip())

def getDeviceName() -> str:
    return os.popen("whoami").read()

@app.route("/")
def home():
    return "Local Console Partnered Device Name: {}\n".format(str(getDeviceName()))

@app.route("/usage")
def getDeviceUsage():
    try:
        old_time = time.time()
        CPU_ret_status = exec("./Scripts/CPU_usage.bash")
        RAM_ret_status = exec("./Scripts/RAM_usage.bash")
        
        if CPU_ret_status < 0 and RAM_ret_status < 0:
            print("Failed to execute script...")
            sys.exit()
        
        struct = {
                'CPU': getData("CPU"),
                'RAM': getData("RAM"),
                'time_taken': round(time.time() - old_time, 4), 
        }
        
        return jsonify(struct)

    except Exception as e:
        print("Exception ruled when obtaining CPU:", e)
    
    sys.exit()
    