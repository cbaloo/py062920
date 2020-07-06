#!/usr/bin/env python3

# list.append() and list.extend()

mylist = ["alena", "camel", "elephant"]

mylist.append("dog")

print(mylist)

mylist1 = ["hat", "mat", "bat"]
mylist.extend([mylist1])

print(mylist)

mylist.append(["pig", "cow", "cat"])
print(mylist)
mylist.extend("mouse")
print(mylist)
print(mylist1)
print(mylist1[0],mylist1[1], mylist1[2])
