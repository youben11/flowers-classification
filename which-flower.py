#! /usr/bin/python3

import requests as req
from sys import argv, exit

API_URL = "http://130.211.108.207:5000/pred"
#API_URL = "http://localhost/pred"

def fatal(msg):
    print(msg)
    exit()

if __name__ == "__main__":
    if len(argv) != 2:
        fatal("[*] Usage: %s <flower-image>" % argv[0])

    try:
        flower_img = open(argv[1], "rb")
    except:
        fatal("[-] Can't open file '%s'" % argv[1])

    try:
        resp = req.post(API_URL, files={'flower_img': flower_img})
    except:
        fatal("[-] Can't connect to the API")

    probs = resp.json()
    if type(probs) != type(dict()):
        fatal("[-] Bad response from the server")

    list_probs = [(k, v) for k,v in zip(probs.keys(), probs.values())]
    sorted_probs = sorted(list_probs, key=lambda x:x[1], reverse=True)
    print("[+] This flower is a %s" % sorted_probs[0][0])
