from flask import Flask, render_template
import RPi.GPIO as GPIO
LED_PIN = 6


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("led.html")

@app.route("/led/<op>")
def led_op(op):
    if op == "on" :
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op == "off"  :
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"
    else:
      return 
        
    
        

if __name__ == "__main__":
    try:
      app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()