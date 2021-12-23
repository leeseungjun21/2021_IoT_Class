from flask import Flask, render_template
import RPi.GPIO as GPIO
LED_PIN = 6
LED_PIN2 = 22


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("led.html")

@app.route("/led/<op>/<color>")
def led_op(op,color):
    if op == "on" and color == "blue" :
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op == "off" and color == "blue"  :
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"
    elif op == "on" and color == "green" :
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return "LED ON"
    elif op == "off" and color == "green"  :
        GPIO.output(LED_PIN2, GPIO.LOW)
        return "LED OFF"
    return 
        
    
        

if __name__ == "__main__":
    try:
      app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()