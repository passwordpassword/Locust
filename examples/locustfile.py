#!/usr/bin/python3

from locust import Locust, Taskset, task

class MyTaskset(Taskset):
	@task
	def my_task(self):
		print("Executing My Task")
	

class MyLocust(Locust):
	task_set = MyTaskset 
	min_wait = 5000
	max_wait = 15000

#if we want to run it more often,we can define the weight attribute.

class WebUserLocust(Locust):
	weight = 3

class MobileUserLocust(Locust):
	weight = 3

