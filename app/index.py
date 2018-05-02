import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    relay1 = subprocess.check_output(['gpio 0 rread 1'])
    relay2 = subprocess.check_output(['gpio 0 rread 2'])
    relay3 = subprocess.check_output(['gpio 0 rread 3'])
    relay4 = subprocess.check_output(['gpio 0 rread 4'])
    relay5 = subprocess.check_output(['gpio 0 rread 5'])
    relay6 = subprocess.check_output(['gpio 0 rread 6'])
    relay7 = subprocess.check_output(['gpio 0 rread 7'])
    relay8 = subprocess.check_output(['gpio 0 rread 8'])



    return render_template('dashboard.html', relay1, relay2, relay3, relay4, relay5, relay6, relay7, relay8)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)