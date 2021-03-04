# Importing required libraries
import requests
import configparser

# parse Config File for parameters
parser = configparser.ConfigParser()
parser.read('config.cfg')


# This Function Sends SMS to user
# This Function takes 2 arguments
# 1. Mobile - Mobile Number of User
# 2. SMS - Message to be sent to user
def sendsms(mobile, sms):
    url = "http://www.sms.godrej.com/services/SMSService.php?wsdl"
    payload = "<soapenv:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
              "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" " \
              "xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\">\n   <soapenv:Header/>\n   " \
              "<soapenv:Body>\n  " \
              "    <soapenv:sendSMS soapenv:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n         " \
              "<userName xsi:type=\"xsd:string\">" + parser.get('auth', 'username') + "</userName>\n         <pswd " \
                                                                                      "xsi:type=\"xsd:string\">" + parser.get(
        'auth', 'password') + "</pswd>\n         <number xsi:type=\"xsd:string\">+91" + str(
        mobile) + "</number>\n         <msg xsi:type=\"xsd:string\">" + sms + "</msg>\n      </soapenv:sendSMS>\n   " \
                                                                              "</soapenv:Body>\n</soapenv:Envelope> "
    headers = {
        'SOAPAction': 'http://www.sms.godrej.com/services/SMSService.php',
        'Content-Type': 'text/xml'
    }
    response = requests.request("POST", url, headers=headers, data=payload)