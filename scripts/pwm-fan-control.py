import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21,120)

print("\nPress Ctrl+C to quit \n")
dc = 0
pwm.start(dc)

try:
    while True:
        temp = subprocess.getoutput("vcgencmd measure_temp|sed 's/[^0-9.]//g'")
        if round(float(temp)) >= 40:
            dc = 100
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
        else:
            dc = 0
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Ctrl + C pressed -- Ending program")
