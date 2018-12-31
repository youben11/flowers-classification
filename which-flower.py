#! /usr/bin/python3

import requests as req
from sys import argv, exit

API_URL = "http://localhost:8888/pred"

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

    prob = resp.json()
    if type(prob) != type(dict()):
        fatal("[-] Bad response from the server")

    list_prob = [(k, v) for k,v in zip(prob.keys(), prob.values())]
    sorted_prob = sorted(list_prob, key=lambda x:x[1], reverse=True)
    print("[+] This flower is a %s" % sorted_prob[0][0])
