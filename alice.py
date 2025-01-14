from gate import GATE
from utils import gen


def build_circuit():
    gates = []

    ### Layer 1
    a00 = gen()
    a01 = gen()
    b00 = gen()
    b01 = gen()
    c00 = gen()
    c01 = gen()
    d00 = gen()
    d01 = gen()
    e00 = gen()
    e01 = gen()
    f00 = gen()
    f01 = gen()
    c10 = gen()
    c11 = gen()
    gates.append(GATE(a00, a01, c00, c01, d00, d01, 'XOR'))
    gates.append(GATE(b00, b01, c00, c01, e00, e01, 'XOR'))
    gates.append(GATE(d00, d01, e00, e01, f00, f01, 'AND'))
    gates.append(GATE(a00, a01, f00, f01, c10, c11, 'XOR'))

    ### Layer 2
    a10 = gen()
    a11 = gen()
    b10 = gen()
    b11 = gen()
    d10 = gen()
    d11 = gen()
    e10 = gen()
    e11 = gen()
    f10 = gen()
    f11 = gen()
    c20 = gen()
    c21 = gen()
    gates.append(GATE(a10, a11, c10, c11, d10, d11, 'XOR'))
    gates.append(GATE(b10, b11, c10, c11, e10, e11, 'XOR'))
    gates.append(GATE(d10, d11, e10, e11, f10, f11, 'AND'))
    gates.append(GATE(a10, a11, f10, f11, c20, c21, 'XOR'))

    ### Layer 3
    a20 = gen()
    a21 = gen()
    b20 = gen()
    b21 = gen()
    d20 = gen()
    d21 = gen()
    e20 = gen()
    e21 = gen()
    f20 = gen()
    f21 = gen()
    c30 = gen()
    c31 = gen()
    gates.append(GATE(a20, a21, c20, c21, d20, d21, 'XOR'))
    gates.append(GATE(b20, b21, c20, c21, e20, e21, 'XOR'))
    gates.append(GATE(d20, d21, e20, e21, f20, f21, 'AND'))
    gates.append(GATE(a20, a21, f20, f21, c30, c31, 'XOR'))

    alice_input = {
        'a00': a00,
        'a01': a01,
        'a10': a10,
        'a11': a11,
        'a20': a20,
        'a21': a21,
        'c01': c01
    }   

    bob_input = {
        'b00': b00,
        'b01': b01,
        'b10': b10,
        'b11': b11,
        'b20': b20,
        'b21': b21
    }  

    return gates, alice_input, bob_input, [c30, c31]

def set_key(alice_input, A0, A1, A2):
    alice_key = {}
    alice_key['c0'] = alice_input['c01']
    if A0 == 0:
        alice_key['a0'] = alice_input['a00']
    else:
        alice_key['a0'] = alice_input['a01']
    if A1 == 0:
        alice_key['a1'] = alice_input['a10']
    else:
        alice_key['a1'] = alice_input['a11']
    if A2 == 0:
        alice_key['a2'] = alice_input['a20']
    else:
        alice_key['a2'] = alice_input['a21']
    
    return alice_key