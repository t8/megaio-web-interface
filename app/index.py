import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

relay1 = os.popen("megaio 0 rread 1").readline()
relay2 = os.popen("megaio 0 rread 2").readline()
relay3 = os.popen("megaio 0 rread 3").readline()
relay4 = os.popen("megaio 0 rread 4").readline()
relay5 = os.popen("megaio 0 rread 5").readline()
relay6 = os.popen("megaio 0 rread 6").readline()
relay7 = os.popen("megaio 0 rread 7").readline()
relay8 = os.popen("megaio 0 rread 8").readline()

@app.route('/')
def home():
    return render_template('dashboard.html', relay1=relay1, relay2=relay2, relay3=relay3, relay4=relay4, relay5=relay5, relay6=relay6, relay7=relay7, relay8=relay8)

@app.route('/relay/<int:rNum>')
def editRelay(rNum):
    status = os.popen("megaio 0 rread " + str(rNum)).readline()
    if status == 1:
        os.system("megaio 0 rwrite " + str(rNum) + " off")
    elif status == 0:
        os.system("megaio 0 rwrite " + str(rNum) + " on")
    return render_template('dashboard.html', relay1=relay1, relay2=relay2, relay3=relay3, relay4=relay4, relay5=relay5, relay6=relay6, relay7=relay7, relay8=relay8)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)