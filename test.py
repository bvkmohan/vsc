import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("BVK Mohan"))
print("")
r = requests.get("http://www.bvkmohan.com")
print(r.status_code)

name = input(" What is your name ? ")
print("Hello, " + name)
