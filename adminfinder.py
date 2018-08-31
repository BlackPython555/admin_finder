#! /usr/bin/env python

# importing needed modules
from urllib2 import urlopen, Request, HTTPError, URLError
from os import system, name
import socket

def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

def find_admin(wordlist, sitelist):
    try:
       words = open(wordlist, 'r').readlines()
       sites = open(sitelist, 'r').readlines()
    except IOError:
       exit("One of your file was not found!")

    if not words or not sites: exit('Wordlist or Sitelist is empty')
    print("Searching...")

    def _not_found_msg(site, word):
        print "Not found: {}/{}".format(site.strip(), word.strip())

    def _check(site):
        found = []
        for word in words:
            try:
                req = Request("{}/{}".format(site.strip(), word.strip()))
                resp = urlopen(req)
            except HTTPError as e:
                _not_found_msg(site, word)
                continue
            except URLError as e:
                _not_found_msg(site, word)
                continue
            except socket.error as e:
                _not_found_msg(site, word)
                continue
            else:
                print "\x1b[32;1mFound: {}/{}\x1b[0m".format(site.strip(), word.strip())
                open("./found.txt", "a").write("{}/{}\n".format(site.strip(), word.strip()))
                found.append("{}/{}".format(site.strip(), word.strip()))
        clear()
        banner()
        print "Found sites:"
        for n in found:
            print n

    try:
        for site in sites:
            _check(site)
    except KeyboardInterrupt:
        exit("User exit")

def banner():
    print "#####################################################"
    print "#                                                   #"
    print "#  Admin control panel finder v1.1 by Black Python  #"
    print "#                                                   #"
    print "#                  NoB Cyber Army                   #"
    print "#                                                   #"
    print "#####################################################"

banner()
try:
    find_admin(raw_input('Wordlist Path: '), raw_input('Sitelist Path: '))
except KeyboardInterrupt:
    exit("User exit")
