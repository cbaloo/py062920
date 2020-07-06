#!/usr/bin/env python3

""" working on dictionary"""

mydict11 = {"apple": "red", "berry" : "blue", "banana" : "yellow"}
print(mydict11["berry"])

print(mydict11.get("something"))

print(mydict11.keys())
print(mydict11.values())
mydict11["grapes"] = "green"
print(mydict11)
