#!/usr/bin/env python3
# create the list called vendors
def main():
    """
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# loop across the list vendors
    for x in vendors:
        print("The vendor is:" + x)  # each time through the loop print value of x
        print("\nOur loop has ended.")  # when the loop ends print this
    
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# loop across the list vendors
    for x in vendors:
        print("The vendor is:" + x)  # each time through the loop print value of x
        print("\nOur loop has ended.")  # when the loop ends print this
     """


    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
    approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
    for x in vendors:
        print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
        print("\nOur loop has ended.") # print when loop has finished
    if __name__ == "__main__":
        main()

        """
        print("The vendor is:" + x)  # each time through the loop print value of x
        print("\nOur loop has ended.")  # when the loop ends print this
        """

