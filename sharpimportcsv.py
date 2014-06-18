"""imports csv address list into a Sharp 6240 MFP (and maybe other Sharps in the same generation)"""

__author__ = 'sjames'
__copyright__ = 'Copyright (C) 2014 Steven James'
__license__ = "Public Domain"
__version__ = "0.1"
__email__ = "sjames@ctiengr.com"
__status__ = "Beta"


from csv import DictReader
from urllib import urlencode
import urllib2, argparse
from address_entry import AddressEntry


def do_post(endpoint, entry):
    post_data = urlencode(entry.address_entry_data)
    req = urllib2.Request(endpoint, data=post_data)
    result = urllib2.urlopen(req)
    return result


def add_address(name,email,hostname, pretend):
    entry = AddressEntry(name,email)
    endpoint = "http://%s/addressbook_entry.html" % hostname
    if not pretend:
        result = do_post(endpoint, entry)
        data = result.read() #read full response from copier, mostly for delay between requests
    else: result = 'pretended'
    return result

def main():
    """accepts command line input of a csv filepath and a copier hostname/ip
    and adds the addresses to the copier's address book"""
    parser = argparse.ArgumentParser(description='Import csv address book to Sharp 6240 (-h for more details)')
    parser.add_argument('-i', '--inputcsv', help='path to csv input file; columns "mail" and "name" will be imported',
                        required=True)
    parser.add_argument('-n', '--hostname', help='hostname/ip or hostname:port (will communicate via HTTP)',
                        metavar='HOSTNAME(:PORT)')
    parser.add_argument('-s', '--simulate', dest='simulate', action='store_true', help='if this argument is present, do not send changes, just pretend')
    args = parser.parse_args()
    inputcsv, hostname, pretend = args.inputcsv, args.hostname, args.simulate

    print 'reading ' + inputcsv
    if pretend:
        print 'SIMULATING!'
    with open(inputcsv, 'r') as f:
        rdr = DictReader(f, )
        for line in rdr:
            result = add_address(line['name'], line['mail'], hostname, pretend)
            print 'added',line['name']

if __name__ == '__main__':
    main()