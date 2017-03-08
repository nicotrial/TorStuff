import sys
import argparse
import base64
import codecs
import random
from random import randint

import stem
from stem.control import Controller
import time
from random import randint
from multiprocessing.pool import ThreadPool as Pool
from gevent import Timeout
from gevent import monkey
monkey.patch_all()

# from multiprocessing import Pool

def handler(signum, frame):
    print "Forever is over!"
    raise Exception("end of time")

pool_size = 20  # your "parallelness"
pool = Pool(pool_size)
seconds =5 # max time the worker may run
a = []

def generateRSAKey():
    key = base64.b32encode(codecs.decode(codecs.encode('{0:020x}'.format(random.getrandbits(80))),'hex_codec')).lower()
    print (key)
    return key


def worker(item):
    try:

        #timeout = Timeout(seconds)
        #timeout.start()
        hs_descriptor = controller.get_hidden_service_descriptor(item.rstrip())
        #hs_descriptor = controller.get_hidden_service_descriptor(args.onion_address)
        #print dir(controller)
        print item
        a.append(item)
        for introduction_point in hs_descriptor.introduction_points():
            print('  %s:%s => %s' % (introduction_point.address, introduction_point.port, introduction_point.identifier))
            #print dir(introduction_point)
    except stem.DescriptorUnavailable:
        print("Descriptor for %s not found, the hidden service may be offline." %item.rstrip())
        pass
    except Timeout:
        print('Could not complete for %s' %item.rstrip())
        pass
    except Exception as e:
        for exection in e:
            print e
    #    print('Could not complete error grave for %s' %item.rstrip())
    #    pass
    

with Controller.from_port(port=9151) as controller:
    controller.authenticate()
    f = open('torlist.txt')
    for line in f:
            try:
                pool.apply_async(worker, (line,))
            except Exception:
                print('Could not complete error grave')
                pass
    f.close()
    #for item in range(100):
    #    pool.apply_async(worker, (item,))

    pool.close()
    pool.join(10)
    if pool.is_alive():
        print "running... let's kill it..."

        # Terminate
        pool.terminate()
        pool.join()
print a