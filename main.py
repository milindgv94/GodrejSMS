# Importing required Libraries
import logging
from logging.handlers import RotatingFileHandler
from flask import request, Flask, jsonify
from assembly import GodrejSMS

app = Flask(__name__)


@app.route('/')
def execute():
    mobile = request.args.get('mobile', type=int)
    sms = request.args.get('sms', type=str)
    if (type(mobile) == int) and (len(str(mobile)) == 10):
        GodrejSMS.sendsms(mobile, sms)
        logmessage = str(mobile) + ' | ' + sms
        app.logger.info(logmessage)
        return jsonify({'Action': 'Success', 'Message': 'SMS Sent Successfully'})
    else:
        return jsonify({'Action': 'Error', 'Message': 'Mobile Number provided is Invalid'})


if __name__ == '__main__':
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s')
    log = RotatingFileHandler('logs/stdout.log', maxBytes=100000000, backupCount=0)
    log.setFormatter(formatter)
    app.logger.addHandler(log)
    app.logger.setLevel(logging.INFO)
    app.logger.info('GodrejSMS App Started Successfully')
    app.run(debug=False, threaded=False, processes=4)
