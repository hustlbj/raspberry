import os
import sys
import time
import psutil
from abc import ABCMeta, abstractmethod

# Parent class
class Metric:
	__metaclass__ = ABCMeta #指定这是一个抽象类
	def __init__(self):
		self.data = {}
	@abstractmethod #抽象方法
	def do_collect(self):
		pass
	def get_data(self):
		return self.data
	@abstractmethod
	def do_alarm(self):
		pass

# Child class
class CPU(Metric):
	# rewrite, implementation 
	def do_collect(self):
		self.data['cpu_percent'] = psutil.cpu_percent()	
	def do_alarm(self):
		if self.data['cpu_percent'] > 0.9:
			return True
		return False

class MEM(Metric):
	def do_collect(self):
		self.data['mem_percent'] = psutil.virtual_memory()[2] / 100.0
	def do_alarm(self):
		if self.data['mem_percent'] > 0.9:
			return True
		return False

class NET(Metric):
	# class variables, using CLS.var (e.g. NET.last) to call them
	last = None
	is_first = True

	def do_collect(self):
		now = psutil.net_io_counters(pernic = True)
		if not NET.is_first:
			# limit 1M/s, then it equals 10M/10s, 
			self.data['eth0_bytes_sent'] = float(now['eth0'][0] - NET.last['eth0'][0]) / 1000 #KB
			self.data['eth0_bytes_recv'] = float(now['eth0'][1] - NET.last['eth0'][1]) / 1000 #KB
		else:
			self.data['eth0_bytes_sent'] = 0.0
			self.data['eth0_bytes_recv'] = 0.0
			NET.is_first = False
		NET.last = now	
	def do_alarm(self):
		# limit 5M/10s for sent, 10M/10s for recv
		if self.data['eth0_bytes_sent'] > 5000 or self.data['eth0_bytes_recv'] > 10000:
			return True
		return False
	

class TEMP(Metric):
	def do_collect(self):
		file = open('/sys/class/thermal/thermal_zone0/temp')
		temp = float(file.read()) / 1000
		file.close()
		self.data['cpu_temperature'] = temp
	def do_alarm(self):
		if self.data['cpu_temperature'] > 70:
			return True
		return False

if __name__ == "__main__":
	cpu = CPU()
	mem = MEM()
	net = NET()
	temp = TEMP()
	interval = 10
	while (1):
		for metric in [cpu, mem, net, temp]:
			metric.do_collect()
			print(metric.data)
			print(metric.do_alarm())

		time.sleep(interval)
