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

class GATE:
    def __init__(self, a0, a1, b0, b1, y0, y1, type=None):
        if type == None:
            raise Exception('Gate type error')
        match type:
            case 'XOR':
                self.gate_table = XOR(a0, a1, b0, b1, y0, y1)
            case 'AND':
                self.gate_table = AND(a0, a1, b0, b1, y0, y1)
            case 'OR':
                self.gate_table =  OR(a0, a1, b0, b1, y0, y1)
    
    def dec_gate(self, k0, k1):
        for text in self.gate_table:
            result = DEC(k0, k1, text)
            if result:
                return result
        
    