#!/usr/bin/env python3

def main():

    """iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"]

    for ip in iplist:
       
      print(ip)
   """
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")
# close your file

dnsfile.close()

if __name__== "__main__":
    main()
    #    for ip in iplist:
     #       print(ip)
