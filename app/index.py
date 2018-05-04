import os
import subprocess
from flask import Flask, render_template, make_response
from functools import wraps, update_wrapper
from datetime import datetime

app = Flask(__name__)

relay1 = 0
relay2 = 0
relay3 = 0
relay4 = 0
relay5 = 0
relay6 = 0
relay7 = 0
relay8 = 0

def refreshRelayStatus():
    relay1 = os.popen("megaio 0 rread 1").readline()
    relay2 = os.popen("megaio 0 rread 2").readline()
    relay3 = os.popen("megaio 0 rread 3").readline()
    relay4 = os.popen("megaio 0 rread 4").readline()
    relay5 = os.popen("megaio 0 rread 5").readline()
    relay6 = os.popen("megaio 0 rread 6").readline()
    relay7 = os.popen("megaio 0 rread 7").readline()
    relay8 = os.popen("megaio 0 rread 8").readline()


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


@app.route('/')
@nocache
def home():
    refreshRelayStatus()
    return render_template('dashboard.html', relay1=relay1, relay2=relay2, relay3=relay3, relay4=relay4, relay5=relay5, relay6=relay6, relay7=relay7, relay8=relay8)


@app.route('/relay/<int:rNum>')
@nocache
def editRelay(rNum):
    status = int(os.popen("megaio 0 rread " + str(rNum)).readline())
    if status == 1:
        os.system("megaio 0 rwrite " + str(rNum) + " off")
    elif status == 0:
        os.system("megaio 0 rwrite " + str(rNum) + " on")
    refreshRelayStatus()
    return render_template('dashboard.html', relay1=relay1, relay2=relay2, relay3=relay3, relay4=relay4, relay5=relay5, relay6=relay6, relay7=relay7, relay8=relay8)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)