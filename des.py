import random as rnd
from utils import generate_subkey, net_process


class DES:
    def __init__(self, key):
        self.subkey = generate_subkey(key)

    def enc(self, message):
        return net_process(message, self.subkey)
    
    def dec(self, message):
        return net_process(message, self.subkey[::-1])




if __name__ == '__main__':
    rnd.seed(42)

    test_num = 10
    correct_num = 0
    for _ in range(test_num):
        key = bin(rnd.getrandbits(64))[2:].zfill(64)
        print('key:', key)
        
        des = DES(list(key))
        message = bin(rnd.getrandbits(64))[2:].zfill(64)
        print('plain text:', message)

        cipher = des.enc(list(message))
        print('cipher text:', ''.join(cipher))

        dec_message = ''.join(des.dec(cipher))
        print('dec text:', dec_message)
        print('dec text == plain text?', message == dec_message)
        correct_num += (message == dec_message)
    
    print("%d tests complete,  %d corrects"% (test_num, correct_num))