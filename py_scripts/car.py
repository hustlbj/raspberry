import RPi.GPIO as GPIO
import time

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(29, GPIO.OUT)
	GPIO.setup(31, GPIO.OUT)
	GPIO.setup(33, GPIO.OUT)
	GPIO.setup(35, GPIO.OUT)
	GPIO.setup(37, GPIO.OUT)

def reset_back():
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	GPIO.output(29, GPIO.LOW)
def reset_forward():
	GPIO.output(31, GPIO.LOW)
	GPIO.output(33, GPIO.LOW)
	GPIO.output(35, GPIO.LOW)
	GPIO.output(37, GPIO.LOW)

def set_back():
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
def set_forward():
	GPIO.output(31, GPIO.HIGH)
	GPIO.output(35, GPIO.HIGH)
def set_left():
	GPIO.output(35, GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(35, GPIO.LOW)
def set_right():
	GPIO.output(31, GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(31, GPIO.LOW)

def back():
	reset_forward()
	reset_back()
	set_back()
	time.sleep(1)
	reset_forward()
	reset_back()
def forward():
	reset_back()
	reset_forward()
	set_forward()
	time.sleep(1)
	reset_back()
	reset_forward()
def left():
	reset_back()
	reset_forward()
	set_left()
def right():
	reset_back()
	reset_forward()
	set_right()
	
	
if __name__ == "__main__":
	try:
		init()
		forward()
		back()
		left()
		time.sleep(1)
		right()
	except KeyboardInterrupt as e:
		print(e)
	except Exception as e:
		print(e)
	finally:
		GPIO.cleanup()
