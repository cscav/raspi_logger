import serial
import time
import json
import paho.mqtt.publish as publish
from dotenv import load_dotenv
import os

# -----------------------
# MQTT setup
# -----------------------
load_dotenv('.env')
mqttTopic = "b219a/cscav_analysis/vmr"
mqttBrokerAddress = os.environ.get("ADDRESS")
credentials = {'username': os.environ.get("MQTT_USERNAME"), 'password': os.environ.get("PASSWORD")}
