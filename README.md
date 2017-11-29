Locust - Begineers Guide

Contents:

1. Introduction

a. What is Locust?

Locust is an easy-to-use, distributed, user load testing tool. It is intended for load-testing web sites (or other systems) and figuring out how many concurrent users a system can handle.

The idea is that during a test, a swarm of locusts will attack your website. The behavior of each locust (or test user if you will) is defined by you and the swarming process is monitored from a web UI in real-time. This will help you battle test and identify bottlenecks in your code before letting real users in.

b.Features

a. Write user test scenarios in plain-old Python
b. Distributed & Scalable - supports hundreds of thousands of users
c. Web-based UI
d. Can test any system
e. Hackable


2. Installation

Locust is available on PyPI and can be installed through pip.

pip install locustio

When Locust is installed, a locust command should be available in your shell.

To see available options, run:

locust --help

3. Writing the Locustfile

Locustfile is a normal python file. The only requirement is that it declares at least one class — let’s call it the locust class—that inherits from the class Locust.

a. Defining the Locust class & task_set attribute 

A Locust class represents one user (or a swarming locust if you will). Locust will spawn (hatch) one instance of the locust class for each user that is being simulated. There are a few attributes that a locust class should typically define.

e.x. class MyLocust(Locust):

The task_set atribute should point to Taskset class which defines the behaviour of the user.

e.x. task_set = MyTaskset

b. min_wait & max_wait attributes

In addition to the task_set attribute, one usually wants to declare the min_wait and max_wait attributes. These are the minimum and maximum time respectively, in milliseconds, that a simulated user will wait between executing each task. min_wait and max_wait default to 1000, and therefore a locust will always wait 1 second between each task if min_wait and max_wait are not declared.

e.x. class MyLocust(Locust):
     task_set = MyTaskSet
     min_wait = 5000
     max_wait = 15000

c.Taskset class & declaring tasks

If the Locust class represents a swarming locust, you could say that the TaskSet class represents the brain of the locust. Each Locust class must have a task_set attribute set, that points to a TaskSet.

A TaskSet is, like its name suggests, a collection of tasks.

e.x. class MyTaskset(Taskset):
        @task
        def my_task(self):
                print("Executing My Task")


d. tasks attribute 

Using the @task decorator to declare tasks is a convenience, and usually the best way to do it.

e.x. task(3)

task would be executed 3 times.

4. Documentation

More info and documentation can be found at: http://docs.locust.io/


