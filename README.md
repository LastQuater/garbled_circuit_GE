This project aim to implement a simple garbled circuit to handle $3$-bits $\text{GE}(a, b)$.  In this project, OT is not implement, Bob get input labels from Alice directly. 

All codes are coding under python 3.10.4.

### Usage

```sh
python main.py <number1> <number2>
```

This command gives the result whether the first number is greater or equal than the second number, notice the input number should be in binary representation and be left zero filled to length $3$.



$\text{GE}$  process is in `ge.py`, to test all cases in $3$-bits number, run:

```sh
python ge.py
```

### Normal GE gate

By definition, $\text{GE}(a,b)$ is defined as:
$$
\text{GE}(a,b) = \begin{cases}
1,\quad a\ge b\\
0,\quad a < b
\end{cases}
$$
Below is the induce of the boolean circuit

For $a = a_2a_1a_0,\quad b = b_2 b_1 b_0$

Definite:
$$
c_i = \begin{cases}
1, \quad a_{i - 1}\cdots a_0 \ge b_{i-1}\cdots b_0\\
0,\quad \text{otherwise}
\end{cases}
$$
And we have:
$$
c_{i+1} =  (a_i > b_i) \text{ or } (a_i == b_i\text{ and } c_i == 1) \cdots(1)
$$
$c_0 =  1$ to handle the equal situation.

$(1)$ can be simplify into:
$$
c_{i+1} = a_i\oplus \Big((a_i\oplus c_i)\land (b_i\oplus c_i)\Big)
$$
We build the circuit according to this. 

<img src="imgs\normal_gates.jpg" alt="normal_gates" style="zoom:61%;" />

This figure shows the first layer of the circuit, which can handle $1$-bit $\text{GE}$ with the result $c_1$. For $3$-bits $\text{GE}$, we need to repeat this circuit $3$ times, and  the final result is $c_3$.





### Implement details

- This project use $\text{DES}(n=64)$ as hash function , which is implemented in `des.py` 
- The garbled gate encoding and decoding are implemented in `gate.py`. `XOR`, `AND` , `OR` gate are implemented. Denote the  input of these gate is $a, b$, output is $y$, each line of the garbled table is $\text{ENC}_{a,b}(y) = \text{PRF}_a(b)\oplus y$
- `alice.py` contains process handled by Alice:
  - build the garbled circuit from the boolean circuit, give the input table. Notice our circuit has an initial value $c_0 = 1$, make it a input of Alice. 
  - Set the input according to $a$ and gives a input dictionary. 
- `bob.py` contains process handled by Bob:
  - Receive input label and garbled circuit from Alice, and set the input according to $b$ .
  - Evaluate the boolean value of $\text{GE}(a,b)= c_3$ by decrypting the garbled circuit step by step.
