import random as rnd
from des import DES
from utils import xor

def G_key(key):
    message_1 = '1'.zfill(64)
    message_2 = '10'.zfill(64)

    des = DES(key)
    return des.enc(message_1) + des.enc(message_2)

def PRF(key, message):
    des = DES(key)
    return ''.join(G_key(des.enc(message)))

def ENC(k, r, x):
    return xor(PRF(k, r), x + ''.zfill(64))

def DEC(k, r, s):
    message = xor(PRF(k, r), s)
    tag = message[-64:]
    if sum(int(i) for i in tag) == 0:
        return message[:64]
    else:
        return None

def dec_gate(gate, k0, k1):
    k, r = k0, k1
    for t in gate:
        x = DEC(k, r, t)
        if x:
            return x

class GATE:
    def XOR(a0, a1, b0, b1, y0, y1):
        ans = [
            ENC(a0, b0, y0),
            ENC(a0, b1, y1),
            ENC(a1, b0, y1),
            ENC(a1, b1, y0)
        ]
        rnd.shuffle(ans)
        return ans
    
    def AND(a0, a1, b0, b1, y0, y1):
        ans = [
            ENC(a0, b0, y0),
            ENC(a0, b1, y0),
            ENC(a1, b0, y0),
            ENC(a1, b1, y1)
        ]
        rnd.shuffle(ans)
        return ans
    
    def OR(a0, a1, b0, b1, y0, y1):
        ans = [
            ENC(a0, b0, y0),
            ENC(a0, b1, y1),
            ENC(a1, b0, y1),
            ENC(a1, b1, y1)
        ]
        rnd.shuffle(ans)
        return ans