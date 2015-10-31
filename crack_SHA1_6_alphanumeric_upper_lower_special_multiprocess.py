from functools import partial
from itertools import product 

import hashlib
import multiprocessing as mp
import os
import random
import sys


count = 0
#total_count = 0


#class Counter(object):
#    def __init__(self, init_val=0):
#        self.val = mp.Value('i', init_val)
#        self.lock = mp.Lock()
#    
#    def increment(self):
#        with self.lock:
#            self.val.value += 1
#    
#    def value(self):
#        with self.lock:
#            return self.val.value


#def init(args):
#    global total_count
#    total_count = args

def shift_array(arr, n):
    if n < len(arr):
        return arr[-n:] + arr[:-n]
    return arr

def crack(target_hash, salt, seed_str, num_proc):
    mp.set_start_method('spawn')
    
    #total_count = Counter(0)
    #pool = mp.Pool(initializer=init, initargs=(total_count,), processes=num_proc)
    
    #part_crack_helper = partial(crack_helper, target_hash=target_hash, salt=salt)
    
    try:
        #pool.map(part_crack_helper, product(seed_str, repeat=4))
        #pool.close()
        #pool.join()

        processes = []
        shift_interval = int(len(seed_str) / num_proc)
        pt_len = 6
        for i in range(0, num_proc):
            seed_str = ''.join(shift_array(list(seed_str), shift_interval))
            p = mp.Process(target=crack_helper_proc, args=(product(seed_str, repeat=pt_len), target_hash, salt))
            p.start()
            print("pid: %d started using seed str: %s" % (p.pid, seed_str))
            processes.append(p)

        for p in processes:
            p.join()

    except KeyboardInterrupt:
        #pool.terminate()
        #pool.join()

        for p in processes:
            p.terminate()
            p.join
  
def crack_helper_proc(prod, target_hash, salt):
    global count
    for prod_tuple in prod:
        word = ''.join(prod_tuple)
        word = salt + word
         
        sha = hashlib.sha1() 
        sha.update(word.encode())
        sha_out = sha.hexdigest()
        
        #total_count.increment()
        #if total_count.value() % 100000 == 0:
        #    print("pid %d: %d hashes compared. Current word: %s" %(os.getpid(), total_count.value(), word))
        count += 1
        if count % 10000000 == 0:
            print("pid %d: %d hashes compared. Current word: %s" %(os.getpid(), count, word))

        if (sha_out == target_hash):
            print("Match found: %s %s %s" % (word[len(salt):], target_hash, salt))
            return
    print("pid %d finished." % os.getpid())


def crack_helper_pool(prod_tuple, target_hash, salt):
    global total_count
    word = ''.join(prod_tuple)
    word = salt + word
     
    sha = hashlib.sha1() 
    sha.update(word.encode())
    sha_out = sha.hexdigest()
    
    total_count.increment()
    if total_count.value() % 100000 == 0:
        print("pid %d: %d hashes compared. Current word: %s" %(os.getpid(), total_count.value(), word))

    if (sha_out == target_hash):
        print("Match found: %s %s %s" % (word[len(salt):], target_hash, salt))
        return



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("You gotta supply the SHA1 hash and number of processes to run")
        sys.exit()

    target_hash = sys.argv[1]
    salt = target_hash[:len(target_hash) - 40]
    target_hash = target_hash[len(salt):].lower()
    print("salt: %s hash: %s" % (salt, target_hash))

    num_proc = int(sys.argv[2])
    print("num processes: %d" % num_proc)
    
    seed_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+'
    print("Using seed str: %s" % seed_str)
   
    crack(target_hash, salt, seed_str, num_proc)
    
    
