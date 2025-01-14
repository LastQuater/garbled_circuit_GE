from gate import GATE

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
    a0 =            alice_key['a0']
    b0 =              bob_key['b0']
    c0 =            alice_key['c0']
    d0 =  gates[0].dec_gate(a0, c0) 
    e0 =  gates[1].dec_gate(b0, c0)
    f0 =  gates[2].dec_gate(d0, e0)


    a1 =            alice_key['a1']
    b1 =              bob_key['b1']
    c1 =  gates[3].dec_gate(a0, f0)
    d1 =  gates[4].dec_gate(a1, c1) 
    e1 =  gates[5].dec_gate(b1, c1)
    f1 =  gates[6].dec_gate(d1, e1)


    a2 =            alice_key['a2']
    b2 =              bob_key['b2']
    c2 =  gates[7].dec_gate(a1, f1)
    d2 =  gates[8].dec_gate(a2, c2) 
    e2 =  gates[9].dec_gate(b2, c2)
    f2 = gates[10].dec_gate(d2, e2)
    c3 = gates[11].dec_gate(a2, f2)

    return ''.join(c3)