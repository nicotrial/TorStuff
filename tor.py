import sys
import argparse
import base64
import codecs
import random

import stem
from stem.control import Controller


def generateRSAKey():
    key = base64.b32encode(codecs.decode(codecs.encode('{0:020x}'.format(random.getrandbits(80))),'hex_codec')).lower()
    print (key)
    return key

def main():

    parser = argparse.ArgumentParser(description="%s fetches a Tor hidden "
                                     "service descriptor." % sys.argv[0])

    parser.add_argument("-p", "--port", type=int, default=9151,
                        help="Tor controller port")

    parser.add_argument('onion_address', type=str, help='Onion address')

    args = parser.parse_args()
    with Controller.from_port(port=args.port) as controller:
        controller.authenticate()
        while 1:
            key = base64.b32encode(codecs.decode(codecs.encode('{0:020x}'.format(random.getrandbits(80))),'hex_codec')).lower()
            print key
            try:
                hs_descriptor = controller.get_hidden_service_descriptor(key)
                #hs_descriptor = controller.get_hidden_service_descriptor(args.onion_address)
                #print dir(controller)		
                for introduction_point in hs_descriptor.introduction_points():
                    print('  %s:%s => %s' % (introduction_point.address, introduction_point.port, introduction_point.identifier))
                    #print dir(introduction_point)
            except stem.DescriptorUnavailable:
                print("Descriptor not found, the hidden service may be offline.")
                pass


if __name__ == '__main__':
    sys.exit(main())