#! /usr/bin/python3

import urllib2, httplib, argparse

def checkAdmin(wordlist, sitelist):
    """
    wordlist: the file containing all words (admin dirs), 1 word a line.
    sitelist: the file containing all sites to scan, 1 site a line.
    """

    dirlist = open(wordlist).readlines()
    sites = open(sitelist).readlines()

    def _check(site):
        for n in dirlist:
            try:
                urllib2.urlopen("{}/{}".format(site.strip(), n.strip())).info()
            except urllib2.URLError:
                continue
            except urllib2.HTTPError:
                continue
            except httplib.HTTPException:
                continue
            except IOError:
                continue
            else:
                print("[i] Possible: {}/{}".format(site.strip(), n.strip()))
                open('./found.txt', 'a').write('{}/{}\n'.format(site.strip(), n.strip()))

    try:
        for site in sites:
            _check(site)
    except KeyboardInterrupt:
        exit("\nUser Exited\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawTextHelpFormatter,
        description = 'Simple Admin Control Panel finder by Black Python')

    parser.add_argument('-w', '--wordlist', default = None, help = 'The wordlist file which contains all the directory list to try against target site, 1 word a line')
    parser.add_argument('-s', '--sitelist', default = None, help = 'The file which contains all the target sites, 1 site a line.')

    args = parser.parse_args()

    if args.wordlist is None: exit("[!] You must specify a valid wordlist\n")
    elif args.sitelist is None: exit("[!] You must specify a valid sitelist\n")
    else: checkAdmin(args.wordlist, args.sitelist)
