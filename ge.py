import alice
import bob

def GE(a, b):
    if len(a) != 3 or len(b) != 3:
        raise Exception('Input length error.')

    a2, a1, a0 = int(a[0]), int(a[1]), int(a[2])
    b2, b1, b0 = int(b[0]), int(b[1]), int(b[2])
    
    #Alice build the circuit and send garbled gates table, inputs label and inputs to Bob.
    gates, alice_input, bob_input, c3 = alice.build_circuit()
    alice_key = alice.set_key(alice_input, a0, a1, a2)

    #Bob solve the circuit.
    bob_key = bob.set_key(bob_input, b0, b1, b2)
    result = bob.evaluate(gates, alice_key, bob_key)

    if result not in c3:
        raise Exception('Result error.')
    
    return result == c3[1]

if __name__ == '__main__':
    
    for a in range(8):
        for b in range(8):
            a_bin = bin(a)[2:].zfill(3)
            b_bin = bin(b)[2:].zfill(3)
            result = GE(a_bin, b_bin)
            print("%s %s %s" %(a_bin, '>=' if result else '<' ,b_bin))
            if (a >= b) != result:
                raise Exception('Wrong answer.')
            
    print('All tests complete!')
