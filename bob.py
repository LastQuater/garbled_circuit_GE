from gate import dec_gate

def set_key(bob_input, B0, B1, B2):
    bob_key = {}
    if B0 == 0:
        bob_key['b0'] = bob_input['b00']
    else:
        bob_key['b0'] = bob_input['b01']
    if B1 == 0:
        bob_key['b1'] = bob_input['b10']
    else:
        bob_key['b1'] = bob_input['b11']
    if B2 == 0:
        bob_key['b2'] = bob_input['b20']
    else:
        bob_key['b2'] = bob_input['b21']
    
    return bob_key

def evaluate(gates, alice_key, bob_key):
    a0 = alice_key['a0']
    b0 =   bob_key['b0']
    c0 = alice_key['c0']
    d0 = dec_gate(gates[0], a0, c0) 
    e0 = dec_gate(gates[1], b0, c0)
    f0 = dec_gate(gates[2], d0, e0)


    a1 = alice_key['a1']
    b1 =   bob_key['b1']
    c1 = dec_gate(gates[3], a0, f0)
    d1 = dec_gate(gates[4], a1, c1) 
    e1 = dec_gate(gates[5], b1, c1)
    f1 = dec_gate(gates[6], d1, e1)


    a2 = alice_key['a2']
    b2 =   bob_key['b2']
    c2 = dec_gate(gates[7], a1, f1)
    d2 = dec_gate(gates[8] , a2, c2) 
    e2 = dec_gate(gates[9] , b2, c2)
    f2 = dec_gate(gates[10], d2, e2)
    c3 = dec_gate(gates[11], a2, f2)

    return ''.join(c3)