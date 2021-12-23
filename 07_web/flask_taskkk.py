from flask import Flask
import RPi.GPIO as GPIO
LED_PIN = 22
LED_PIN2 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask !!</p>
        <a href="/led/on/green">GREENLED ON</a>
        <a href="/led/off/green">GREENLED OFF</a>
        <a href="/led/on/blue">BLUELED ON</a>
        <a href="/led/off/blue">BLUELED OFF</a>

    '''

@app.route("/led/<op>/<color>")
def led_op(color,op):
    if op == "on" and color == "green":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
        <p>LED ON</p>
        <a href="/">Go home</a>
      '''
    elif op == "off" and color == "green" :
        GPIO.output(LED_PIN, GPIO.LOW)
        return'''
        <p>LED OFF</p>
        <a href="/">Go home</a>
        '''
    elif op == "on" and color == "blue":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return '''
        <p>LED ON</p>
        <a href="/">Go home</a>
      '''
    elif op == "off" and color == "blue":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return'''
        <p>LED OFF</p>
        <a href="/">Go home</a>
        '''

if __name__ == "__main__":
    try:
      app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()