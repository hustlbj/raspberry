import os
import sys
import time
import psutil
from abc import ABCMeta, abstractmethod

class Metric:
	__metaclass__ = ABCMeta #指定这是一个抽象类
	def __init__(self):
		self.data = {}
	@abstractmethod #抽象方法
	def do_collect(self):
		pass
	def get_data(self):
		return self.data

class CPU(Metric):
	def do_collect(self):
		self.data['cpu_percent'] = psutil.cpu_percent()	

if __name__ == "__main__":
	cpu = CPU()
	cpu.do_collect()
	print(cpu.get_data())	
