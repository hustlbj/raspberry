#!/usr/bin/python
#coding=utf-8
#注意本程序是python3！！！
import RPi.GPIO as GPIO
import time

#LED发光二极管相关的操作
'''
BOARD方式第12引脚（GPIO.1， BCM方式编号18，wPi方式编号1）接到LED正极作为高电平输入到LED
BOARD方式第14引脚（0V）接到LED负极
12+-------200~400R--------+LED-|
14-----------------------------|
'''

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
#点亮1秒钟
def light():
	GPIO.output(12, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(12, GPIO.LOW)

def breath():
	#第一个参数是引脚编号，第二个参数是频率
	pwm = GPIO.PWM(12, 80)	
	#参数表示占空比，范围0.0~100.0
	pwm.start(0)
	#python3中range和原来的xrange实现一样了，去掉了xrange
	for i in range(0, 101, 1):
		pwm.ChangeDutyCycle(i)
		time.sleep(0.02)
	for i in range(100, -1, -1):
		pwm.ChangeDutyCycle(i)
		time.sleep(0.02)

if __name__ == "__main__":
	init()
	try:
		while True:
			light()
			breath()
			time.sleep(1)
	#python2不使用as
	except KeyboardInterrupt as e:
	#python2不必使用括号
		print("Exit...")
	except Exception as e:
		print(e)
	finally:
		GPIO.cleanup()

