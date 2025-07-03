
```
Physics of Quantum
Computing
```
- EL-PH 5553
- Fall 2024


Orientation

- Vladimir Tsifrinovich
- vtsifrin@nyu.edu
- Remote office hour:
- Tuesday at 6 pm.


- Course structure:
- Lectures: every Friday at 2 pm
- At the beginning of the class: HW presentation.

(do not submit HW, HW is not graded)

- After the lecture: quiz based on HW.
- Percentage of final grade: 50%.
- Final presentation: 50%.


Clarification

- I typically give 4 problems for HW and, at the
    beginning of every lecture, invite 4 students to
    present solutions: one student presents a
    solution for one problem. The HW is not graded.
-
- During a quiz you can use everything, except for
    the internet. Certainly, you should not
    communicate with other people.


Our Website

- NYU Brightspace
- Syllabus
- Instruction for the final presentation, and a sample
    presentation
- Lecture notes
- Homework


- Main objectives:
- Understanding the basic ideas in quantum
    computation and information
- Developing basic mathematical skills in the
    field


INTRODUCTION

AND BRIEF HISTORY

OF QUANTUM COMPUTATION


The Origin

- Quantum computation originated on the
    intersection of

(1) computer science,

(2) information theory,

(3) cryptography,

and (4) quantum mechanics.

Brief review of these fields:


1. Computer Science
- The first arithmetical algorithms were developed
in Mesopotamia (Iraq) around 2000 BC.
- 1936: modern computer science

Alan Turing (England): “On Computable

Numbers, with an Application to the

Decision Problem.”

- Universal Turing machine – theoretical digital
    programmable computer.



- In 1940th John von
    Neumann (the US):
- Theoretical model
    of a real digital
    programmable
    computer.


```
The First Programmable Digital
Computer
```
- 1949: University of Cambridge, England.


2. Communication Theory
    - 1948, Claude
       Shannon (the US)
    - Resources needed
       to transfer
       information.


3. Cryptography
- Private key cryptosystem: Alice, Bob, Eve


- Alice and Bob share encryption and
    decryption keys
- 1977, Rivest, Shamir, and Adleman (the US):

RSA public key cryptosystem, where

encryption key differs from the decryption

key.


- Alan Turing
- Rivest, Shamir, and Adleman at MIT


Quantum Mechanics

- Max Planck (Germany), 1900
- Energy of electromagnetic field is quantized.


- Initially: computation of quantized energy levels
    and stationary states.
- After 1950th: superpositional states
- Initially: quantum dynamics of ensemble of
    microscopic particles
- After 1950th: quantum dynamics of a single
    microscopic particle


```
Brief Review of
Computer Speed of a
```
Conventional Computer


```
Laptops: Clock Speed
```
**Clock speed (Hz) –** how many times in a second
electric circuits in the central processing unit (CPU)
turn on and off. Example:
HP (Hewlett-Packard) Zbook -
**Clock Speed 3.1 GHz**


Supercomputers: Computer Speed

- Explanation:
- Fixed-point numbers - integers (e.g. “3”).
- Fixed-point operations (+, -, *, /) operations with
    fixed-point numbers
- “Floating-point numbers” – numbers with the
    decimal points in them (e.g. “2.3”)
- Floating-point operations (+, -, *, /) – operations
    with floating-point numbers.
- Computer speed (performance):
- Number of floating point operations/s (flops)


```
Before 2022: The Fastest
Supercomputer
```
- Fugaku (Japan)
- Speed: 442 Pflops
- (4.42x10^17 flops)
- (Next slide)



For many years researches tried to build an
exascale supercomputer with speed > 1 Eflops.

E stands for Exa = 10^18


```
The First Exascale Supercomputer became
Operational in 2022
```
- OLCF-5, at the Oak Ridge Leadership
    Computing Facility (OLCF) in Tennessee.
    (Another name: Hewlett Packard Enterprise
    Frontier). Speed: **1.1 exaflops**


```
Possible Applications of Exascale
Computers
```
- Climate science, renewable energy,
    genomics, geophysics and artificial
    intelligence.
- Simulate the global climate at a spatial
    resolution of 1 km.


Why Do We Need QC?


Computational Complexity Theory

- Two main complexity classes:
- 1) P (polynomial) problems: there is an
    **efficient algorithm** to solve a problem.
- 2) NP (non-deterministic polynomial): there
    is no efficient algorithm to solve a problem
    but there is an **efficient algorithm** to verify
    the solution.


What is “Efficient Algorithm”?

- Conventional (classical) computer

operates with the digital units “bits”

- Number in binary notation:
- N = .........a 5 a 4 a 3 a 2 a 1 a 0
- ak = 0 or 1
- In decimal notation:
- N = a 020 + a 121 +...


- Physical implementation of a bit:
- Voltage on a capacitor (V 1 or V 2 )
- Magnetic moment in a magnetic domain

(up or down)


- Input L bits (L > 100)
-
**- Efficient algorithm:**

number of computational steps (NCS)
needed to solve the problem is **polynomial**
with respect to L

(increases as Ln, typically n ≤ 3).

- Example: NCS = 2L^3


Polynomial time (P) problems

- Addition, multiplication, solution of an
    ordinary differential equation
- Tractable (solvable) problems


```
Non-Deterministic Polynomial Time
Problems (NP):
```
- Input: L bits
- Number of computational steps **to solve** the
    problem is exponential with respect to L
    (increases typically as 2pL , p =1/3, ½,1, 2, ...)
- Example: NCS = 2L , L = 1000.
- NGS = 2^1000 = 1.07x10^301
- The number of computational steps required **to**
    **verify** a solution increases as Ln.
- Example: L = 1000, n = 2.
- NGS = 1000^2 = 10^6.


- Example of NP Problem:

prime factorization.

- Example:
- 127 x 229 = 29083


- Sub-class of NP problems:
    NP **complete problems**
- the most difficult NP problems
- Example:
- Subset sum problem:
- Given a finite set of positive and negative
    integers.
- Whether any subset sums to zero?


Another Example of a Complete NP Problem

- Geometric packing problem:
Given the dimensions of boxes.
Is it possible to pack them into the trunk?


- Cook, Karp, and Levin (1970th):

```
An efficient algorithm for a complete NP
problem can be used to construct an
efficient algorithm for any NP problem.
```
```
The question of whether an efficient algorithm for
a complete NP problem exists is the most
important unsolved problem in classical
computer science.
```

- So far, in classical computer science NP
    problems are **intractable**.
**- We need a quantum computer which could**
    **solve, at least some NP problems.
- The highest dream would be to solve a**
    **complete NP problem: in this case one could**
    **solve any NP problem.**


Classical Computer’s Logic


Conventional (Classical) Computation

- Change of the values of bits:
- Logic gates
- Logic gates are based on the conventional logic:
- Negation (NOT-gate):
- NOT (True) = False
- NOT (False) = True
- False → 0
- True → 1^


```
Classical logic gates
```
```
Operation of NOT gate (N-gate):
```
```
the Truth Table
```
_ai af_

**0**

**0**

**1**

**1**

```
Final value of
the bit
```
Initial value of a
bit


N-Gate Diagram

a 1 – a


2-Bit Logic Gate “AND”

```
a b
0 0 0
0 1 0
1 0 0
a
b
```
```
ab
```
Input

```
Output
```
```
a AND b = ab
```

Universal Gates.

- “AND” and “NOT” are **universal** for
    classical computation.
- __________________________________
- Addition modulo 2:
- a b : remainder of the fraction (a + b)/2
-
- (Remainder – an amount left after division)


```
NOT AND (NAND) –
a Single Universal Gate
{plus FANOUT (COPY)}
```
```
a b
0 0 1
0 1 1
1 0 1
a
b
```
```
1 ab
```
Input

```
Output
```
```
a NAND b = 1 – ab =
1 ab
```

Example: Binary Half-Adder

```
a b
0 0
0 1
1 0
1 1
```
```
Sum Carry
0 0
1 0
1 0
0 1
```
Input^ Output

```
S = a b, C = ab
```

Half-Adder Circuit Diagram

a
b Sum

```
Carry
```
```
1
```
```
1
```
```
0
```
```
0
```
```
1
```
```
1
```
```
0
```
```
1
```
**S = 0, C = 1**


```
Classical Computer Logic and
Thermodynamics
```
```
Rolf Landauer, 1961:
“Information is Physical”.
```
Computation and transfer of information
are not abstract operations but exist only

through physical representations. (^48)


- A classical computer operates with
    irreversible two-bit gates
- → Conventional logic is the
- “thermodynamical logic”
- Entropy of a system:

S = kB·ln(number of possible states)

Example: 2 wells vs 3 wells

- The 2nd law of thermodynamics: ΔS ≥^ 0.


```
Classical Computer is a Heat
Generator
```
- In a single computational step with a NAND gate:
-
- Entropy S of the available information decreases
    by kBln2

Entropy of the environment ΔSenv > kBln2

→ Classical computer generates heat Q =
TΔSenv > kBT ln2


```
2 nd Law of Thermodynamics:
Classical Computer vs Heat Engine
```
- A heat engine absorbs heat from the hot
    reservoir and does mechanical work. It cannot
    operate without expelling part of the heat into the
    cold reservoir.

```
gas
```
```
hot Cold
```

```
2 nd Law of Thermodynamics:
Classical Computer and Heat Engine
```
- If a classical computer were built before
    the heat engine then

the 2nd law of thermodynamics would be

formulated as:

- A computer based on a classical logic
    cannot operate without generation of heat.
-


Reversible Logic


```
Charles Bennett, 1973:
Reversible Logic
```
- A computer could operate using a
- “reversible logic”!
- Tommaso Toffoli, 1980:
- Universal Control-Control-Not 3-bit gate
    CCN12,3
- 111 → 110
- 110 → 111
- All other combinations do not change


```
55
```
Toffoli → AND (NAND) Gate

### • 000 → 000 000 →(00)0

### • 001 → 001

### • 010 → 010 010 →(01)0

### • 011 → 011

### • 100 → 100 100 →(10)0

### • 101 → 101

### • 110 → 111 110 →(11)1

### • 111 → 110

### •

( _a_ , _b_ , _c_ ) → ( _a_ , _b_ , _c_ ⊕ _ab_ )^55


Toffoli Circuit Diagram

**a**

**b**

**c c ab**

```
b
```
```
a
```

Toffoli → NAND

**a**

**b**

**1 1 ab**

```
b
```
```
a
```

Toffoli → FANOUT (Copy)

```
1
x
0 0 x · 1 = x
```
```
x
```
```
1
```

```
Quantum Computer (QC)
Paul Benioff (1980)
```
- Computer based on quantum physics is possible
- Bit – stationary state of an atom or ion
- Trivial advantage:
- Huge possible information density
- Take 1 nm: Volume density 10^21 bits/cm^3
- Areal density 10^14 bits/cm^2
- Typical interatomic distance in solids: 0.2 nm.
- Currently, areal density < 10^12 bits/cm^2


Richard Feynman (1982)

- QC can simulate quantum dynamics in
    other systems
- →QC can be much more powerful than a
    classical computer


```
David Deutsch, 1985:
Superpositional States
```
- The most important power of QC:
- Using superpositional states
- C 0 |0> + C 1 |1>
- Quantum (projective) measurement:
- |C 0 |^2 – probability to collapse to
    the state |0>
- |C 1 |^2 – probability to collapse to
    the state |1>


Quantum Logic

- Quantum bit (qubit)
- Superposition of true and false
- A quantum logic gate must change all the states of
    superposition simultaneously
- Example. NOT (N) gate:
- N (C 0 |0> + C 1 |1>) = (C 0 |1> + C 1 |0>)
- {One qubit gate – changes the state of a single qubit}


Example: Hadamard (H) Gate

### • H|0> = (|0> + |1>)/√ 2

### • H|1> = (|0> - |1>)/√ 2


```
Creation of a Uniform Superposition of
States
```
- Two H gates acting on two qubits in the
    ground state create uniform superposition
    of four numbers:

### • H 1 H 2 |00>

### • = [(|0> + |1>)/√2] [(|0> + |1>)/√2]

### • (|00> + |01> + |10> + |11>)/2


```
Loading Numbers with One-Qubit
Hadamard Gates
```
- Three H gates can create superposition of
    eight numbers
- (|000> + |001> +... + |111>)/√ 8
- L qubits: we can load 2L numbers at a time
    using L one-qubit gates!
- We create superposition of all possible
    numbers.


**Control Not (CN-gate) Operation of CN-gate**

_ci tf_

**0**

**1**

**0**

(^11)
_ti cf_
**0 0 0
0 0 1**
(^01)
**1 1 1**
Control qubit – “c”
Target qubit – “t”
Two-Qubit Quantum Logic Gates


```
Universal Quantum Computations
Using Quantum Logic Gates
```
- Barenco et al., 1995
- Theorem:
- For universal QC we need universal one-
    qubit gates and a two-qubit Control-Not
    (CN) gate.


Two Registers and a Function

- Using two registers we can load 2L values of
    a function
- Example:
- 2 qubits are in the x-register, 1 qubit is in the
    y-register
- Initial state:
- |x,y> = |00,0>


- |x,y> = |00,0>
- H 1 H 2 |00,0> =
- (|00,0> + |01,0> + |10,0> + |11,0>)/2
- Now CN 23 gate changes the value of y:
- y → y(x).
- 2-control qubit, 3-target qubit:
- (|00,0> + |01,1> + |10,0> + |11,1>)/2
- Periodic function y(x)


```
7070
```
```
Computing a Function
```
- In general:
- We can load 2L values of a function with a
    polynomial number of gates!
- 300 +300 qubits: 2^300 = 2.04x10^90 values of a
    function.
- The number of electrons in the visible Universe

is about 10^80.^

- (The diameter of the visible Universe is about
    90 Gly.)
- How to use this computational power?


Quantum Algorithms


```
Peter Shor, 1994:
The First Practical Quantum
Algorithm
```
- The quantum algorithm for prime

factorization.


Prime Factorization

- Carl Gauss:
- “The dignity of science demands that every
    aid to the solution of such a celebrated
    problem be zealously cultivated”.


- Statement: There is no efficient classical
    algorithm for prime factorization
- (It is not proved!)
- Since 1970th the main cryptosystem RSA
    (Rivest, Shamir, and Adleman) is based on
    this statement.
- Bank cards are based on this statement.


Financial Security is Based on RSA

- No one can fake bank cards.
- Why?
- A bank’s computer chooses at random two
    prime factors N 1 and N 2 ,
- multiply them,
- assign the product N = N 1 N 2 to your account
- saves number N in a bank’s computer
- encode your bank card with factor N 1 ,
- and erases both factors.


- The bank’s computer holds number N and
    your security code, say “1234”
- It does not hold the factors N 1 and N 2
- Only your bank card holds one of the
    factors!


```
Simple Trials on a Classical
Supercomputer
```
- N - 200-digit number:
- Max value N = 10^200 -1
- For L bits the max number is 2L – 1
- We need **Lmin = 665 bits**
- Simple trials:
- We have to try about N1/2 = 2L/2 = 10^100 numbers


- Assume an exascale supercomputer with 3x10^18
    trials/s

It would take about 10^100 /3x10^18 ≈^ 3x10^81 s,

about 10^74 years.

The age of our Universe is about 1.4x10^10 years.


Shor’s Quantum Algorithm

- The Shor’s algorithm is efficient!
- Polynomial number of computational steps
    (less than L^3 )
- For L = 665 qubits the number of steps is
    about 665^3.
- For an exascale quantum computer with 10^18
    operations/s:
- 6653 /10^18 ≈ 0.1 ns.


Lov Grover, 1996

- Quantum speed-up for a complete NP
    problem: search in unsorted data.
- Example: number of entries M = 9.


Grover’s Algorithm

- √M steps instead of M/2 steps
- It can be used for intermediate size input
- Example:
- Number of entries M = 2x10^29
- Number of computational steps ≈ 1029
    Exacomputer with a speed of 10^18 /s:

about 10^11 s ≈ 3000 years


- Using Grover’s algorithm
- √M = 3x10^14 operations
- With quantum exacomputer:
- 3x10^14 /10^18 = 300 μs
- Impressive but still inefficient!


NP Complete Problem

- Is it possible to find a quantum efficient
    algorithm for a complete NP problem?
- Probably, no.
- (No one proved that it does not exist.)
-
- Clay Math Institute in Massachusetts:
- $1,000,000 reward for an efficient
    algorithm for an NP complete problem


New Physical Principle

- Aaronson, 2008:
- A physical computer, which can efficiently
    solve a complete NP problem is
    impossible.
- “Informational principle”


Conclusion

- 1. QC will efficiently solve some important
    NP problems with large size input (e.g.
    prime factorization).
- 2. QC will speed up the solution of
    complete NP problems with an
    intermediate size input.


The Main Tasks for QC

- 1. Search for new quantum algorithms for
    various NP problems.
- 2. Physical implementation of QC.

### • ________________________________

### •


The Main Players in QC


Mathematical Background


Complex Numbers

- “i” = (-1)1/2
- i^2 = -1
- Standard form of a complex number:
- z = a + i·b,^ “a” and “b” –real numbers
-^
- a = Re(z),
-^
- b = Im(z)


```
Geometrical Interpretation of a Complex
Number
```
```
|z|
```
```
φ
```
Modulus: |z| = (a^2 + b^2 )1/2
Argument φ: angle from the real axis: 0 ≤ φ < 2π.


Exponential Form of Complex Numbers

- z = |z|exp(iφ)^
- exp(iφ) = cos(φ) + i·sin(φ)
- **Complex conjugate of z** :
- z* = a – ib = |z|exp(-iφ)
- zz* = a^2 + b^2 = |z|^2
- Useful equality:
- |z 1 z 2 |= |z 1 |·|z 2 | 4


2D Vector Space

Euclidian 2D-space (e.g. x-y-plane) “generates” a 2D

real vector space. Every point → position vector **r**.

The main properties of a 2D real vector space:

1) Sum of vectors = vector

2) Vector * (real number) = vector

Standard basis: unit basis vectors **i** and **j** :

**r** = **i** x **+ j** y


Non-Standard Basis and Dot Product

```
Non-standard basis:
Any unit vectors n 0 and n 1 ( n 1 is normal to n 0 )
r = C 0 n 0 + C 1 n 1
Example.
```
```
Scalar or dot product:
rp • rq.
The length (magnitude) of a vector r :
( r • r )1/2 6
```

2D Complex Vector Space

- **Abstract “ket” – vectors |ψ>**^ (Dirac notation)^
- Standard basis or standard representation.
- Unit basis vectors: |0> and |1>
- Any ket vector |ψ>,

|ψ> = C 0 |0> + C 1 |1>,

C 0 and C 1 – any complex numbers.

All these vectors form 2D complex vector space if

1) Sum of vectors = vector

2) Vector * (complex number) = vector


```
8
```
- Sum of vectors:
- (C 0 |0> + C 1 |1>) + (D 0 |0> + D 1 |1>)
- = (C 0 +D 0 )|0> + (C 1 + D 1 )|1>
- Unit of addition: 0·|0> + 0·|1> - “empty vector”
- Vector times complex number “z”:
- z·(C 0 |0> + C 1 |1>) = zC 0 |0> + zC 1 |1>
- Unit of multiplication: z = 1.
- Generalization:
- nD-complex vector state: |0>, |1> ,..., |n-1>


2D Hilbert Space

- Complex vector space with a scalar product.
- In a Hilbert space every vector has a real magnitude
    (“length”) which is called a **“norm”**.
- In a Hilbert space: **dual “bra” vectors <ψ|**
- If |ψ> = C 0 |0> + C 1 |1>,

the dual bra vector:

<ψ| = C 0 * <0| + C 1 * <1|.

- Dual basis vectors: <0|, <1|^


**Inner Product for <bra| and |ket>**

- For the basis vectors: <k|(inner product) |n>,

<k|n> - “k-n-bracket”:

- <k|n> = δkn (Kronecker symbol)
- For two arbitrary vectors :
- <ψ|(inner product) |φ>

<ψ|φ> - “psi-fi-bracket” – a complex number,

which can be found using a distributive property


Computation of Bracket

- |ψ> = C 0 |0> + C 1 |1>, |φ> = D 0 |0> + D 1 |1>
- <ψ|φ> = (C 0 *<0| + C 1 *<1|) (D 0 |0> + D 1 |1>)

= **C 0 *D 0 + C 1 *D 1.**

- If <ψ|φ> = 0, they are called “ **orthogonal**
    **vectors** ”


Norm of a Vector

- <ψ|ψ > = (C 0 *<0| + C 1 *<1|) (C 0 |0> + C 1 |1>)
- = |C 0 |^2 + |C 1 |^2 – real positive!
- Norm of a vector:
- || ψ|| = <ψ|ψ>1/2
- = (|C 0 |^2 + |C 1 |^2 )1/2^
- {Comparison: for a real space: A = ( **A●A)1/2** } 12


- Vectors of norm 1 (“unit vectors”)
- || ψ|| = 1.
- “Unit vectors”
- |0> and |1> are the unit vectors.
- **A state of a qubit is described by unit vectors only.**
- **In future we will consider only unit vectors.**

In quantum mechanics unit vector – “ **vector of state”.**

- Coefficients C 0 and C 1 – “ **amplitudes** ”
- Any two **orthogonal** unit vectors may form **“non-**
    **standard basis”**


- Example 1: orthogonal unit vectors |vk> (k = 0,1)
- |v 0 > = C 0 |0> + C 1 |1> = 2-1/2 (|0> + |1>),
- C 0 = C 1 = 2-1/2. →^ |C 0 |^2 + |C 1 |^2 = 1
- |v 1 > = D 0 |0> + D 1 |1> = 2-1/2 (|0> - |1>)
- D 0 = 2-1/2, D 1 = - 2-1/2. →^ |D 0 |^2 + |D 1 |^2 = 1
-^
- |vk> are the orthogonal vectors:
- <v 0 |v 1 > = C 0 *D 0 + C 1 *D 1 = 1/2 – 1/2 = 0


- Example 2: orthogonal unit vectors |wk> (k = 0,1)
- |w 0 > = 2-1/2 (|0> + i|1>),^
- |w 1 > = 2-1/2 (|0> - i|1>)
- <w 0 | = 2-1/2 (<0| - i <1|)
- <w 1 | = 2-1/2 (<0| + i <1|)
- <w 0 |w 0 > = (1/2)(1 + 1) = 1,
- <w 1 |w 1 > = 1
- <w 0 |w 1 > = (1/2)(1 - 1) = 0


Transfer to a New Basis (Representation)

- Example:
- |ψ> = C 0 |0> + C 1 |1>
- Transfer to the basis |vk>.


Solution

- |v 0 > = 2-1/2 (|0> + |1>)
- |v 1 > = 2-1/2 (|0> - |1>)
- |0> = 2-1/2 (|v 0 > + | v 1 >)
- |1> = 2-1/2 (|v 0 > - | v 1 >)
- |ψ> = C 0 |0> + C 1 |1>
- = 2-1/2[C 0 (|v 0 > + | v 1 >) + C 1 (|v 0 > - | v 1 >)]
- =^2 **-1/2 [(C 0 + C 1 )|v 0 > + (C 0 - C 1 )|v 1 >]**


```
181818
```
Matrix Representation of Ket Vectors

- Ket vector can be represented by a column matrix
- Basis matrices (in the standard basis)

(^)
0
0 1
1
1
| 0
0
0
| 1
1
| | 0 | 1
_C
C C
C_
ψ
⎛ ⎞
>→ ⎜ ⎟
⎝ ⎠
⎛ ⎞
>→ ⎜ ⎟
⎝ ⎠
⎛ ⎞
>= > + >→ ⎜ ⎟
⎝ ⎠


Matrix Representation of Bra Vectors

- Bra vector – **adjoint** of a corresponding column
    matrix (row matrix)
- **Adjoint: transpose and complex conjugate**
- Basis bra vectors (in the standard basis)

```
19
```
( )

( )

( )

```
0 1
* * * *
```
0 | 1 0

1 | 0 1

If | | 0 | 1

| 0 | 1 |

_C C_

_C C C C_

ψ

ψ

< →

< →

>= > + >

< = < + < →


Inner Product with Matrices

- |ψ> = C 0 |0> + C 1 |1>
- |φ> = D 0 |0> + D 1 |1>
- <ψ|φ> bracket in the algebraic and matrix form:
- <ψ|φ> = (C 0 *<0| + C 1 *<1|)(D 0 |0> + D 1 |1>)
- = C 0 *D 0 + C 1 *D 1

```
20
```
( )

```
* *^0 * *
0 1 0 0 1 1
1
```
```
D
C C C D C D
D
```
```
⎛ ⎞
⎜ ⎟ = +
⎝ ⎠
```

```
21
```
- Common Phase Factor
- In quantum mechanics common phase factor
    exp(iφc) is not important (symmetry).
- **We can always multiply the whole vector of state**
    **by the common phase factor.**

Example. If |ψ> = C 1 |1> = exp(iφ 1 ) |1>

We can multiply vector |ψ> by the common phase

```
factor exp(-iφ 1 ).
```
In this case |ψ> → |1>

.


Non-Zero Amplitudes

Let |ψ> = C 0 |0> + C 1 |1>

= R 0 exp(iφ 0 ) |0> + R 1 exp(iφ 1 ) |1>

Rk = |Ck|, Rk > 0

We can multiply vector

|ψ> = R 0 exp(iφ 0 ) |0> + R 1 exp(iφ 1 ) |1>

by the common phase factor exp(-iφ 0 ).

In this case |ψ> → R 0 |0> + R 1 exp[i(φ 1 – φ 0 )] |1>


**General Property of a Vector of State**

```
→ We can change any vector of state to
either vector |0>, or vector |1>, or vector
R 0 |0> + R 1 exp(iφ) |1>,
(R 0 , R 1 > 0, R 02 + R 12 = 1),
without change of the qubit physical state.
```

Spherical System of Coordinates

- Unit vector can be described by polar angle θ and
azimuthal angle φ:
- 0 ≤ θ ≤ π,
- 0 ≤ φ < 2π.

```
x
```
```
y
```
```
z
```
```
φ
```
```
θ
```

Bloch Form of a Unit Vector

Consider a vector of state:

|ψ> = R 0 |0> + R 1 exp(iφ) |1>,

R 02 + R 12 = 1

We can write it in the “ **Bloch form** ”:

- |ψ> = cos(θ/2)|0> + sin(θ/2)exp(iφ)|1>

0 ≤ θ ≤ π, 0 ≤ φ < 2π.

**Any vector describing a qubit state can be
changed to the Bloch form.**^25


Example

- |ψ> = 2-1/2 exp(iπ/4)|0> + 2-1/2 exp(iπ/2)|1>
- → 2-1/2|0> + 2-1/2 exp(iπ/4)|1>
- = cos(π/4)|0> + sin(π/4) exp(iπ/4)|1>
- = **cos[(π/2)/2]|0> + sin[(π/2)/2] exp(iπ/4)|1>**^
- |ψ> = cos(θ/2)|0> + sin(θ/2)exp(iφ)|1> 26


Visualization: the Bloch Vector

- Bloch vector is a unit vector in the 3D-space
**b** = **b** (θ,φ) which corresponds to the vector of state in the Bloch form:
- |ψ> = cos(θ/2)|0> + sin(θ/2)exp(iφ)|1>
-^ x

```
y
```
```
z
```
```
φ
```
```
b (θ,φ)
```

Problem

- The Bloch vector **b** points in the positive z-
    direction. Write the corresponding vector |ψ>
    in the Hilbert space in the Bloch form.


Solution

- |ψ> = cos(θ/2)|0> + sin(θ/2)exp(iφ)|1>
- θ = 0
- |ψ> =|0>
- (If the Bloch vector points in the negative z-
    direction: θ = π, |ψ> =|1>)
- Standard basis |0> and |1> - **the z-basis.** 29


Problem

- The Bloch vector points in the positive x-
    direction. Find the corresponding vector |ψ> in
    the Hilbert space in the Bloch form.


Solution

- |ψ> = cos(θ/2)|0> + sin(θ/2)exp(iφ)|1>
- θ = π/2, φ = 0
- |ψ> = cos[(π/2)/2]|0> + sin[(π/2)/2]|1>

= 2-1/2 (|0> + |1>) = |v 0 >

- (If the Bloch vector points in the negative x-
    direction: |ψ> =|v 1 >)
- Basis |v 0 > and |v 1 > - **the x-basis.** 31


Summary of Lecture 2

- Complex numbers: geometrical representation,
    modulus and argument, standard and exponential
    forms, complex conjugate.
- 2D complex vector space, Dirac notation “cat” for
    vectors.
- Hilbert space: dual vectors “bra”, inner product
    “bracket”, norm of a vector.
- Standard and non-standard bases. Transfer to a
    different basis.
- Matrix representation of vectors.
- Bloch form of a unit vector, Bloch vector. 1


OPERATORS


**Operators. Outer Product (ket-bra)**

- Operator transforms one vector into another vector
- Linear operators: A(p|ψ> + q|φ>) = pA|ψ> + qA|φ>
- Elementary operators in Dirac notation:
- |k><n| acts on |p>: |k><n|p> = δnp|k>^
- Elementary operators in Hubbard notation:
- |k><n| = Xkn – **Hubbard operators**
- Xkn|p> = δnp|k> ,^


```
4
```
- Action of an operator on a bra vector:
- The bra vector is placed to the left of the operator.
- Action of elementary operators |k><n| on a bra vector
    <p|:
- <p|k><n| = δkp<n|,
- or with Hubbard operators
- <p|Xkn = δkp<n|
- Arbitrary operator can be written as a sum of Hubbard
    operators with complex coefficients:^
- A = ∑kn aknXkn,^


Matrix of Coefficients

```
00 01
```
```
, 10 11
```
A = X ( )

```
kn
kn
k n
```
```
a a
a A
a a
```
```
⎛ ⎞
→ = ⎜ ⎟
⎝ ⎠
```
∑

```
Coefficients akn – matrix elements
```

Pauli Operators σk and Identity

Operator E.

- Identity operator E = X^00 + X^11 (E = I = σ 0 )
- σx = σ 1 = X^01 + X^10
- σy = σ 2 = -iX^01 + iX^10
- σz = σ 3 = X^00 - X^11
- Another set of elementary operators:
- σk (k = 0,1,2,3)


Property of Coefficients akn

- A = ∑kn aknXkn
- For any fixed “k” and “n”:
- akn = < k | A | n >

Prove using A = Σp,q apq Xpq


Proof

- < k | A | n >
- = < k | Σp,q apq Xpq | n >
- = < k | Σp,q apq δqn |p>
- = <k | Σp apn |p>
- = Σp apn <k|p>
- = Σp apn δpk
- = akn.


```
9
```
Identity Operator

- Identity operator E = X^00 + X^11
- (E = σ 0 = I)
- Elementary operators σk (k = 0,x,y,z)
- E = ∑k Xkk = ∑kn δknXkn^
- Properties of the identity operator
- E| ψ> = | ψ>


Proof

- E = ∑k Xkk,^ | ψ> = ∑p Cp|p>.^
- E| ψ> = ∑k Xkk ∑p Cp|p>
- = ∑k,pCpXkk|p>
- = ∑k,pCp δpk|k>
- = ∑p Cp|p>
- = | ψ>.


Operator’s Algebra

- Sum of operators: C = A + B = B + A
- ckn = akn + bkn
- Zero operator: “empty operator” akn = 0
- Product of operator A and complex number q:
    C = qA = Aq
- ckn = qakn


Product of Operators

### • C = AB

- Xkn Xpq = |k><n|p><q| = δnp Xkq^
- Example:
- A = 2X^00 – 3X^01
- B = 4X^01 – (5i)X^11
- 1) Find C = AB
- 2) Find D = BA


Solution

### • A = 2X^00 – 3X^01

- B = 4X^01 – (5i)X^11
- C = AB = {2X^00 – 3X^01 }{4X^01 – (5i)X^11 }
- = 8 X^01 + (15i)X^01
- = (8 + 15i)X^01.
- D = BA = {4X^01 – (5i)X^11 } {2X^00 – 3X^01 }
- = Empty operator
- **No commutative property.** 13


- Unit of multiplication of operators:

identity operator E

- AE = EA = A


```
Proof
```
- A = ∑kn akn Xkn^ E = ∑p Xpp
- AE = ∑kn akn Xkn ∑p Xpp^
- = ∑knp akn Xkn Xpp^
- = ∑knp akn δnp Xkp^
- = ∑kn akn Xkn^
- = A


```
Matrix Form of Operators (A = ∑kn aknXkn)
```
```
00
```
```
11
```
```
01
```
```
10
```
Hubbard matrices:

1 0
X
0 0
0 0
X
0 1
0 1
X
0 0
0 0
X
1 0

```
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠ 16
```

Product of operators is equivalent to the
matrix product.

(^0001)
, 10 11
00 01
, 10 11
00 01 00 01
10 11 10 11
= X
= X
_kn
kn
k n
pq
pq
p q
a a
A a
a a
b b
B b
b b
a a b b
AB
a a b b_
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
⎛ ⎞⎛ ⎞
→ ⎜ ⎟⎜ ⎟
⎝ ⎠⎝ ⎠
∑
∑


Proof (Skip)

```
18
```
( )

( )

```
00 01
, 10 11
```
```
00 01
, 10 11
```
```
, , ,
```
```
, , , ,
```
= X

= X

( ) ( )( )

```
kn
kn
k n
```
```
pq
pq
p q
kn pq
kn pq
k n p q
```
```
kq kq kq
kn nq kn nq kq
k n q k q n k q
```
```
kq kn nq
n
```
```
a a
A a A
a a
```
```
b b
B b B
b b
```
_C AB a b X X p n_

_C a b X a b X c X_

_C A B c a b_

```
⎛ ⎞
→ = ⎜ ⎟
⎝ ⎠
⎛ ⎞
→ = ⎜ ⎟
⎝ ⎠
= = → =
```
```
⎛ ⎞
= = ⎜ ⎟ =
⎝ ⎠
= → =
```
∑

∑

∑

∑ ∑ ∑ ∑

∑


```
Action of operator on a ket-vector is equivalent
to the corresponding matrix product. (The same
is true for bra-vectors.)
```
( )

```
00 01
, 10 11
```
```
0
1
```
```
00 01 0
```
(^10111)
A = X ( )
| | ( )
| ( )
_kn
kn
k n
p
p
a a
a A
a a
C
C p
C
a a C
A A
a a C_
ψ ψ
ψ ψ
⎛ ⎞
→ = ⎜ ⎟
⎝ ⎠
⎛ ⎞
>= > → = ⎜ ⎟
⎝ ⎠
⎛ ⎞⎛ ⎞
>→ = ⎜ ⎟⎜ ⎟
⎝ ⎠⎝ ⎠
∑
∑


Proof (Skip)

```
0
1
```
```
00 01 0 00 0 01 1 0
```
(^101111001111)
( )( ) ( )
_k kn n
n
D
A
D
a a C a C a C D
a a C a C a C D
D a C_
ψ
⎛ ⎞
= Φ = ⎜ ⎟
⎝ ⎠
⎛ ⎞⎛ ⎞ ⎛ + ⎞ ⎛ ⎞
⎜ ⎟⎜ ⎟ = ⎜ ⎟ = ⎜ ⎟
⎝ ⎠⎝ ⎠ ⎝ + ⎠ ⎝ ⎠
= ∑


Continue (Skip)

```
,
```
```
, ,
```
```
,
```
```
| | |
```
```
| X |
```
```
|
```
```
| |
```
```
k
k
kn
kn p
k n p
```
```
kn p pn
k n p
```
```
kn n k
k n k
```
```
k kn n
n
```
```
A D k
```
```
A a C p
```
```
a C k
```
```
a C k D k
```
```
D a C
```
```
ψ
```
```
ψ
```
```
δ
```
```
>= Φ >= >
```
```
>= >
```
= >

= >= >

```
=
```
∑

∑ ∑

∑

∑ ∑

∑


- Operations with vectors and operators are
    equivalent to the corresponding operations with
    matrices
- Sometimes we use the same notation for vector and
    column matrix and for operator and square matrix.
- Properties of operators and properties of the
    matrices are the same.
- In particular associative property:
- {AB}C = A{BC}
- No commutative property
- If AB = BA: commutative operators


Non-Standard Basis |b 0 >, |b 1 >

- Vector |ψ> in a non-standard basis |bk> :
- |ψ> = ∑k C’k |bk>
- Operator A in basis |bk>
- A = ∑kna’kn |bk ><bn|
- a’kn = <bk|A|bn>^


Identity Operator in Arbitrary Basis

- Matrix elements of the identity operator

are the same in any basis:

- e’kn = <bk|E|bn> = <bk|bn> = δkn.
- E = ∑k |bk><bk|

```
1 0
(E) =
0 1
```
```
⎛ ⎞
⎜ ⎟
⎝ ⎠
```

```
Eigenvalues and Eigenvectors of
Operators
```
- Eigenvectors | ψ > and eigenvalues λ of an

operator A satisfy to the equation:

A| ψ > = λ| ψ >

(Equations do not depend on basis.)

```
To find eigenvalues λ consider the matrix
(A – λE) and equate its determinant to zero:
```
det (A – λE) = 0 Solutions - eigenvalues.


Property of a Diagonal Operator

- For a diagonal operator the matrix
    elements are its eigenvalues.
- Proof.

```
00
11
```
```
00
11
```
```
00 11
```
```
0
= X
0
```
0
( )
0

( ) ( )( ) 0

```
kk
kk
k
```
```
a
A a
a
```
```
a
A E
a
```
_Det A E a a_

```
λ
λ
λ
```
λ λ λ

```
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
⎛ − ⎞
− → ⎜ ⎟
⎝ − ⎠
− = − − =
```
∑


- λ 0 = λ 1 **degenerate eigenvalues**
- A| ψ > = λ| ψ >^

We will choose the following

“physical” eigenvectors | ψ >:

**| ψ > = C 0 |0> + C 1 |1>**

**has norm 1 and real amplitude C 0** ≥ **0**


Eigenvectors of Identity Operator

### • E = X^00 + X^11.

- Matrix representation: diag (1, 1)
- Degenerated eigenvalues 1, 1.
- **Any vector is the eigenvector of E** (E|ψ> = |ψ>)
- The same is true for qE.


Example

- Find eigenvalues and eigenvectors for X^00


Solution (|ψ> = ∑k Ck |k>)

```
00
```
```
00
0 1 0 1
0 0 1
1
0 0
```
```
1 0
0 0
```
1 ) 1

```
( | 0 | 1 ) 1 ( | 0 | 1 )
| 0 | 0 | 1
0
```
- any number, we choose = 1
Eigenvector | | 0

_X_

```
X C C C C
C C C
C
C C
```
λ

ψ

```
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
=
> + > = ⋅ > + >
>= > + >
=
```
>= >


```
00
```
```
00
0 1 0 1
0
0
1 1
```
```
1 0
0 0
2 ) 0
```
```
( | 0 | 1 ) 0 ( | 0 | 1 )
| 0 " "
0
```
- any number, we choose = 1
Eigenvector | >= | 1

_X_

_X C C C C_

_C empty vector_

_C_

_C C_

λ

ψ

```
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
=
```
```
> + > = ⋅ > + >
>=
=
```
>


Normal Operators

An operator X^00 has two different eigenvalues

and two corresponding eigenvectors.

Operators qE and operators having two different

eigenvalues and two corresponding eigenvectors

are called the “normal operators”.


Problem with “Abnormal Operator”

- Find eigenvalues and eigenvectors for X^01


Solution

```
01
```
```
2
01
0 1 0 1
1
1
0 0
```
```
1
```
- E
    0
0
( | 0 | 1 ) 0 ( | 0 | 1 )
| 0 " "
0
is any number, we choose C = 1

The only eigenvector | >= | 0

```
X
```
```
X C C C C
```
_C empty vector_

_C_

_C_

```
λ
λ
λ
```
λ

```
ψ
```
```
⎛− ⎞
→⎜ ⎟
⎝ − ⎠
=
> + > = ⋅ > + >
>=
=
```
```
>
```

Normal Operators

- Consider a “ **normal operator** ” A with two
    eigenvectors.

Let its eigenvalues are λ 0 and λ 1

(at least one of them ≠ 0)

and corresponding eigenvectors |b 0 > and |b 1 >


```
Spectral Decomposition of a Normal
Operator
```
- Consider |b 0 > and |b 1 > as basis vectors
- In this basis:
- a’kn = <bk|A|bn> = <bk| λnbn> = λn δkn^
- A = λ 0 |b 0 ><b 0 | + λ 1 |b 1 ><b 1 | = ∑n λn |bn><bn| Diagonal
    operator!
- Normal operator A is written in its own basis
    (representation)
- or
- “Spectral decomposition” of normal operator A.


Completeness Relation

- A = λ 0 |b 0 ><b 0 | + λ 1 |b 1 ><b 1 |
- For the identity operator any vectors are eigenvectors
    with eigenvalues 1.
- E = |b 0 ><b 0 | + |b 1 ><b 1 |

→ For any basis |bk> :

∑k |b **k** ><b **k** | = E – **completeness relation**


Matrix Form of an Operator in its Own

Basis – Diagonal Matrix

```
0
```
```
1
```
```
0
( )
0
```
_A_

λ

λ

```
⎛ ⎞
= ⎜ ⎟
⎝ ⎠
```
A = λ 0 |b 0 ><b 0 | + λ 1 |b 1 ><b 1 |


Construction of the Normal Operators

- 1. Consider any Bloch vector **b** (θ,φ) in the upper
    hemisphere and the opposite vector (- **b** ) in the
    bottom hemisphere.
- 2. Consider the corresponding vectors in the
    Hilbert space |b 0 > and |b 1 >.
- 3. Take any two complex numbers λ 0 and λ 1.
- 4. Construct the normal operator
- A = λ 0 |b 0 ><b 0 | + λ 1 |b 1 ><b 1 | 39


**Adjoint of operator A = A† (dagger)**

|k><n|† = |n><k| or (Xkn)† = Xnk

A = akn Xkn^

A† = a*kn Xnk

(A†)^ = transpose

and complex conjugate

```
∑ k , n
```
```
00 10
01 11
```
```
a a
a a
```
```
∗ ∗
∗ ∗
```
### ⎛ ⎞

### ⎜ ⎟

### ⎝ ⎠

```
k , n
```
∑

```
00 01
10 11
```
### ( )

```
a a
A
a a
```
### ⎛ ⎞

### = ⎜ ⎟

### ⎝ ⎠


Property of Adjoint Operation

- |ψ><φ|† = |φ><ψ|.
- Proof:
- |ψ> = ∑k Ck |k>, |φ> = ∑n Dn |n>
-^
- |ψ><φ| = ∑k Ck |k> ∑n D*n <n|
- = ∑kn Ck D*n |k><n|
- |ψ><φ|† = ∑kn C*k Dn |n><k|
- |φ><ψ| = ∑n Dn |n> ∑k C*k <k| = ∑kn C*k Dn |n><k|


```
Action of an Adjoint Operator on a Dual
Vector
```
- If A|ψ> = |Φ>
- Then < ψ|A† = < Φ|
- Proof (Skip)
- A|ψ> = ∑kn akn Xkn ∑p Cp |p>
- ∑knp aknCp δnp |k>
- = **∑kn aknCn |k> = |Φ>**
- < ψ|A† = ∑p Cp* <p| ∑kn akn* Xnk^
- = ∑knp akn* Cp* δnp <k|
- = **∑kn akn* Cn* <k| = < Φ|** 42


Adjoint of a Product of Two Operators

- (AB)† = B† A†
- Proof (Skip)
- A = ∑kp akp Xkp ,^ B = ∑qn bqn Xqn^
- AB = ∑kp akp Xkp ∑qn bqn Xqn^ (q = p)
- = ∑k,p,n akpbpnXkn^
- **(AB)† = ∑k,p,n akp* bpn* Xnk**^
-^
-^


Continue

- **(AB)† = ∑k,p,n akp* bpn* Xnk**
- A = ∑kp akp Xkp ,^ B = ∑qn bqn Xqn^
- B† A† = ∑qn bqn* Xnq ∑kp akp* Xpk^ (q = p)
- = **∑k,p,n bpn* akp* Xnk**^


Adjoint of a Sum of Two Operators

### • (A+B)† = A† + B†^

- A + B = ∑kn (akn + bkn)Xkn
- (A+B)† = ∑kn (akn* + bkn* )Xnk
- = ∑kn akn* Xnk +∑kn bkn* Xnk = A† + B†


For a normal operator A, A† commutes with A:
A A† = A† A
Proof:
A = ∑k λk |bk ><bk| (<bk|bn> = δkn)
A† = ∑n λ*n |bn ><bn|

A A† = ∑k λk |bk ><bk| ∑n λ*n |bn ><bn| n = k = ∑k |λk|^2 |bk ><bk|

A†A^ = ∑n λ*n |bn ><bn| ∑k λk |bk ><bk| n = k =∑k |λk|^2 |bk ><bk|


Function of a Normal Operator
Spectral decomposition of a normal operator

A = ∑kλk | b **k** >< b **k** |

Function of an operator:

f(A) = ∑kf(λ **k** ) | b **k** ><b **k** |

Examples.

Exp(X^00 ) = exp(1)|0><0| + exp(0)|1><1|

= eX^00 + X^11


Two New Terms

- A = λ 0 |b 0 ><b 0 | + λ 1 |b 1 ><b 1 |
- 1. If λk are real numbers, then A is called a Hermitian

```
operator.
```
- 2. If |λk| = 1, then A is called a unitary operator.


Example

- Take |bk> = |vk>, and λk = (1, -1)
- We construct the normal operator which is
    Hermitian and unitary:
- A = |v 0 ><v 0 | - |v 1 ><v 1 | = σx
-^


Property of a Unitary Operator

- Eigenvalues: |λk| = 1.
- λk = exp(iαk)
- A)
- UU† = U†U = E^

(can be used as a definition of a unitary operator)


UU† = E: Proof

- U = ∑k exp(iαk)|bk><bk|
- U† = ∑n exp(-iαn)|bn><bn|
- UU† = ∑k exp(iαk)|bk><bk| ∑n exp(-iαn)|bn><bn|
- = ∑k,n exp{i(αk – αn)} |bk><bk|bn><bn|^ n=k
- = ∑k|bk><bk| = E


B) If U is a unitary operator

and U | ψ > = | φ >

then || ψ || = || φ ||

- Proof: (better write U in its own representation!)
- 1) U | ψ > = |φ >
- 2) < ψ|U† = <φ|
- (2)x(1):^ Left bracket = Right bracket
- < ψ|U†U|ψ > = < φ|φ >
- < ψ|ψ > = < φ|φ >^ → || ψ || = || φ ||


- C) Product of unitary operators = unitary operator.
- Proof:
- U 1 U 1 † = E
- U 2 U 2 † = E
- Product U 1 U 2 :

### • (U 1 U 2 )(U 1 U 2 ) † = (U 1 U 2 ) (U 2 + U 1 † ) = U 1 U 1 † = E


```
545454
```
Unitary operator U in the matrix form: (UU† = E)

### = (E) =

for rows

**The rows are orthonormal.**

The same is true for the columns.

```
00 01
10 11
```
```
u u
u u
```
```
⎛ ⎞
⎜ ⎟
⎝ ⎠
```
```
00 10
01 11
```
```
u u
u u
```
```
∗ ∗
∗ ∗
```
```
⎛ ⎞
⎜ ⎟
⎝ ⎠
2 2
00 01
2 2
10 11
```
```
00 10 01 11
```
```
1
```
```
1
```
```
0
```
```
u u
```
```
u u
```
```
u u ∗ u u ∗
```
```
⎧ + =
⎪⎪
⎨ + =
⎪
⎪ + =
⎩
```
```
*
kn pn kp
n
```
∑ _u u_ = δ

```
1 0
0 1
```
```
⎛ ⎞
⎜ ⎟
⎝ ⎠
```

Arbitrary Unitary Operator

( )( )

( )( )

```
00 ' 01
```
```
' 10 11
```
```
* *
00 10 01 11
'
```
```
'
```
[( cos ) ( sin )

( sin ) ( cos ) ]

cos sin

sin cos 0

```
i i i
```
```
i i
```
```
i i i i
```
```
i i i i
```
_U e e X e X_

_e X e X_

_u u u u_

_e e e e_

_e e e e_

```
α φ φ
```
```
φ φ
```
```
α φ α φ
```
```
α φ α φ
```
θ θ

θ θ

θ θ

θ θ

```
− −
```
```
− − −
```
```
− − −
```
= + −

+ +

+

=

− =


*Hermitian (Self-Adjoint) Operator

Normal operator with real eigenvalues:

λk* = λk

Properties:

- 1) A = A†^ (It can be used as a definition)

Proof (take its own basis)

- A = ∑kλk | b **k** ><b **k** |
- A† = ∑kλk* | b **k** ><b **k** | = ∑kλk | b **k** ><b **k** | = A


Hermitian Matrix in Arbitrary Basis

```
2
```
```
†
```
```
00 01 00 10
```
```
10 11 01 11
```
* *

* *

*

*

```
( ) , ,
*
```
```
kk kk kk
```
```
kn nk
```
_A A_

_a a a a_

_a a a a_

_a a a real_

_a a_

```
a b
A a c real
b c
```
=

⎛ ⎞ ⎛ ⎞
⎜ ⎟ = ⎜ ⎟
⎝ ⎠ ⎝ ⎠

→ = → −

=

```
⎛ ⎞
= ⎜ ⎟ −
⎝ ⎠
```

```
Sum of Hermitian Operators is a
Hermitian Operator
```
- Proof:
- (A + B) † = A † + B † = A + B


- If A is a Hermitian operator
- Then exp(iA) is a unitary operator
- Proof:
- A = ∑kλk | b **k** >< b **k** |,^ λk are real.
- exp(iA) = ∑k exp(iλk)| b **k** >< b **k** |
- |exp(iλk)| = 1


Summary for Operators

- Outer Product (ket-bra)
- Elementary Hubbard operators |k><n| = Xkn
- Action of an operator on the ket and bra vectors
- Pauli operators σk and identity operator E
- Connection between operators and matrices
- Sum and product of operators^5


```
Summary Continued
```
- Eigenvalues and eigenvectors of operators
- Spectral decomposition of a normal operator
- Adjoint of an operator
- Function of a normal operator
- Unitary and Hermitian operators


Quantum Mechanics of a Qubit


- Niels Bohr:
- Anybody who is not shocked by quantum

theory has not understood it.


Physical State of a Qubit

**norm 1** vector in the 2D Hilbert space

- |ψ > = C 0 |0> + C 1 |1>^

“Vector of state”

Coefficients Ck – “amplitudes”

Sequence (C 0 , C 1 ) – discrete complex function

```
“wave function”)
```
- **Common phase factor exp(iφ)**
- **is not important.**


```
Any Physical Quantity (Observable) “λ”
is Described by a Hermitian Operator
```
- Let the values λk are the possible values of a physical
    quantity (“observable”) λ.
- Let the vectors |bk> are the states which correspond to the
    values λk.
- **The observable λ is described by the Hermitian operator** Λ^
    **= ∑λk|bk><bk|.**
- **If we measure observable λ we say that we do the**
    **measurement in the “measurement basis” |bk>.**


```
Example with the Standard Measurement
Basis
```
- The z-component of the magnetic moment of a
    proton (observable) can take only two values μp and
    (–μp), which correspond to the vectors of state |0>
    and |1>. (μp = 1.41x10-26 J/T)
- Write the Hermitian operator Mz describing the

```
component of the magnetic moment.
```

Solution

- Mz = μp |0><0| + (- μp) |1><1|
- = μp X^00 - μp X^11
- = **μp (X**^00 **- X**^11 **) = μpσz**^.


```
Important Example with the
Standard Measurement Basis:
Measurement of the State
```
- Observable: the “standard state” of a qubit (the
    state in the standard basis). This standard state
    (ss) has two possible values “0” and “1”. The
    corresponding vectors of state are |0> and |1>.
- The Hermitian operator which describes ss is

**SS = 0·X**^00 **+ 1·X**^11 **= X**^11**.**

-^


“Projective Measurement” of a

Quantum State in the Standard Basis

- Standard measurement basis |0>, |1>
- 1) Initially, a qubit is in a state |k>, k = 0,1.
    → non-demolition measurement
- 2) The system is in a superpositional state
    | ψ > = ΣCk|k>, | ψ > → |0>, or |1>
- Probability P 0 =|C 0 |^2 ,^ P 1 =|C 1 |^2
- [Projection (collapse) of the wave function]
- → **“Measurement device” is a probabilistic**
    **projector**


- Example: measurement of state in the measurement basis |vk>
- If initially, a qubit is in a state |vk>, k = 0,1. → non-
    demolition measurement
- If the system is in a superpositional state | ψ > = ΣDk|
    vk >,
- Projection (collapse) of the wave function^
- | ψ > → | v 0 >, or | v 1 >
- Probability Pk =|Dk|^2
- The same is true for the measurement of state in an an arbitrary
    measurement basis |bk>


Example

- Measurement basis |vk>
- | ψ > = |0>
- What is the probability to get the state |v 0 >

```
after the measurement?
```
- Solve the problem transferring to the
    measurement basis |vk>


Solution

- **Transfer to basis |vk>**
- | ψ > = |0> = ΣDk|vk >
- | ψ > = |0> = (½)1/2 (|v 0 > + |v 1 >)
- D 0 = (½)1/2^
- → P 0 = |D 0 |^2 = ½
-^


```
18
```
Convenient formula for the probabilities
One can find probability Pn without transfer to the

new basis.
Example: measurement basis |vk>.

What is the probability to get the state |v 1 > after

the measurement?
| ψ > = Σk Dk|vk>. How to find D 1 without transfer

to basis |vk>?

**<v 1 | ψ>** = <v 1 | Σk Dk|vk> = Σk Dk δk1 = **D 1**

**P 1 = |D 1 |**^2 **= |<v 1 | ψ>|**^2

The same for an arbitrary measurement basis |
bk>: **Pn = |<bn| ψ>|**^2


Example

- Measurement basis |vk>
- | ψ > = |0>
- What is the probability to get the state |v 0 > after the
    measurement?
- Solve without transferring to the measurement basis |
    vk>.
- <v 0 | ψ> = (½)1/2 (<0| + <1|) |0> = (½)1/2^
- P 0 = |<v 0 | ψ>|^2 = ½ (The same answer as before.) 19


Measurement of an Unknown State

- **Measurement of an unknown state of a single**
    **qubit is impossible!**
- | ψ > = C 0 |0> + C 1 |1>,^ C 0 – real, non-negative
- Many (3N) qubits in the same state.
- We split this ensemble into three groups, N qubits
    in every group.


The First Group

- | ψ > = C 0 |0> + C 1 |1>,^ C 0 – real, non-negative
- In the first group we measure the qubit state in
    the standard basis |k>.
- P 0 = N 0 /N = C 02.^ **→ C 0**


The Second Group

- In the second group we measure the qubit
    state in the basis |vk>.
-^


```
23
```
- | ψ > = C 0 |0> + C 1 |1>, C 0 – real, positive
- <v 0 |ψ > = 2-1/2 (<0| + <1|) (C 0 |0> + C 1 |1> )
- = 2-1/2 (C 0 + C 1 )
- P(|v 0 >) = |<v 0 |ψ >|^2
- = (1/2) (C 0 + C 1 ) (C 0 + C 1 )*
- = (1/2) (C 0 + C 1 ) (C 0 + C* 1 )
- = (1/2)(C 02 + C 0 C* 1 + C 1 C 0 + |C 1 |^2 )
- = (1/2){1 + C 0 (C* 1 + C 1 )}
- = (1/2){1 + C 0 ·(2Re(C 1 )} = **½ + C 0 Re(C 1 )**
- P 0 = N 0 /N
- = **½ + C 0 Re(C 1 )**^ **→ Re(C 1 )**


The Third Group

- In the third group we measure the qubit state in
    the basis |wk>.
- Compute <w 0 |ψ >
-^
- P 0 = N 0 /N = **½ + C 0 Im(C 1 )**^
-^ **→ Im(C 1 )**
- Thus, we can measure the unknown state
- | ψ > = C 0 |0> + C 1 |1> (C 0 – real, non-negative)

if we have a large number of qubits in this state.^24


Problem

- Bob has 3000 qubits, all of them are in the same state |ψ> =
    C 0 |0> + C 1 |1>, where C 0 is a real non-negative number. He
    splits the qubits into three groups A,B, and C, 1000 qubits in
    every group. Then he measures the state of the qubits of
    group A in the standard measurement basis |k>. He finds
    that after the measurement 250 qubits are in the state |0>.
- Find the value of C 0.


Solution

### • P 0 = C 02 = N 0 /N = 250/1000 = ¼.

### • C 0 = (1/4)1/2 = ½.


- Problem.
- In the previous Problem, after the measurement in
    group A, Bob measures the state of the qubits in group
    B in the measurement basis |vk>. He claims that after
    the measurement 750 qubits are in the state |v 0 >. Then
    he measures the state of the qubits of group C in the
    measurement basis |wk> and claims that after the
    measurement 750 qubits are in the state |w 0 >. Compute
    the norm and show that the Bob’s claim is wrong.
- Hint: C 0 = ½;^ In basis |vk>: P 0 = ½ + C 0 Re(C 1 )
-^ In basis |wk>: P 0 = ½ + C 0 Im(C 1 )


Solution

- C 0 = ½
- In basis |vk>): P 0 = ½ + C 0 Re(C 1 )

= ½[1 + Re(C 1 )] = 0.750 = ¾

- In basis |wk>): P 0 = ½ + C 0 Im(C 1 )

= ½[1 + Im(C 1 )] = 0.750 = 3/4

- P(|w 0 >) = ½ + C 0 Im(C 1 ) = ½[1 + Im(C 1 )] = 3/4
- Re(C 1 ) = Im(C 1 ) = ½
- **|ψ> = (½)|0> + (½ +½ i)|1>**
- **(Norm)**^2 **= ¾ - error!**^28


*Problems with Operators

- Find the eigenvalues of the operator **A = exp(iσx)**^

```
in the standard form (λ = a + i·b) in decimals with
3 significant figures.
```
- Hint:
- σx = |v 0 > <v 0 | - |v 1 > <v 1 |
- The eigenvalues are “1” and “-1”.
-^


Solution

- σx = |v 0 > <v 0 | - |v 1 > <v 1 |
- A = exp(iσx)
- = exp{i·1}|v 0 > <v 0 | + exp{i·(-1)}|v 1 > <v 1 |
- λ 0 = exp{i·1} = cos(1) + i·sin(1) = **0.540 + i·0.841**
- λ 1 = exp{-i·1} = cos(1) - i·sin(1)
- = cos(1) - i·sin(1) = **0.540 - i·0.841**


Problem

- Write the Pauli operator

σx = |v 0 ><v 0 | - |v 1 ><v 1 |

in the standard basis in terms of Xkn.

Hint:

|v0,1>= 2-1/2 (|0> ± |1>)


Solution

- A = |v 0 ><v 0 | - |v 1 ><v 1 |

= 2-1/2 (|0> + |1>) 2-1/2 (<0| + <1|)

- 2-1/2 (|0> - |1>) 2-1/2 (<0| - <1|)
- = |0><1| + |1><0|

= **X**^01 **+ X**^10


Problem

- Write operator X^00 = |0><0| in basis |
    vk> in the matrix form.
- Notation (X^00 )|v>
- Hints:
- |0> = 2-1/2 {|v 0 > + |v 1 >}
- Use the distributive property of the
    outer product


Solution

- X^00 = |0><0|
-^
- = 2-1/2 (|v 0 > + |v 1 >) 2-1/2 (<v 0 | + <v 1 |)
- = (1/2) (|v 0 ><v 0 | + |v 0 ><v 1 | + |v 1 ><v 0 | +|

v 1 ><v 1 |)

```
34
```
( )

```
00
|
```
```
1 1 1
v 2 1 1
```
```
X
>
```
```
⎛ ⎞
→ ⎜ ⎟
⎝ ⎠
```

Summary of Lecture 4

- Physical state of a qubit
- A physical quantity “observable” and
    corresponding Hermitian operator
- Measurement basis
- Measurement of the state
- Non-demolition measurement and projective
    measurement
- Formula for the probability: Pn = |<bn| ψ>|^2
- Measurement of an unknown state with many
    qubits in that state.


Hamiltonian of a Qubit

- Let state |k> of a qubit corresponds to energy Ek (k =

```
0,1).
```
- Hermitian energy operator – “Hamiltonian” H:
- H = E 0 |0><0| + E 1 |1><1|,^

It describes the energy of the two-level qubit.

- E 0 and E 1 are the eigenvalues of the Hamiltonian
- |0> and |1> are the eigenvectors of the Hamiltonian


Generalization

- Let state |b **0** > corresponds to energy E 0 and

```
state |b 1 > corresponds to energy E 1.
```
- Then the Hamiltonian:

H = E 0 |b **0** >< b **0** | + E 1 |b **1** >< b **1** |

describes the energy of the two-level qubit.


```
Deterministic (Unitary) Evolution of a
Quantum System
```
- A quantum system experiences external electric or
    magnetic fields with no measurement and no interaction
    to the environment: deterministic evolution of the vector
    of state.

The **Schrodinger equation** :

iħ (d/dt)|ψ(t) > = H|ψ(t) >

- Solution can be written in the form:
- |ψ(t) > = U(t)|ψ(0)>
- U – evolution operator (propagator)
- (Unitary evolution)^4


Evolution Operator

- Statement: if Hamiltonian does not depend on time then **U(t) = exp(-iHt/ħ)**
- It is a unitary operator → it does not change the norm of the vector.
- Deterministic evolution – unitary evolution.
- Proof:
- Let, for simplicity, state |k> corresponds to energy Ek (k = 0,1)


- We should prove that
- |ψ(t) > = {exp(-iHt/ħ)} |ψ(0)>

is the solution of the Schrodinger equation, i.e.

iħ (d/dt) |ψ(t) > = H |ψ(t) >

- {The initial condition is satisfied: when t = 0

|ψ(t) > = |ψ(0)>}

- First, write exp(-iHt/ħ) in terms of Hubbard operators: (H
    = E 0 X^00 + E 1 X^11 )

exp(-iHt/ħ)

= exp{-iE 0 t/ħ}X^00 + exp{-iE 1 t/ħ}X^11

= **exp(-iω 0 t)X**^00 **+ exp(-iω 1 t)X**^11 **,**

E 0 /ħ = ω 0 , E 1 /ħ = ω 1


Proof

- Left side of equation iħ (d/dt) |ψ(t) > = H |ψ(t) >:
- iħ (d/dt) {exp(-iHt/ħ)}|ψ(0) >
- = iħ (d/dt){exp(-iω 0 t)X^00 + exp(-iω 1 t)X^11 )}|ψ(0) >
- = {iħ (-iω 0 ) exp(-iω 0 t) X^00

+ iħ (-iω 1 ) exp(-iω 1 t) X^11 }^ |ψ(0) >

- = {ħω 0 exp(-iω 0 t) X^00 + ħω 1 exp(-iω 1 t) X^11 }^ |ψ(0) >


Continue

- Left side:
- **{ħω 0 exp(-iω 0 t) X**^00 **+ ħω 1 exp(-iω 1 t) X**^11 **}**^ **|ψ(0) >**
- Right side of equation:
- H|ψ(t) > = H {exp(-iHt/ħ)}|ψ(0)>

= (E 0 X^00 + E 1 X^11 ) {exp(-iω 0 t)X^00 + exp(-iω 1 t)X^11 )} |ψ(0)>

= **{E 0 exp(-iω 0 t)X**^00 **+ E 1 exp(-iω 1 t)X**^11 **}|ψ(0)>**

E 0 = ħω 0 , E 1 = ħω 1

The same!^8


Stationary States

Eigenvectors of the Hamiltonian describe the
stationary states.
Prove. Let |0> and |1> are the eigenvectors of H:
H = E 0 X^00 + E 1 X^11
Let |ψ(0)> = |0>, then
|ψ(t) > = U(t)|ψ(0)> = U(t)|0> = {exp(-iHt/ħ)}|0>
= {exp(-iω 0 t)X^00 + exp(-iω 1 t)X^11 )}|0>
= exp(-iω 0 t) |0> → |0>
The same is true for |1>:
|ψ(t) > = exp(-iω 1 t) |1> → |1>
**|0> and|1> are the stationary states.**

(^)


Non-stationary states:

|ψ(0)> = C 0 |0> + C 1 |1>

C 0 is a real positive number.

|ψ(t)> = U(t)|ψ(0)>

= {exp(-iω 0 t)X^00 + exp(-iω 1 t)X^11 }(C 0 |0> + C 1 |1>)

= C 0 exp(-iω 0 t)|0> + C 1 exp(-iω 1 t)|1>

→ C 0 |0> + C 1 exp(-iωt)|1>

ω = ω 1 – ω 0 = (E 1 – E 0 )/ ħ – **transition frequency**

**ħω = E 1 – E 0** (Assume E 1 > E 0 ,

then ω is positive, and |0> is the ground state.^10


Precession of the Bloch Vector

|ψ(t)> = C 0 |0> + C 1 exp(-iωt)|1>

Vector of state in the Bloch form:

|ψ(0)> = cos(θ 0 /2)|0> + sin(θ 0 /2)exp(iφ 0 )|1>

|ψ(t)> = cos(θ 0 /2)|0> + sin(θ 0 /2)exp[i(φ 0 - ωt)]|1>

- The Bloch vector precesses clockwise about the positive
z-direction: **Larmor precession**.
- The positive z-direction is the direction of the Bloch
vector for the ground state |0>.


Larmor Precession of the Bloch Vector

_z_

```
b
```
```
52
```

General Case

- Energies E 0 and E 1.
- |b **0** > (the ground state, the corresponding Bloch vector **b 0** ) and |
b **1** > (excited state, the corresponding Bloch vector **b 1** opposite to **b 0**.
- H = E 0 |b **0** >< b **0** | + E 1 |b **1** >< b **1** |
- Evolution operator:
U(t) = exp(-iHt/ħ) =
exp{-iE 0 t/ħ}|b **0** >< b **0** | + exp{-iE 1 t/ħ} |b 1 >< b 1 |)

= exp(-iω 0 t) |b **0** >< b **0** | + exp(-iω 1 t) |b 1 >< b 1 |


Solution in General Case

If the initial state is a superpositional state

|ψ(0)> = D 0 |b 0 > + D 1 |b 1 >,

|ψ(t)> = U(t)|ψ(0)>

= {exp(-iω 0 t) |b **0** >< b **0** | + exp(-iω 1 t) |b 1 >< b 1 |}

{D 0 |b 0 > + D 1 |b 1 >}

= D 0 exp(-iω 0 t) |b **0** > + D 1 exp(-iω 1 t) |b **1** >

→D 0 |b 0 > + D 1 exp(-iωt)|b 1 >

Precession of the Bloch vector:

The corresponding Bloch vector rotates clockwise around
the Bloch vector of the ground state **b 0.** 14


```
Summary: Quantum Measurement and
the Unitary Evolution
```
- **Two ways for manipulating a quantum system**.
- 1. Probabilistic:

quantum (projective) measurement.

- 2. Deterministic:
    application of an external field causes clockwise
    precession of the Bloch vector about the Bloch
    vector of the ground state **b 0**. 15


Problem

- Let |0> and |1> are the eigenvectors of the
    Hamiltonian.
- Let the initial vector of state of a qubit is
- |ψ(0)> = cos(3/2)|0> + sin(3/2)|1>.
- If the transition frequency of the qubit ω^ = 2 x10^12
    rad/s find the vector of state |ψ(t)> at t = 1 ps. Write
    the answer in the Bloch form (0 ≤ φ < 2π)
-^


Answer

- |ψ(0)> = cos(3/2)|0> + sin(3/2)exp(i·4.28)|1>.


Problem

- The ground state of a qubit is |v 0 >, and the excited

```
state is |v 1 >. If the initial state of the qubit is |ψ(0)>
= |0>, and its transition frequency ω = πx10^12 rad/s,
what is the state of the qubit at time t = 1 ps in the
basis |vk>?
```

Solution

- |ψ(0)> = |0> = 2-1/2(|v 0 > + |v 1 >)
- |ψ(t)> = 2-1/2{|v 0 > + |v 1 >exp(-iωt)}
- |ψ(tf)> = 2-1/2{|v 0 > + |v 1 >exp(-iωtf)}
- = 2-1/2{|v 0 > + |v 1 >exp(-iπ)}
-^ **= 2-1/2(|v 0 > - |v 1 >}**


Problem

- The qubit energy can take two values: E 0 = -T and

```
E 1 = T.
```
- The corresponding vectors of state are:
- |v 0 > and |v 1 >.
- Write the Hamiltonian of the qubit in terms of “T”
    and Pauli operators.


Solution

- H = -T|v **0** >< v **0** | + T|v **1** >< v **1** |
- = -T(|v 0 >< v 0 | - |v 1 >< v 1 |)
- = - Tσx^


Problem

- A qubit state |k> corresponds to the energy Ek :
- → H = E 0 |0><0| + E 1 |1><1|= E 0 X^00 +E 1 X^11
- The possible values of energy:
- E 0 = 0, E 1 = 1 eV.
- The vector of state of a qubit in the standard basis
- | ψ > = (1/3)1/2|0> + (2/3)1/2|1>
- Find the mean energy by direct computation: < E > =
    ∑kEkP(Ek). Write the answer in the form of a fraction.


Solution

- | ψ > = (1/3)1/2|0> + (2/3)1/2|1>
- <E> = ∑Ek |Ck|^2
- = (1/3)E 0 + (2/3)E 1 (E 0 = 0, E 1 = 1 eV)
- = **(2/3) eV**


Problem

- Let the Hamiltonian of a qubit H = Eσx. Write the

```
spectral decomposition of the evolution operator
U(t) = exp(-iHt/ħ).
```

Spin and Internal Magnetic

Moment of an Electron

```
The Simplest Qubit
```

Summary of Lecture 5

- Deterministic (unitary) evolution of a quantum system.

The Schrodinger equation:

iħ (d/dt)|ψ(t) > = H|ψ(t) >

Evolution operator U(t):

|ψ(t) > = U(t)|ψ(0)>, U(t) = exp(-iHt/ħ)

If the standard basis is the energy basis,

i.e. state |k> corresponds to energy Ek (k = 0,1),

then |0> and |1> are the stationary state.

(We assume E 0 < E 1 .)


Summary of Lecture 5 (Continued)

- If |ψ(0)> = C 0 |0> + C 1 |1>,^ C 0 – real positive

then |ψ(t)> = C 0 |0> + C 1 exp(-iωt)|1>

ω = (E 1 – E 0 )/ ħ

(Larmor precession of the Bloch vector about the z-

axis)

- In general, if the energy basis is |b **k** >

and |ψ(0)> = C 0 |b **0** > + C 1 |b **1** >,

then |ψ(t)> = C 0 |b **0** > + C 1 exp(-iωt) |b **1** >

(Larmor precession about the Bloch vector **b** 0 .) 3


Angular Momentum in Classical Physics

- **L** = (mr^2 )ω **k**^ (unit J·s)^

### •^

```
z
```

```
Magnetic Moment in Classical Physics:
Electromagnet and Bar Magnet
```
- Electromagnet: **μ** = N·I·A · **k** (unit A·m^2 or J/T)
- Permanent magnet: **μ** = μaNa **k**

```
z
```

```
6
```
```
Internal Angular Momentum (Spin) and
Magnetic Moment of Electron
```
- Spin S = ħ/2,^ ħ = 1.05x10-34 J·s^
- Spin magnetic moment μ = μB (Bohr magneton)
- μB = (e/me)S = 9.28x10-24 J/T
- Electron gyromagnetic ratio:
- γ = μB / S = e/me = 1.76x10^11 rad/(s·T)
- Direction of spin magnetic moment is opposite to the
    direction of the spin.


Gyromagnetic Effect, Na iron atoms,

4 unpaired electrons in every atom:

Sa =2ħ, μa = 4μB. After applying **B 0** :

Total: μ = μaN, S = SaN. γ = μ/S = e/me.

```
L = SaN,
CCW
rotation
```

Interaction Between the Magnets


```
99
```
```
Stern-Gerlach Experiment (1922):
Spin Component is Quantized
Z
```
B

```
μ
```
```
N
```
```
S
S
```
```
Screen
μ z =−μ B
```
```
N μ z =μ B
```
```
N
S
atom
```
```
μ
```
Silver (Ag): 5s^1 (unpolarized spins)



```
The Z-Component of Magnetic Moment
and Spin
```
- μz = ± μB^
- →^ Sz = - (ħ/2)⋅sgn(μz)


```
The Future “Measurement” of the z-
component of Atomic Magnetic Moment
```
z


Spin Components

- Polarized atoms:

spins point in the positive z-direction: Sz = ħ/2.

- Sx = ±ħ/2^ (probability ½)
- Sy = ±ħ/2^ (probability ½)
- S **n** = ±ħ/2^ (probability cos^2 (θ/2)

θ is the polar angle of the unit vector **n**.

→ Spin can be described by a vector of state.^13


“Direction” of Spin

- Spin points in the positive z-direction:
- Probability to get Sz = ħ/2:

P(Sz = ħ/2) = 1

- Spin points in the direction of unit vector **n** :
- Probability to get S **n** = ħ/2
- P(S **n** = ħ/2) = 1
- Guess: Direction of spin is the direction of the Bloch
    vector.^14


Mathematical Description of the Spin

- Spin points “up”, i.e. in the positive z-direction:
- vector of state |0>.
- Spin points in the positive x-direction:
- vector of state |v 0 >.
- Spin points in the positive y-direction:
- vector of state |w 0 >.


Opposite Spin Direction

- State |1>:
- spin points “down” in the negative z-direction (S **z** =

```
-ħ/2)
```
- State |v 1 >:

spin points in the negative x-direction (S **x** = -ħ/2)

- State |w 1 >:

spin points in the negative y-direction (S **y** = -ħ/2)


```
An Observable and
a Measurement Basis
```
- Measurement of the z-component of spin is
    the measurement in the standard basis
- Measurement of the x-component of spin is
    the measurement in the basis |vk>
- Measurement of the y-component of spin is
    the measurement in the basis |wk>


Direction of a Spin in General

- Let a large number of polarized spins point in the direction
    of the unit vector **n** with the spherical coordinates θ and φ.
- We can split atoms in 3 groups and measure the x, y, and z-
    components of the spin (standard, |v>, and |w>
    measurement bases)
- The result of the measurement of the spin state:
- |ψ> = cos(θ/2)|0> + sin(θ/2)exp(iφ)|1>
-^
- →^ **the Bloch vector of the spin state points in the**
    **direction of the spin.**


```
Spin 1/2 is an Ideal Qubit.
Possible Implementations:
```
- 1) An atom or ion with a single valence
    electron in the S-state

(orbital angular momentum is zero).

- 2) A single electron confined in a quantum dot
    in a semiconductor.
- 3) A single electron in an electron trap
- 4) Nuclear spin ½ (proton, neutron,^31 P,^57 Fe).


Spin and Magnetic Moment Operators

- Operator describing the spin z-component
- Operator describing the z-component of magnetic
    moment:

(^)
| 0 0 | | 1 1 |
2 2 2 _z_
>< − >< = σ
!!!
−μ _B_ σ _z_


Operators Describing the x- and y-

Components of the Spin

```
2
```
```
2
```
```
x
```
```
y
```
```
σ
```
```
σ
```
```
!
```
```
!
```
```
The x- and y-components
of the magnetic moment
B x
B y
```
```
μ σ
μ σ
```
```
−
−
```

```
Operator of Spin Component along
a Unit Vector n (θ,φ)
```
- Two possible values of the spin component along the
direction **n** (θ,φ): ± ħ/2
- Corresponding vectors of state:
- |b **0** > = cos(θ/2)|0> + sin(θ/2) exp(iφ)|1>
- |b **1** > = cos[(π-θ)/2]|0>

+ sin[(π-θ)/2] exp[i(φ±π)]|1>

-^


Spin Operators

- (ħ/2)|b **0** > <b **0** | - (ħ/2)|b **1** ><b **1** |

= (ħ/2) σ **n** = (ħ/2) **n•σ**

**n•σ =** nxσx + nyσy + nzσz

nx = sinθcosφ, ny = sinθsinφ, nz = cos θ


- Operator of the component of the magnetic

moment along the unit vector **n** :

- **-** μB σ **n** = **-** μB **n•σ**
- nx = sinθcosφ, ny = sinθsinφ, nz = cos θ


Deterministic Evolution of Spin

- Spin in the Magnetic Field


Spin Energy
Two stationary states: spin points opposite to the

magnetic field **B** and spin points in the direction of **B**.

Example: silver atoms. Splitting of an energy level in a

magnetic field (Zeeman splitting): E = ±μBB.

(Electron spin resonance.)


```
0 " "
1 " "
```
```
spin up
spin down
```
```
−
−
```
```
Bz = − B
```
**B**

```
z
```
```
E
```
_spin_

1 ↓

0 ↑


Frequency of Transition

```
0
1
```
```
11
```
```
10
```
```
2 /
1 T
1. 76 10 rad/s
```
```
3 10 Hz
2
```
```
B
B
B
```
```
E B
E B
B B
B
```
```
f
```
```
μ
μ
ω μ γ
```
```
ω
ω
π
```
```
= −
=
= =
=
≈ ×
```
```
= ≈ ×
```
```
!
```
```
B
```

```
/ 2 / 2
```
0 0 1 1

```
1
2
( ) exp( / ) exp( / 2 )
```
0 0 1 1

```
B B
```
```
B z z
```
```
z
i t i t
```
_H B B_

_H B_

_U U t iHt i t_

_U e_ ω _e_ ω

μ μ

μ σ ωσ

```
ω σ
−
```
= − +

= − = −

= = − =

= +

!

!

Hamiltonian and Evolution Operator

```
Magnetic field points in the
negative z-direction: STOP
```

```
0
```
```
/ 2 / 2
```
```
/ 2 00 / 2 11
```
```
0 0
```
0 0 1 1

```
( 0 ) cos 0 sin 1
2 2
( ) ( 0 )
```
```
i t i t
```
```
i t i t
```
```
i
```
_U e e_

_e X e X_

_e_

_t U_

```
ω ω
```
```
ω ω
```
ψ θ θ φ

ψ ψ

```
−
```
```
−
```
= +

= +

= +

=


```
0
```
```
0
```
```
0
```
/ 2 00 / (^21100)
/ 2 0 / (^20)
0 0 ( )
( ) cos 0 sin | 1
2 2
cos 0 sin | 1
2 2
cos 0 sin | 1
2 2
_i t i t i
i t i t i
i t
t e X e X e
e e e
e_
ω ω φ
ω ω φ
φ ω
θ θ
ψ
θ θ
θ θ
−
−
−
⎡ ⎤
= ⎡⎣ + ⎤⎦⎢ + >⎥
⎣ ⎦
= + >
→ + >
**Counter-clockwise
precession of the spin
about the magnetic field.**


Larmor Precession of the Bloch Vector

**B**

```
b
```

```
Physical Manipulations with the
Electron Spin
```
- Magnetic pulse in the positive z-direction:
- Spin rotates counterclockwise about the positive z-
    direction by angle
- α =ωτ
- ω = 2μBB/ħ = γB

```
Bz
```
```
B
```
```
o τ t
```

How to Change the Spin State?

- **A)** |ψ> → |0> (move spin to the (+z) direction)
- Reduce azimuthal and polar angles (φ 0 and θ 0 ) to

```
zero
```
- Magnetic field pulses:
- 1) (-z) direction, τ 1 = φ 0 /ω
- moves spin to the x-z plane,
- 2) (-y) direction, τ 2 = θ 0 /ω
- moves spin
- to the (+z) direction.
    x 34

```
y
```
```
z
```
```
φ 0
```
```
θ 0
```

Continued. Change of the Spin State.

- **B)** |0> → |ψ > = cos(θ/2)|0> + sin(θ/2)exp(iφ)|1>
- Increase polar and azimuthal angles to θ and φ.
- Pulses:
- 1) (+y), τ 1 = θ/ω
- 2) (+z), τ 2 = φ/ω

```
x^35
```
```
y
```
```
z
```
```
φ
```
```
θ
```

Conclusion

- Using magnetic field pulses one can transform
    any initial spin state |ψ 0 > to any other state |
    ψ 1 >.
- A trivial (but not the only) way to do it is to
    move the spin from the state |ψ 0 > to the state
    |0> and then from the state |0> to the state |
    ψ 1 >.


Summary of Lecture 6.

- Spin and magnetic moment of an electron.
- S = ħ/2,^ ħ = 1.05x10-34 J·s^
- Magnetic moment μ = μB (Bohr magneton)
- μB = 9.28x10-24 J/T
- Electron gyromagnetic ratio:
- γ = μB / S = 1.76x10^11 rad/(s·T)


Summary Continued

- “Direction of spin” (θ, φ)
- Direction of spin = direction of the Bloch vector.
- Measurement of the spin components.
- Deterministic evolution of spin in the magnetic field:
- Counterclockwise precession about the magnetic
    field.
- Manipulation with the spin direction using the
    magnetic field pulses.


Single-Qubit Rotational Gates

```
General Formalism for an Arbitrary
Qubit
```

- Definition:
- Unitary operator **exp(-iασz/2 )**

is called a rotational gate **Rz(α)**

For any qubit it rotates the Bloch vector by angle α

counterclockwise about the +z-direction

(Formal proof is on the next page.)


Formal Proof

- Rz(α) = exp(-iασz/2 )
- = exp(-iα/2 )X^00 + exp(iα/2 )X^11
- Rz(α)|ψ 0 > = [exp(-iα/2 )X^00 + exp(iα/2 )X^11 ]

[cos(θ 0 /2)|0> + sin(θ 0 /2)exp(iφ 0 )|1>

= cos(θ 0 /2)exp(-iα/2 ) |0>

+ sin(θ 0 /2)exp(iφ 0 ) exp(iα/2 )|1> [·exp(iα/2 )]

→ cos(θ 0 /2)|0> + sin(θ 0 /2)exp[i(φ 0 + α)]|1>


```
6
```
General Rotational Gate

```
6
```
_Rn_ (α) = exp{− _i_ ασ **_n_** / (^2) }, σ **_n_** = ( **_n_** • σ)
Rn (α) rotates the Bloch vector by angle α,
counter-clockwise about unit vector **n**.
Proof:
θ' and φ’ – polar and azimuthal angles with respect
to unit vector **n**
|ψ>=cos(θ’/2)|b **0** > + sin(θ’/2)exp[i(φ’)]|b 1 >
|b 0 > and |b 1 > are the eigenvectors of σn :
Bloch vectors point in the directions **n** and (– **n** ).


Proof Continued

Rn(α) = exp(-iα/2) |b **0** ><b **0** | + exp(iα/2) |b **1** ><b **1** |

- Rn(α)|ψ>

= [exp(-iα/2) |b **0** ><b **0** | + exp(iα/2) |b **1** ><b **1 ]**

[cos(θ’/2)|b **0** > + sin(θ’/2)exp(iφ’)]|b 1 >]

= [cos(θ’/2)exp(-iα/2) |b **0** >

+ sin(θ’/2) exp(iφ’) exp(iα/2) |b 1 >] [· exp(iα/2)]

- → cos(θ’/2)|b **0** > + sin(θ’/2)exp[i(φ’ + α)]|b 1 >^7

_Rn_ (α) = exp{− _i_ ασ **_n_** / (^2) }, σ **_n_** = ( **_n_** • σ)


Special Cases

- CCW rotation of the Bloch vector by angle
    α about +x- and +y-axes:

( )

( 1 , 0 , 0 )

( ) exp( / 2 )

( 0 , 1 , 0 )

( ) exp( / 2 )

```
x
```
```
x x
```
```
y
```
```
y y
```
_R i_

_R i_

σ

σ σ

α ασ

σ σ

α ασ

= •

= → =

= −

= → =

= −

```
n
```
```
n
```
```
n
```
**_n_**

**_n_**

**_n_**

σ


Example

- Write the rotational gate Rz(α) in the standard

```
basis in the matrix form.
```
- Rz(α) = exp(-iασz/2 )


Solution

```
/ 2
```
```
/ 2 00 / 2 11
```
```
/ 2
```
```
/ 2
```
( )

0

0

```
i z
z
i i
```
```
i
```
```
i
```
_R e_

_e X e X_

_e_

_e_

```
ασ
```
```
α α
```
```
α
```
```
α
```
α

```
−
```
```
−
```
```
−
```
=

= +

⎛ ⎞
→ ⎜ ⎟

⎝ ⎠


Example

- Write the rotational gate Ry(α) in the standard

```
basis
```
- A) in terms of the cos(α/2), sin(α/2), and the
    Hubbard operators,
- B) the same in the matrix form


Solution

( )

( ) ( )

( ) ( )

```
0 0 1 1
00 11 01 10
```
( ) exp / 2

exp / 2 | | exp / 2 | |

```
cos sin
2 2
```
```
cos sin
2 2
```
```
sin cos
2 2
```
_Ry i y_

_i w w i w w_

_X X X X_

α ασ

```
α α
α α
```
α α

α α

= −

= − >< + ><

= + + − +

⎛ ⎞
⎜ − ⎟
→ ⎜ ⎟
⎜ ⎟
⎜ ⎟
⎝ ⎠


Theorem:

Any One-Qubit Gate can be

Decomposed into One-Qubit

Rotations _Ry_ and _Rz_ with accuracy

to a phase factor.


```
14
```
```
Decomposition of a One-Qubit Gates into
Rotational Gates
```
```
00 ' 01
```
```
' 10 11
```
Any one-qubit gate can be represented in the form:

[( cos ) ( sin )

( sin ) ( cos ) ]

( ') ( 2 ) ( ')

```
i i i
```
```
i i
```
```
i
z y z
```
_e e X e X_

_e X e X_

_e R R R_

```
δ φ φ
```
```
φ φ
```
```
δ
```
θ θ

θ θ

φ φ θ φ φ

− + − −

+ +

= + −

( ) ( )

```
/ 2 00 / 2 11
```
```
00 11 01 10
```
( )

```
( ) cos sin
2 2
Next page - proof for | 0 >
```
```
i i
z
```
```
y
```
_R e X e X_

_R X X X X_

```
α α α
α α
α
```
= − +

= + + − +


```
15
```
( )

```
00 ' 01
' 10 11
'
```
```
( ')/ 2
( ')/ 2
```
```
[( cos ) ( sin )
( sin ) ( cos ) ]| 0
cos | 0 sin | 1
```
```
( ') ( 2 ) ( ')| 0
( ') ( 2 ) | 0
( ') cos | 0 sin | 1
```
```
i i i
i i
i i i
```
```
i
z y z
i i
z y
i i
z
```
_e e X e X_

```
e X e X
e e e
```
_e R R R_

```
e R R e
e e R
```
```
δ φ φ
φ φ
δ φ φ
```
```
δ
δ φ φ
δ φ φ
```
```
θ θ
θ θ
θ θ
```
```
φ φ θ φ φ
φ φ θ
φ φ θ θ
```
```
− −
```
```
−
```
```
− −
− −
```
```
+ −
+ + >
```
= ⎡⎣ > + >⎤⎦

```
+ − >
```
= + >

= + > + >

( )

( ) ( )

```
( ')/ 2 ( ')/ 2 ( ')/ 2
'
/ 2 00 / 2 11
```
```
00 11 01 10
```
```
cos | 0 sin | 1
cos | 0 sin | 1 the same!
( )
```
```
( ) cos sin
```
```
i i i i
i i i
i i
z
```
```
y
```
```
e e e e
e e e
R e X e X
```
```
R X X X X
```
```
δ φ φ φ φ φ φ
δ φ φ
α α
```
```
θ θ
θ θ
α
```
```
α α α
```
```
− − − + +
−
−
```
= > + >

= ⎡⎣ > + >⎤⎦ −

```
= +
```
```
= + + − +
```

Example: Hadamard Gate (HG)

### • HG|0> = 2-1/2(|0> + |1>)^

### • HG|1> = 2-1/2(|0> - |1>)

### • HG = 2-1/2(X^00 + X^01 + X^10 – X^11 )

-^ {θ between zero and π/2,^
    δ, φ and φ’ as close to zero as possible,

positive or negative}

```
00 ' 01
' 10 11
```
```
[( cos ) ( sin )
( sin ) ( cos ) ]
( ') ( 2 ) ( ')
```
```
i i i
i i
i
z y z
```
```
U e e X e X
e X e X
e R R R
```
```
δ φ φ
φ φ
δ
```
```
θ θ
θ θ
φ φ θ φ φ
```
```
= − + − −
+ +
= + −
```

Solution

- θ = π/4
- δ – φ = 0
- (δ + π – φ’ = 0)
- δ + φ’ = 0
- δ + φ = π,^

δ = π/2

φ = π/2

φ‘ = -π/2

- **HG = exp(iπ/2) Ry(π/2) Rz(π)**^17

```
00 ' 01
' 10 11
```
```
[( cos ) ( sin )
( sin ) ( cos ) ]
( ') ( 2 ) ( ')
```
```
i i i
i i
i
z y z
```
```
U e e X e X
e X e X
e R R R
```
```
δ φ φ
φ φ
δ
```
```
θ θ
θ θ
φ φ θ φ φ
```
```
= − + − −
+ +
= + −
```
```
HG = 2-1/2(X^00 + X^01 + X^10 – X^11 )
```
```
U = ei δ Rz (φ +φ') Ry ( 2 θ) Rz (φ −φ')
```

Verification

- We can verify that
- exp(iπ/2) Ry(π/2) Rz(π)
- = 2-1/2(X^00 + X^01 + X^10 – X^11 )

( ) ( )

```
/ 2 00 / 2 11
```
```
00 11 01 10
```
```
( )
```
```
( ) cos sin
2 2
/ 2
```
```
i i
z
```
```
y
```
```
R e X e X
```
```
R X X X X
```
```
α α α
α π
α α
α
```
```
α π
```
```
= − +
=
```
```
= + + − +
```
```
=
```

Verification Continued

- exp(iπ/2) Ry(π/2) Rz(π)
- = i·^2 -1/2(X^00 + X^11 - X^01 + X^10 )(-iX^00 + i X^11 )

### • = 2-1/2(X^00 + X^11 - X^01 + X^10 )(X^00 - X^11 )

### • = 2-1/2(X^00 - X^11 + X^01 + X^10 )


Quantum Circuit Diagram (QCD):

Example

```
ψ → ( )
z 4
R π ( )
y 6
R π ( )
z 8
R π ψ '
```
```
( ) ( ) ( ) '
z 8 y 6 z 4
G R R R
```
```
π π π
ψ = ψ = ψ
```
```
→
```

Two Qubits – 4D Hilbert Space

```
0 0 00
0 1 01
1 0 10
1 1 11
```
```
k ⊗ n = kn
⊗ =
⊗ =
⊗ =
⊗ =
```
- Standard basis:
- Basis states -
tensor product


Matrix form of the Tensor Product.

Example.

| 0 | 1 | 01

0

1 0 1

0 1 0

0

> ⊗ >= >

```
⎛ ⎞
⎜ ⎟
⎛ ⎞ ⎛ ⎞ ⎜ ⎟
⎜ ⎟ ⊗⎜ ⎟ =
⎝ ⎠ ⎝ ⎠ ⎜ ⎟
⎜ ⎟
⎝ ⎠
```

- Bra vector, matrix form

( ) ( ) ( )

0 | 1 | 01 |

1 0 0 1 0 1 0 0

< ⊗ < =<

⊗ =


```
24
```
- Tensor product of single qubit states
- (a|0> + b|1>)(a’|0> + b’|1>)
- = aa’|00> + ab’|01> + ba’|10> + bb’|11>
- Tensor product of matrices:

```
Tensor Product of Superpositional
States
```
'

' '

```
' '
'
```
_aa_

_a a ab_

```
b b ba
bb
```
```
⎛ ⎞
⎜ ⎟
⎛ ⎞ ⎛ ⎞ ⎜ ⎟
⎜ ⎟ ⊗⎜ ⎟ =
⎝ ⎠ ⎝ ⎠ ⎜ ⎟
⎜ ⎟
⎝ ⎠
```

- **Entangled states.**^^
- Example:
- Bell state
- |B 0 > = 2-1/2(|00> + |11>)^
- No decomposition into the tensor product!


Inner product in 4-D Hilbert Space

- <kn|pq> = δkpδnq
- Non-standard single-qubit basis
- Example: basis |vk vn>
- <vkvn|vpvq> = δkpδnq


```
Entangled Basis, e.g. the Bell Basis
(STOP)
```
- |B 0 > = 2-1/2(|00> + |11>)

### • |B 1 > = 2-1/2(|00> - |11>)

### • |B 2 > = 2-1/2(|01> + |10>)

### • |B 3 > = 2-1/2(|01> - |10>)


Operators in a Two Qubit Hilbert

Space


Operators in 2-Qubit Hilbert Space

- Standard basis |kn>
- Outer product (ket-bra)
- 16 elementary operators |kn><pq|
- Action of a elementary operator on a basis
    state:
- |kn><pq|rs> = δprδqs |kn>


Decimal Notation

- |00> → |0>
- |01> → |1>
- |10> → |2>
- |11> → |3>
-^
- Superpositional state: ∑Ck |k>
- (k from 0 to 3).
- 16 Hubbard operators Xkn = |k><n|
- (k,n from 0 to 3).

Arbitrary operator: A = ∑aknXkn


```
Vector of State in Decimal Notation in the
Matrix Form
```
```
4
```
```
0
```
(^31)
(^02)
3

### 1 0 0 0

### 0 1 0 0

### | 0 | 1 > | 2 > | 3 >

### 0 0 1 0

### 0 0 0 1

| >= _k_ |
_k_

### C

### C

```
C k
C
C
```
```
ψ
=
```
### ⎛ ⎞ ⎛ ⎞ ⎛ ⎞ ⎛ ⎞

### ⎜ ⎟ ⎜ ⎟ ⎜ ⎟ ⎜ ⎟

### >→⎜ ⎟ →⎜ ⎟ → ⎜ ⎟ → ⎜ ⎟

### ⎜ ⎟ ⎜ ⎟ ⎜ ⎟ ⎜ ⎟

### ⎜ ⎟ ⎜ ⎟ ⎜ ⎟ ⎜ ⎟

### ⎝ ⎠ ⎝ ⎠ ⎝ ⎠ ⎝ ⎠

### ⎛ ⎞

### ⎜ ⎟

### > → ⎜ ⎟

### ⎜ ⎟

### ⎜⎜ ⎟⎟

### ⎝ ⎠

∑


Operator in Decimal Notation in the

Matrix Form

```
11
```
```
00
```
```
00 01 02 03
```
(^310111213)
, (^020212223)
30 31 32 33
1 0 0 0
0 0 0 0
.....
0 0 0 0
0 0 0 0
_kn
kn
k n
X
a a a a
a a a a
a X
a a a a
a a a a_
=
⎛ ⎞
⎜ ⎟
→ ⎜ ⎟
⎜ ⎟
⎜ ⎟
⎝ ⎠
⎛ ⎞
⎜ ⎟
→ ⎜ ⎟
⎜ ⎟
⎜ ⎟
⎝ ⎠
∑


Tensor Product of One-Qubit Operators

- Basic relation:
(|k><n|) (|p><q|) =|kp><nq|
- Example:

### ⊗

[ ] [ ]

```
1 2 1 2
```
```
00 11 22 33
```
| 0 0 | | 1 1 | | 0 0 | | 1 1 |

| 00 00 | | 01 01 | | 10 10 | | 11 11 |

| 0 0 | | 1 1 | | 2 2 | | 3 3 |

```
z z z z
```
_X X X X_

σ ⊗σ =σ σ =

>< − >< ⊗ >< − >< =

```
>< − >< − >< + >< →
>< − >< − >< + >< =
```
− − +


Tensor Product of One-Qubit Operators

```
in the Matrix Form:
Tensor Product of 2x2 Matrices
```
### ' ' ' '

### ' ' ' ' ' '

### ' ' ' ' ' '

### ' ' ' '

```
aa ab ba bb
a b a b ac ad bc bd
c d c d ca cb da db
cc cd dc dd
```
### ⎛ ⎞

### ⎛ ⎞ ⎛ ⎞ ⎜ ⎟

### ⎜ ⎟⊗⎜ ⎟ = ⎜ ⎟

### ⎝ ⎠ ⎝ ⎠ ⎜ ⎟

### ⎜ ⎟

### ⎝ ⎠


```
8
```
Example

```
1 2
```
```
00 11 22 33
```
1 0 1 0

0 1 0 1

1 0 0 0

```
0 1 0 0
=
0 0 1 0
```
0 0 0 1

```
z z
```
_X X X X_

σ σ

```
⎛ ⎞ ⎛ ⎞
⊗ → ⎜ ⎟ ⊗⎜ ⎟
⎝ − ⎠ ⎝ − ⎠
```
```
⎛ ⎞
⎜ ⎟
−
⎜ ⎟
⎜ − ⎟
⎜ ⎟
⎝ ⎠
```
→ − − +


```
One-Qubit Operators in the Two-
Qubit Hilbert Space
```
- Action of _σx1_^ in binary notation:^

σ _x_ 1 ( _C_ 0 | 00 > + _C_ 1 | 01 >)= ( _C_ 0 | 10 > + _C_ 1 | 11 >)

```
1 2 1
1 2 2
```
```
x x
x x
```
```
E
E
```
```
σ σ
σ σ
```
```
⊗ =
⊗ =
```

Irreducible Two-Qubit Operators.

Example: Control Not (CN) Gate.

```
12
12
12
12
```
```
00 00
01 01
10 11
11 10
```
```
CN
CN
CN
CN
```
```
⎧ = ⎫
⎪ ⎪
⎪ = ⎪
⎨ ⎬
⎪ = ⎪
⎪ = ⎪
⎩ ⎭
```

```
12
```
```
12
```
```
12
```
```
12
```
```
00 11 23 32
12
```
Decimal notation

0 0

1 1

2 3

3 2

_CN_

_CN_

_CN_

_CN_

_CN X X X X_

```
⎧ = ⎫
⎪ ⎪
⎪ = ⎪
⎨ ⎬
⎪ = ⎪
⎪ = ⎪
⎩ ⎭
```
= + + +

```
12
12
12
12
```
```
00 00
01 01
10 11
11 10
```
```
CN
CN
CN
CN
```
⎧ = ⎫
⎪ ⎪
⎪ = ⎪
⎨ ⎬
⎪ = ⎪
⎪ = ⎪
⎩ ⎭


Summary of 2-Qubit Hilbert Space

- Tensor product →^ transfer to the 2-qubit Hilbert

```
space.
```
- Inner product of vectors in the two-qubit Hilbert
    space → complex number
- Outer product →^ operators
- Decimal notation for vectors and operators
- Entangled states (e.g. Bell states)
- Irreducible operators (e.g. CN gate)


Quantum Measurement in a

Two-Qubit Hilbert Space


Standard Measurement Basis

Measurement basis:

standard basis of the Hilbert space |kn>

- A) Measurement of the state (MS) of two
    qubits
- 1. Non-demolition measurement.


2. General case

```
00 01 10 11
```
MS

```
ψ = C 0 00 + C 1 01 + C 2 10 + C 3 11
```
ψ →

```
00 01 10 11
```
```
↓ ↓ ↓ ↓
```
Probabilities 2
_Pk_ = _Ck_


```
5
```
```
Measurement with Non-Standard
Basis
```
- Example:
- Measurement basis |vkvn> (k,n = 0, 1)
-
- Measurement of the state:
- 1. Write vector of state |ψ> in the
    measurement basis |vkvn>
- 2. P(|vkvn>) = |< vkvn | ψ>|^2


```
Measurement of the State of a Single
Qubit
```
Measurement of the state of the **first** qubit (MS 1 )

Measurement basis: standard basis of the first
qubit.

```
ψ = C 0 00 + C 1 01 + C 2 10 + C 3 11
```

```
ψ = C 0 00 + C 1 01 + C 2 10 + C 3 11
```
ψ → MS 1

```
0 1
2 3
2 2
2 3
```
```
0 1
1
```
```
C C
C C
```
```
+
⊗
+
```
```
0 1 0 1
2 2
0 1
```
```
0 1 0 1
0 0
...
```
```
C C C C
C C
```
```
+ +
⊗ = ⊗
+
```
```
P = C 22 + C 32
```
```
2 2
P = C 0 + C 1
```

```
8
```
Measurement of the state of the **second**
qubit

Measurement basis: standard basis of the
second qubit.

```
ψ = C 0 00 + C 1 01 + C 2 10 + C 3 11
```

```
ψ = C 0 00 + C 1 01 + C 2 10 + C 3 11
```
ψ → MS 2

```
0 1
1 3
2 2
1 3
```
_C_ 0 _C_ (^11)
_C C_
+ ⊗
+
0 2
2 2
0 2
0 1
0
_C C
C C_
+
⊗
+
_P_ = _C_ 12 + _C_ 32
_P_ = _C_ 02 + _C_ 22


Example

- The state of two qubits is described by the
    vector
- |ψ> = (1/5)1/2 |00> + (2/5)1/2 |01> + (2/5)1/2 |11>
- One measures the state of the first qubit.
- A) If the outcome of the measurement is |0>
    what is the state of the qubits after the
    measurement?
- B) What is the probability of this outcome?


Solution (A)

(^1) | 0 2 | 1
| | 0 5 5
1 2
5 5
| 0 1 | 0 2 | 1
3 3
ψ
> + >
>→ >⊗
+
⎛ ⎞
= >⊗⎜⎜ > + >⎟⎟
⎝ ⎠
|ψ> = (1/5)1/2 |00> + (2/5)1/2 |01> + (2/5)1/2 |11>


Solution (B)

- |ψ> = (1/5)1/2 |00> + (2/5)1/2 |01> + (2/5)1/2 |11>

### • P(|0> 1 ) = (1/5) + (2/5) = 3/5 = 0.6.


```
Quantum Entanglement and a
Single-Qubit Measurement
```
- Measurement of a single qubit in the Bell
    state B 0 :

### • |B 0 > = 2-1/2(|00> + |11>)

- After the measurement the states of two
    qubits must be the same!
- Non-physical state? Actually |00> or |11>? 13


Why Not? Example

- Write the Bell state
- |B 0 > = 2-1/2(|00> + |11>)

in the basis |vkvn>


Solution

### • |B 0 > = 2-1/2(|00> + |11>)

- = 2-1/2 (1/2) [(|v 0 > + v 1 >) (|v 0 > + v 1 >)
- + (|v 0 > - v 1 >) (|v 0 > - v 1 >)]
- = 2-1/2 (1/2) (|v 0 v 0 > + |v 0 v 1 > + |v 1 v 0 > + |v 1 v 1 >
- + |v 0 v 0 > - |v 0 v 1 > - |v 1 v 0 > + |v 1 v 1 >)
- = 2-1/2 (|v 0 v 0 > + |v 1 v 1 >)


-^2 -1/2 (|v 0 v 0 > + |v 1 v 1 >)
- Again, after the measurement

the states of two qubits must be the same!

- (The same is true for any measurement
    basis |bk> with the Bloch vectors in the x-z
    plane)
- May be the entangled states cannot be
    created?


Nobel Prize in Physics for 2022

```
17
```
Alain Aspect, John F. Clauser and Anton

Zeilinger (France, USA, and Austria)


New Question

- |B 0 > = 2-1/2(|00> + |11>) = 2-1/2 (|v 0 v 0 > + |v 1 v 1 >)
-
- Superluminal transfer of information?
- No.
- The outcome is random!


Using quantum measurement one can transfer
information about measurement basis:

- If Alice uses the standard measurement basis the
Bob’s outcome is either |0> or |1>.
- If Alice use the measurement basis |vk> the Bob’s

outcome is either |v 0 > or |v 1 >.

- Superluminal transfer of information?
- No.
- Bob has to copy the state!


No-Cloning Theorem

- Superluminal transfer of information

violates the basic principle of relativity.

**- → No-cloning theorem:
-
- Cloning of an arbitrary quantum state is**
    **impossible.**


```
2121
```
```
Decomposition of any Quantum Logic
Gates (QLG)
```
- Barenco et al., 1995.
- Theorem:
- Any QLG can be decomposed into one-qubit
    rotations and a two-qubit Control-Not (CN) gate.
- If one can implement **Ry(α), Rz(α), and CNpq**
    gates then the problem of deterministic unitary
    evolution is solved.
- (It is not the only decomposition.) 21


QCD for a Control-Not Gate

### CN 12

### CN 21


Decomposition of the Control Not

Gate into Simpler Gates


Two-Qubit U(π/4)-Gate

- U(π/4)|kk> = exp(iπ/4)|kk>
- U(π/4)|kn> = exp(-iπ/4)|kn>, k ≠ n


Example

- Write U(π/4)-gate in decimal notation in
    terms of the Hubbard operators.
- U(π/4)|kk> = exp(iπ/4)|kk>
- U(π/4)|kn> = exp(-iπ/4)|kn>, k ≠ n


Solution

- U(π/4) = exp(iπ/4)(|00><00| +|11><11|)
- + exp(-iπ/4)(|01><01| +|10><10|)
- = exp(iπ/4)(X^00 + X^33 ) + exp(-iπ/4)(X^11 + X^22 )


```
2727
```
QCD for CN 12 ·exp(-iπ/4)

```
HG 2 U(π/4) Rz2(π/2)
```
```
Rz1(π/2)
HG 2
```
```
/ 2
/ 2 00 / 2 11
/ 2
```
```
0
( )
0
```
```
i
i i
z i
```
_e
R e X e X
e_

```
α
α α
α α
```
```
−
= − + =⎛ ⎞
⎜ ⎟
⎝ ⎠
```
```
HG|0> = 2-1/2(|0> + |1>)
```
```
HG|1> = 2-1/2(|0> - |1>)
```

Algebraic Formula

exp(-iπ/4)CN 12

= HG 2 ·Rz1(π/2)·Rz2(π/2) U(π/4)·HG 2

```
HG 2 U(π/4) Rz2(π/2)
```
```
Rz1(π/2)
HG 2
```

Verification for |00>

- Check: |00> → e-iπ/4 |00>
- 1. HG 2 |00> = |0>(1/21/2)(|0> + |1>) =
- = (1/21/2)(|00> + |01>)
- 2. U(π/4):

(1/21/2)(eiπ/4 |00> + e-iπ/4|01>)

- 3. Rz1(π/2):^
- (1/21/2) e-iπ/4(eiπ/4 |00> + e-iπ/4|01>)^29


Continue

- (1/21/2) e-iπ/4(eiπ/4|00> + e-iπ/4|01>) =
- = (1/21/2) e-iπ/4 |0>⊗(eiπ/4|0> + e-iπ/4|1>)
- 4. Rz2(π/2):
- (1/21/2) e-iπ/4 |0>⊗(|0> + |1>)

### • 5. HG 2 :

- (1/2) e-iπ/4 |0>⊗(|0> + |1> + |0> - |1>) =
- = e-iπ/4 |00>^30


Continue

- In the same way:
- |01> → e-iπ/4 |01>
- |10> → e-iπ/4 |11>
- |11> → e-iπ/4 |10>
- QCD for {CN 12 ·exp(-iπ/4)} gate is correct.^31


```
Summary of Lecture 8
```
- Quantum measurement in the 2-qubit Hilbert
    space:
- A) Measurement of the state of two qubits
- B) Measurement of the state of a single qubit.
- No-Cloning theorem.
- Decomposition of any quantum logic gate into
    CN gate and one-qubit gates.
- Decomposition of CN gate into U(π/4) gate and
    one-qubit gates.


Physical Implementation of

U(π/4) Gate.


```
Hamiltonian for U(π/4) Gate
```
- Hamiltonian of the Ising interaction:
- H ≈ - ħJ σz1 σz2^
- J – interaction constant (unit 1/s or rad/s)

```
Ernst Ising (Germany),
1900 – 1998.
```

```
Eigenvector and Eigenvalues of the
Ising Hamiltonian
```
- H ≈ - ħJ σz1 σz2
- Eigenvectors |00> and |11>,
- Eigenvalue E = -ħJ
-
- Eigenvectors |01> and |10>,
- Eigenvalue E = ħJ


```
Evolution Operator Uev for the Ising
Hamiltonian
```
- E = -ħJ, E = ħJ
- Uev (t) = exp(-iHt/ħ)
- = exp(iJt) {|00><00| + |11><11|}
- + exp(-iJt) {|01><01| + |10><10|}
- Uev (t)|kk> = exp(iJt)|kk>
- Uev (t)|kn> = exp(-iJt)|kn>, k ≠ n


Implementation of U(π/4) Gate

- Uev (t)|kk> = exp(iJt)|kk>,
- Uev (t)|kn> = exp(-iJt)|kn>, k ≠ n
- Controllable Ising interaction.
Choose duration of interaction t 0 = π/(4J):

Jt 0 = π/4

- Uev (t 0 )|kk> = exp(iπ/4)|kk>
- Uev (t 0 )|kn> = exp(-iπ/4)|kn>, k ≠ n
- →^ Uev (t 0 ) = U(π/4)
- → U is the U(π/4) gate!

```
6
```

```
Ising Interaction in Physics.
Dipole-Dipole and Ising Interaction.
```
- Ed = (μ 0 /4πr^3 ){ **m 1 •m 2** – 3( **m 1 •n 12** ) ( **m 2 •n 12** )}
- Hd = (μ 0 /4πr^3 )(μB^2 ){ **σ 1 • σ 2** – 3( **σ 1 •n 12** ) ( **σ 2 •n 12** )}

```
m 1
```
```
m 2
```

```
Strong Non-Uniform Magnetic Field B
along the z-axis
```
- If magnetic atoms experience strong non-
    uniform magnetic field in the positive z-
    direction then the dipole interaction,
    approximately, transforms to the Ising
    interaction.


Physical Explanation

**- B** = **B** ex + **B** d^ Bex >> Bd^
**- B** = **k** Bex + **i** Bdx + **j** Bdy + **k** Bdz
- B = {(Bex + Bdz)^2 + Bdx^2 +^ Bdy^2 }1/2^
- ={(Bex + Bdz)^2 [1 + (Bdx^2 + Bdy^2 )/(Bex + Bdz)^2 ]}1/2
- = (Bex + Bdz)[1 + (1/2) (Bdx^2 + Bdy^2 )/(Bex + Bdz)^2 ]
- = (Bex + Bdz) + (1/2) (Bdx^2 + Bdy^2 )/(Bex + Bdz)
- The x- and y- components of the dipole field are
    suppressed!^9


- Hd = (μ 0 μB^2 /4πr^3 ){ **σ** 1 **• σ** 2^ – 3( **σ** 1 **•n** 12 ) ( **σ** 2 **•n** 12 )}
**- σ 1** → **k** σz1,^^ **σ 2** → **k** σz2^ **k•n** 12 = cosθ^

Hd → (μ 0 μB^2 /4πr^3 )⋅{σz1σz2 – 3(σz1cosθ) (σz2cosθ)}

-^ ≈ - ħJσz1 σz2
- ħJ = (μ 0 μB^2 /4πr^3 )[3cos^2 (θ) – 1]

```
θ
```
```
z
```
```
n 12
```
```
B ex
```

- ħJ = (μ 0 μB^2 /4πr^3 )[3cos^2 (θ) – 1]
- θ = 0: maximum Ising interaction
- ħJ = μ 0 μB^2 /2πr^3
- Example: for r = 8 nm:
- J = πx10^5 rad/s
- J/2π=50 kHz

```
Bex
```

Magic Angle

- ħJ = (μ 0 μB^2 /4πr^3 )[3cos^2 (θ) – 1]
- When θ increases the interaction constant
    decreases.

• When cos^2 (θ) = 1/3, then ħJ = 0. (^)

- Magic angle. θ = θM = 54.7^0


Change of the Sign of Interaction

**- B**^ When θ > θM = 54.7^0

```
the interaction constant
becomes negative
In particular, for
```
```
θ = π/2: J = - (μ 0 /4πħ)(μB^2 /r^3 )
```
```
J/2π = -25 kHz
```
**-**

```
Bex
```

Other Systems with Ising Interaction

- Ising interaction was found in many
    materials with rare earth elements.
- The simplest “Ising material”:
- DyPO 4
- Superconducting qubits:
- Effective spins with the Ising interaction.


Decomposition of 2–

```
and 3-Qubit Gates
into the CN-Gates
and 1-Qubit Gates
```

SWAP Gate

_kk_ → _kk_ , _kn_ → _nk_


Decomposition of the SWAP Gate

- SWAP = CN 12 CN 21 CN 12
- Verification for |01>: (|01> → |10>)

### • CN 12 |01> = |01>

### • CN 21 |01> = |11>

### • CN 12 |11> = |10>

### • |01> → |10>^17


( )

( )( ) ( )( )

```
00 12 21 33
```
### 00 1 1 11 22 33 1 1 12 21

### 2 2

_iSWAP X i X X X_

### SWAP

```
X i X X X i X X
```
```
SWAP SWAP SWAP
```
### = + + +

### = + + + + + − +

### ⋅ =


CN 12 Gate Based on Zero

```
σ x σ x
```
```
σ x − gate = Not gate
```
```
CN 12
```
_CN_ 12 = Decomposition
QCD:


CN 12 Gate Based on Zero: Decomposition

```
σ x σ x
```
```
σ x − gate = Not gate
```
```
CN 12
```
```
CN 12 =
```
```
Next slide - verificationQCD
```

Verification of Decomposition for |

00>

```
12
```
```
1 12 1
1 12
1
```
| 00 | 01

```
| 00
| 10
| 11
| 01
```
_CN_

```
N CN N
N CN
N
```
>= >

```
>
= >
= >
= >
```

Other Popular Two-Qubit Gates

( )

```
12
12
```
```
Control single qubit gate:
```
Example: (^) _z_ ( )

### CU

```
CR α
```
### ⎧

### ⎪

### ⎨

### ⎪

### U ⎩

```
/ 2
/ 2
```
```
0
( )
0
```
```
i
z i
```
```
e
R
e
```
```
α
α α
```
```
⎛ − ⎞
=⎜ ⎟
⎝ ⎠
```

Multiple Target and Multiple Control

Gates

```
Example:
3-qubit
gate
```
```
CNk... -gate
CmN... -gate
CmNk... -gate
CmUk... -gate
```
```
2
CN 1 , 23
```

Problem

- Consider two atoms, each with an electron
    spin (1/2). The strong non-uniform
    magnetic field **B** transforms the magnetic
    dipole-dipole interaction between the spins
    into the Ising interaction. When magnetic
    field **B** points along the line (line L)
    connecting the two atoms the Ising
    interaction constant J = 500 rad/s. At what
    angle θ between **B** and L the value of J will
    be 100 rad/s? Hint: consider J(θ)/J(0).
-^ ħJ(θ) = (μ 0 μB^2 /4πr^3 )[3cos^2 (θ) – 1]


Solution

- ħJ(θ) = (μ 0 μB^2 /4πr^3 )[3cos^2 (θ) – 1]
- ħJ(0) = (μ 0 μB^2 /4πr^3 )⋅^2
- J(θ)/J(0) = [3cos^2 (θ) – 1]/2 = 100/500 = 1/5
- 3cos^2 (θ) – 1 = 2/5 (= 0.4)
- cos^2 (θ) = 1.4 / 3
**- θ = 46.9**^0


Problem

- Express the SWAP gate in terms of the
    Hubbard operators in decimal notation.

_kk_ → _kk_ , _kn_ → _nk_


Solution

```
00 21 12 33
```
,

```
| 00 00 | | 01 10 |
| 10 01 | | 11 11 |
```
_kk kk kn nk_

_SWAP_

_X X X X_

→ →

= >< + ><

+ >< + ><

= + + +


Problem

0 ( )

```
Compute in decimal notation:
1
| | 0 | 3
2
```
```
SWAP B >= SWAP > + >
```
(^00) ( )( (^1122) ) (^33) ( )( (^1221) )
(^1111)
2 2
_SWAP_
= _X_ + + _i X_ + _X_ + _X_ + − _i X_ + _X_


```
Solution
```
( )( ) ( )( )

( )

( )

```
0
00 11 22 33 12 21
```
```
0
```
```
|
1 1
1 1
2 2
1
| 0 | 3
2
1
| 0 | 3 |
2
```
```
SWAP B
```
```
X i X X X i X X
```
```
B
```
```
>
```
= ⎧ + + + + + − + ⎫
⎨ ⎬
⎩ ⎭

```
> + >
```
= > + > = >


Problem

12 ( )

Compute:

```
1
| 00 | 11
2
```
_CN_ > + >


Solution

( )

( )

( )

```
12
```
```
1
| 00 | 11
2
1
| 01 | 11
2
1
| 0 | 1 | 1
2
```
_CN_ > + >

= > + >

= > + > ⊗ >


Problem

- Compute [CRz(π)] 12 {(1/2)1/2 (|00> + |11>)}

```
/ 2
/ 2
```
```
0
( )
0
```
```
i
z i
```
```
e
R
e
```
```
α
α α
```
```
⎛ − ⎞
=⎜ ⎟
⎝ ⎠
```

Solution

- [CRz(π)] 12 (1/2)1/2 (|00> + |11>)
- = (1/2)1/2 (|00> + exp(iπ/2)|11>)
- = (1/2)1/2 (|00> + i·|11>)


Problem with the Hadamard Gate

### • HG = (1/21/2)(X^00 + X^10 + X^01 - X^11 )

- Find (HG)^2.


Summary of Lecture 9.

- H ≈ - ħJ σz1 σz2^
- Using the Ising interaction one can
    implement U(π/4) gate.
- Ising interaction can be implemented, for
    example, using the magnetic dipole-dipole
    interaction.
- One can control the magnitude and sign of
    the interaction constant J.


Summary Continued

- SWAP gate (notation for X|p>!)
- iSWAP
- (SWAP)1/2
- CN gate based on zero (notation!)
- CU gate
_- CmUk..._ gate


Quantum Fourier Transform(FT)
1

```
, 0
```
```
1 2
,
```
```
D
i km km
m k
```
```
FT e X
D D
```
α α π

```
−
```
```
=
```
= ∑ =

```
1
```
```
0
```
```
1
```
```
2
Elementary phase =
```
```
For every next term " "
the phase shift is ( )
```
```
D i nk
```
```
k
```
```
FT n e k
D
```
```
D
k
n
```
```
α
```
```
π
α
```
```
α
```
```
−
```
```
=
```
= ∑


Example

- Compute FT|0> for a single qubit.

( )

```
1
```
```
0
```
```
2
2 2 Elementary phase =
```
```
1
```
0 0

```
1
| 0 | 0 | 1
2
```
```
L
```
```
D i nk
```
```
k
```
```
D
D
```
```
FT n e k
D
n
```
```
FT
```
```
α
```
```
π
α π
```
```
α α
```
```
−
```
```
=
```
```
= = → =
```
```
=
```
```
⋅ = ⋅ =
```
```
>= > + >
```
∑


Computation of FT|1>

( )

( )

```
2
2 2 , ,
```
```
1
1
| 1 | 0 | 1
2
1
| 0 | 1
2
```
```
L
```
```
i
```
```
D
D
n
```
```
FT e
```
```
FT HG
```
```
π
```
```
π
α π
```
```
α α π
```
```
= = = =
```
```
⋅ = ⋅ =
```
```
>= > + >
```
```
= > − >
```
```
=
```

```
Simplification of Phase Factors
for L ≥ 2
```
- Phase factor diagram:
- Use complex plane.
- Draw a circle of unit radius.
- Show the phase factors on the circle.


```
Quantum FT for Two Qubis.
Two qubits: 2 4 ,
2
4 2
0 1 ( 0 1 2 3 )
2
1 1 ( 0 1 2 3 )
2
2 1 ( 0 1 2 3 )
2
3 1 ( 0 1 2 3 )
2
```
```
D L
```
```
FT
```
```
FT i i
```
```
FT
```
```
FT i i
```
α π π

```
= =
```
```
= =
```
```
= + + +
```
```
= + − −
```
```
= − + −
```
```
= − − +
```
(^) ( 0 , 0 , 0 , (^0) )
1 : 0 , , ,^3
2 2 2
⋅α =π ⎛ π π π ⎞
⎜⎝ ⎟⎠
2 ⋅α =π (^) ( 0 ,π, 2 π, 3 π)
3 3 0 ,^3 , 3 ,^9
2 2 2
⋅α = π ⎛ π π π ⎞
⎜⎝ ⎟⎠
Draw phase factor diagram


Quantum FT for 3 qubits

### • D = 2L = 2^3 = 8

- α^ = 2π/8 = π/4

### • FT|0>

### • FT|1>

### • FT|2>


Decomposition of FT for 3 Qubits

```
9
```
1) HG 1 , 2) CS 21 , 3) CT 31 , 4) HG 2 , 5) CS 32 ,
6) HG 3 , 7) SWAP 13.
Definitions: S|0> = T|0> =|0>,
S|1> = exp(iπ/2)|1>, T|1> = exp(iπ/4)|1>.


Verification

- Verify the previous QCD for the state

|0> = |000>

### 1)HG 1 , 2) CS 21 , 3) CT 31 , 4) HG 2 , 5) CS 32 ,

### • 6) HG 3 , 7) SWAP 13.^

### •

- S|1> = exp(iπ/2)|1>, T|1> = exp(iπ/4)|1>.


```
11
```
### 1) HG 1 , 2) CS 21 , 3) CT 31 , 4) HG 2 , 5) CS 32 , 6) HG 3 ,

### 7) SWAP 13.

### • HG 1 |000> = (1/2)1/2 (|0> + |1>) |00>;

### • CS 21 ; CT 31 ;

### • HG 2 (1/2)1/2 (|0> + |1>) |00>

### • = (1/4)1/2 (|0> + |1>) (|0> + |1>) |0>;^ CS 32 ;

### HG 3 (1/4)1/2 (|0> + |1>) (|0> + |1>) |0>

= (1/8)1/2 (|0> + |1>) (|0> + |1>) (|0> + |1>) = |ψ>


Continue

- |ψ> = |(1/8)1/2 (|0> + |1>) (|0> + |1>) (|0> + |1>)
- = (1/8)1/2 (|000> + |001> +|010> + |011>
    + |100> + |101> +|110> + |111>)
- SWAP 13 |ψ>
- = (1/8)1/2 (|000> + |100> +|010> + |110>
    + |001> + |101> +|011> + |111>) = |ψ>
- |ψ> = (1/8)1/2 (|0> + |1> +|2> + |3>
    + |4> + |5> +|6> + |7>)


Shor’s Quantum Algorithm

- Period Finding and Prime
    Factorization


From the Math

- y = f(x) = ax mod N

= remainder of the fraction (ax / N)

Example: a = 2, N = 3.

y = 2x mod 3:

20 mod 3 = 1

21 mod 3 = 2

22 mod 3 = 1

23 mod 3 = 2

24 mod 3 = 1

...

```
14
```
```
(Graph a discrete
function)
```

Continued

- Let “a _”_ is coprime to N (“a” shares no factors
    with N except of 1).
- 1) Consider the equation
- (ax mod N) = 1
- The minimum positive solution of this equation
    x 0 is **“the order of (a mod N)”**
- In our example: the order of (2 mod 3) = 2.


Continued

- 2) (ax mod N) is a periodic function of x.
- The period T of this function equals the
    order of ( _a_ mod N).
- 3) T is even with probability P > 1/2.


```
17
```
```
Shor’s Algorithm for Prime Factorization of Number
N = N 1 ⋅ N 2 (N 1 and N 2 are the prime factors)
```
1.Choose number “ _a”_ which is coprime to N
2.QC: Compute the periodic function:

(The number of electrons in the visible Universe is
about 10^82 = 2^272 ).^

3. QC: Find period T of this function

```
( ) (mod )
For a large number N, the required number
of values x and y is greater than the number
of electrons in the visible Universe.
```
```
y = f x = ax N
```

```
18
```
4. Compute
5. Compute

if it is not a factor of _N_

compute

One of these numbers is the factor of N.

```
z = aT /^2
GCD ( z − 1 , N )
```
```
GCD ( z + 1 , N )
```
```
“Classical computer”:
```

```
19
```
4. Compute
5. Compute

if it is not a factor of _N_

compute

One of these numbers is the factor of N.

```
z = aT /^2
GCD ( z − 1 , N )
```
```
GCD ( z + 1 , N )
```
```
“Classical computer”:
```

Problem

- Find the order of (3 mod 4).


Solution

- y = 3x mod 4.

```
21
```
```
Order of (3 mod 4) = 2
{Period T of (3x mod 4) = 2}
```
```
x y
0 1
1 3
2 1
3 3
4 1
```

```
2222
```
```
/ 2 1
```
```
4 , 3
3 (mod 4 )
2
/ 2 1
3 3
( 1 , ) ( 3 1 , 4 ) 2
The factor of 4 is 2.
```
```
x
```
```
T
```
```
N a
y
```
_T_

_T_

```
z a
GCD z N GCD
```
```
= =
=
=
=
= = =
− = − =
```
```
Example based on the previous problem.
Find the factor of N = 4 using the Shor’s
algorithm. Assume that a = 3.
```

- “Intrinsic” error in the algorithm:

odd period.

(Probability P < ½. Actually it is very small.)

→ Change a coprime number “a”


Problem

Find the factor of N = 15 using the Shor’s
algorithm. Assume that a = 7.

Hint:

Find period T of y = 7x mod 15

Compute z = 7T/2

Find GCD (z-1, 15)


Solution

- N = 15, a = 7. y = 7x mod (15):
- x = 0, y = 1,
- x = 1, y = 7,
- x = 2, y = 4, (quotient 3)
- x = 3, y = 13 (quotient 22)
- x = 4, y = 1 (quotient 160)
- Order of (7 mod 15) = 4
- T = 4, z = 74/2 = 49, GCD(48, 15) = 3


Summary of Lecture 10.

- FT gate
- Simplification of phase factors.
- Decomposition of FT gate into Hadamard
    gate and (CU)kn gates.
- Shor’s quantum algorithm (overview)
- {The order of (a mod N)}


Period Finding


Algorithm for Period Finding: Simplified

Version.

- 1. Use 2 registers “x” and “y”, and start
    from the ground state for the qubits:
- |x, y> = |0,0>
- 2. Create the uniform superposition of the
    numbers in the x-register (Rky(π/2) – gates)
    :
       1

```
0
```
```
1
, 0 , = 2
```
```
x
x
```
```
D
L
x
x k
```
```
k D
D
```
```
−
```
```
=
```
∑


- 3. Compute the periodic function

f(k) =ak mod N (f-gate)

```
1 1
```
```
0 0
```
```
1 1
, 0 = , ( )
```
```
Dx Dx
```
```
x k x k
```
```
f k k f k
D D
```
```
− −
```
```
= =
```
∑ ∑


4. Measure the state of the y-register:
    outcome is not important (not a
    mandatory step).
5. Apply FT to the x-register
6. Measure the value of x


7. If x ≠ 0 consider the fraction Dx/x {Dx = 2^(Lx)}
If x = 0 repeat the whole procedure
8. Reduce the fraction to the lowest terms Dx/x = D’/x’.

(With the probability about 50% D’ = T.)

9. Verify whether aD’ mod N = 1
{In general verify f(D’) = f(0)}
10. If aD’ mod N ≠ 1 repeat the whole
procedure until you get the numerator D’ = T.


```
0
```
```
1
```
```
Example: Find the period of a function ( ) mod 2.
```
Consider 2 qubits in the x-register, 1 qubit in the y-register.

Start from the ground state.

```
Binary notation: 00 0 , (See the next slide)
```
```
y ( /^2 )
```
```
f x x
```
```
R
```
```
ψ
```
```
π
```
```
=
```
```
=
```
```
2 0
```
```
1
```
```
23
```
```
23 1 2
```
```
2
```
```
( / 2 )^1 ( 00 01 10 11 ) 0
2
1 ( 00 , 0 01 , 0 10 , 0 11 , 0 )
2
For f(x) = x mod 2 , the f-gate = CN :
```
(^1) ( 00 , 0 01 , 1 10 , 0 11 , 1 )
2
(^1) ( 0 , 0 1 , 1 2 , 0 3 , 1 )
2
_Ry
CN_
π ψ
ψ
ψ ψ
ψ
= + + +
= + + + =
= + + + =
= + + +


Reminder: Rotational Gate

( )

( ) ( )

( ) ( )

( )

```
0 0 1 1
00 11 01 10
```
```
00 10 01 11
```
```
( ) exp / 2
```
```
exp / 2 | | exp / 2 | |
```
```
cos sin
2 2
1
( / 2 )
2
```
```
y y
```
```
y
```
```
R i
```
```
i w w i w w
```
```
X X X X
```
```
R X X X X
```
```
α ασ
```
```
α α
α α
```
```
π
```
```
= −
```
= − >< + ><

= + + − +

```
= + − +
```

```
99
```
2
Decimal notation: 1 ( 0 , 0 1 , 1 2 , 0 3 , 1 )
2

Let ( 0 ): 1 ( 0 , 0 2 , 0 )^1 ( 0 2 ) 0
2 2

1 ( 0 2 )^1 ( 0 1 2 3
2 2 2
+ 0 1 2 3 )

=^1 ( 0
2

```
y
```
```
x
```
```
M y
```
```
FT
```
```
ψ = + + +
```
```
= + = +
```
```
+ = + + +
```
```
− + −
```
```
+ 2 )
```
') ( 0 )

'') ( 2 )

4 2 , Check ( 2 ) ( 0 ) 0
2 1
2

```
x
x
x
```
```
A M x
A M x
D f f
x
T
```
```
=
=
= = = =
=
```

```
1010
```
```
2
```
One more example: y = x mod 4. L 3. 2 / 8 / 4

Decimal notation: 1 ( 0 , 0 1 , 1 2 , 2 3 , 3
8
4 , 0 5 , 1 6 , 2 7 , 3 )

```
) ( 0 ): 1 ( 0 , 0 4 , 0 )^1 ( 0 4 ) 0
2 2
1 ( 0
2
```
```
x
```
```
y
```
```
x
```
```
A M y
```
```
FT
```
```
α π π
```
```
ψ
```
```
= = =
```
```
= + + +
```
```
+ + + +
```
```
= + = +
```
```
+ 4 )^1 ( 0 1 2 3
4
+ 4 5 6 7
+ 0 1 2 3
+ 4 5 6 7 )
```
```
=^1 ( 0 2 + 4 6 )
```
```
= + + +
```
```
+ + +
− + −
− + −
```
```
+ +
```

```
1111
```
( )

```
2
Decimal notation: 1 ( 0 , 0 1 , 1 2 , 2 3 , 3
8
4 , 0 5 , 1 6 , 2 7 , 3 )
```
```
) ( 1 ): 1 ( 1 , 1 5 , 1 )^1 ( 1 5 ) 1
2 2
1 / 4 , 5 = 5 / 4 = + / 4 , " " exp / 4
```
```
1 ( 1 5 )^1
2 4
```
```
y
```
```
x
```
```
B M y
```
```
e i
```
```
FT
```
```
ψ
```
α π α π π π π

```
= + + +
```
```
+ + + +
```
```
= + = +
```
```
⋅ = ⋅ =
```
```
+ = ( 0 1 2 3
```
- 4 5 6 7
+ 0 1 2 3
- 4 5 6 7 )

```
=^1 (
```
```
e i ie
```
```
e i ie
e i ie
e i ie
```
```
+ + +
```
```
− − −
− + −
+ − +
```
```
0 2 4 6 )
+ i − − i
```

: 0 , 2 , 4 , 6

```
8 4 8 2 8 4
, ,
2 1 4 1 6 3
```
Check ( 4 ) ( 0 ) 0

4

) y = 2 , ...

```
x
```
```
x
```
_M x_

```
D
x
f f
T
```
_C_

=

= = = =

```
= =
→ =
```

```
Additional Information from Computer
Science
```
For an L-bit number N (L ≈ log 2 N)

the number of operations in the quantum
Shor’s algorithm is about L^3

Efficient Algorithm

-


Reduction to the Lowest Terms

Finding GCD


```
Continued Fraction Representation of
a Number
```
ak are the integers.

Rational number: a finite continued fraction.


```
Continued Fractions Algorithm
(CFA). Example with CD.
```
(^15361) (invert)
2048 2048 / 1536
1 (split to quotient and proper fraction)
1 512 / 1536
1 1 =^3 (invert: no remainder!)
(^114)
1 1
1536 / 512 3
The last devisor = GC
=
=
+
= =
+ +
D = 512


Additional Information from Math

- The simplified Shor’s algorithm can be
    directly applied to find period T for any
    periodic function if ratio Dx/x can be
    reduced to the lower terms.


Simple Example with no Common

Devisor (CD)

(^1112) (split)
9 9
1
1 (invert)
9 / 2
1 1 =^11 (split)
4 1 9
2
No CD > 1 ,
The fraction is not reducible:
it cannot be reduced to the lower terms.
= +
= +
= + ⎛ ⎞
⎜⎝ ⎟⎠
+


(^3125) (split)
13 13
2 1 (invert)
13 / 5
2 1 (split)
2 3
5
2 1 (invert)
2 1
5 / 3
= +
= +
= +
+
= +
+
2 1 (split)
2 1
1 2
3
2 1 (invert)
2 1
1 1
3 / 2
2 1 12 (split)
2 1 5
1 1
1 1
2
= +
+
+
= +
+
+
= + ≈
+
+
+⎛ ⎞
⎜⎝ ⎟⎠
**Approximation** of a Fraction with CFA
2.38
vs 2.40


Extension of the Shor’s Algorithm

- The simplified version of the algorithm works if
    fractions Dx/x reducible (i.e. can be reduced to
    the lowest terms).
- (Note: Dx = 2L →^ The simplified version

```
assumes that T = 2n, where “n” is the integer.)
```
- In general, the fraction Dx/x may be irreducible.

```
Then we use CFA to approximate the value of
fraction Dx/x. With probability about ½ the
numerator of the approximate fraction equals or
close to the period T. 20
```

Example

- Applying the Shor’s algorithm for
    decomposition of number N you have
    obtained a value of x, which does not have
    common factors with Dx. Using CFA you
    **approximate** the value Dx/x and obtained
    Dx/x ≈ 12/5.

You should check numbers p = 12, 10, 14.

- {if ap (mod N) =1 then T = p} 21


```
When Will Quantum Computers
Break RSA Encryption?
```
- A similar story: “ **Y2K crisis”.**
- Before year 2000, software programs had
    denoted years by only two digits: 2000 was the
    same as 1900.
- All the programs were expected to malfunction
    in 2000.
- The end year for Y2K clock was 2000.
- Computer programmers have fixed the bug
    before 2000.


Continued

- Information in computers is encrypted with RSA.
- “ **Y2Q crisis”** : the RSA cryptosystem can be
    broken.
- The current end year for Y2Q clock is accepted
    to be 2030 (it is a guess).
- In December 2022 the U.S. Congress passed
    “the QC Cybersecurity Preparedness Act”:
    government agencies must create a plan for
    transitioning to “post-quantum algorithms”.


Problem

```
2
```
```
1
Decimal notation: ( 0 , 0 1 , 1 2 , 0 3 , 1 )
2
( 1 ): 1 ) Find the vector of state
```
after the measurement?

: 2 ) Find the vector of state of the x-register

after application of the gate.

Reminde

```
y
```
```
x
```
```
x
```
_M y_

_FT_

_FT_

ψ = + + +

=

```
2
r:
D 2
```
```
π π
α = =
```

2
Decimal notation: 1 ( 0 , 0 1 , 1 2 , 0 3 , 1 )
2
) ( 1 ): 1 ( 1 , 1 3 , 1 )^1 ( 1 3 ) 1
2 2

1 ( 1 3 )^1 ( 0 1 2 3
2 2 2

+ 0 1 2 3 )

=^1 ( 0
2

```
y
```
```
x
```
```
B M y
```
```
FT i i
```
```
i i
```
```
ψ = + + +
```
```
= + = +
```
```
+ = + − −
```
```
− − +
```
```
2 )
−
```
Solution.


Summary of Lecture 11.

- Simplified version of the Shor’s quantum
    algorithm for period finding.
- Continued fraction algorithm.
- Extension of the Shor’s algorithm for the
    period finding.


Grover’s Algorithm

- Search over Unsorted Data
- (Gradual Increase of Probability)


```
33
```
- Grover’s algorithm: speed-up for a large class of
    the intermediate size NP problems associated
    with the search over unsorted data.
-
- Example of search over unsorted data.

Tel. book: names are sorted, telephone

numbers are unsorted.

- N tel. numbers.
- We need on average N/2 steps with simple trials.
- In Grover’s algorithm we need √N steps
- It is not an efficient algorithm


Example: Prime Factorization

50-digit number “N” (max value: 10^50 -1)

L qubits: max number = 2L - 1

Max 50-digit number requires 167 qubits

Simple trials: about 10^25 operations

```
50
```
```
1 2
25
1
```
```
10
```
```
10
```
```
N
N N N
N
```
```
<
=
<
```

```
Estimation for a Supercomputer
Speed of 10^15 Trials/Second
```
- 1025 /10^15 = 10^10 s = 3000 years^
- Grover’s algorithm: (10^25 )1/2 steps about 3x10^12
    steps
-
- 3x10^12 /10^15 = 3 ms
- Huge acceleration for an intermediate size input


```
Objective
```
- Unsorted data:

e.g. you enter a complicated or even random

function y(x), x,y – integers.

(Values of “y” - unsorted data)

Let equation y(x) = 0 has unique solution x 0.

```
Objective: find x 0.
```
Example: prime factorization

- N = N 1 N 2 (N 1 < N 2 )^ Find N 1.
- Enter function f(x) = N mod(x), 1< x < N1/2.

• Equation: N mod(x) = 0. Solution x 0 = N (^1     6)


“Phase Gate”

- Phase gate ( **decimal notation** ):
**- PG** = -X^00 +Σk≠0Xkk^^
- In general it is a many-qubit gate.
- One qubit: PG =-X^00 + X^11 = -σz.
- 2 qubits: PG = -X^00 + X^11 + X^22 + X^33
- ...


Example

- In a binary notation the vector of state is
- |ψ> = (1/2) (|001> + |010> + |000> + |111>)
- Find PG |ψ> in binary notation.
- PG |ψ> = (1/2) (|001> + |010> - |000> + |111>)


“Partial” Phase Gate

- In a binary notation the vector of state is
- |ψ> = (1/2) (|110001> + |000010> + |111000> +

+ |101111>).

- Find PG 456 |ψ> in binary notation.
- PG 456 |ψ> = (1/2) (|110001> + |000010>
- |111000> + |101111>).


```
Decomposition of the Partial Phase
Gate into Control Rotational Gate
```
- Previous example:
- |ψ> = (1/2) (|110001> + |000010> + |111000> +

+ |101111>).

- PG 345 |ψ> = (1/2) (|110001> + |000010>
- |111000> + |101111>).

( ) ( )

{ ( )}

```
3 3
```
(^345345) , 1 2 345 , 1
2
_z
z
PG C E C R
E R_
π
π
= ⎡⎣ − ⎤⎦ = ⎡⎣ ⎤⎦
− =


Grover’s Gate (GG)

- In decimal notation:
- GG(∑Cn |n>) = ∑ (2<C> – Cn)|n>
- Cn^ →^ (2<C> – Cn)

```
1
```
```
0
```
```
1
D
k
k
```
```
C C
D
```
```
−
```
```
=
```
= ∑


```
Example
```
- One qubit.
- L = 1, D = 2.^ Find GG|0> and GG|1>.
- Solution: |ψ> = 1·|0>
- C 0 = 1, C 1 = 0.
- <C> =(1)/2 = ½
- 2<C> = 1
- C 0 → 2<C> - C 0 = 1 – 1 = 0
- C 1 → 2<C> - C 1 = 1 – 0 = 1
- GG|0> = |1>^12


Continued

- |ψ> = |1> = 1·|1>,^ C 0 = 0, C 1 = 1.
- <C> = (1)/2 = ½
- 2<C> = 1
- C 0 → 2<C> - C 0 = 1 – 0 = 1
- C 1 → 2<C> - C 1 = 1 – 1 = 0
**- GG|1> = |0>**
- GG = X^01 + X^10 = σx = NOT-gate^13


Problem

- Find GG|0> and GG|1> for two qubits.
- Hint:
- Cn^ →^ (2<C> – Cn)

```
1
```
```
0
```
```
1
D
k
k
```
```
C C
D
```
```
−
```
```
=
```
= ∑


- Solution:
- Two qubits: L = 2, D = 4
- |ψ> = |0> = 1·|0> ,
- C 0 = 1, Ck≠ 0 = 0
- <C> = ¼
- 2<C> = ½
- C 0 → 2<C> - C 0 = ½ -1 = -1/2
- C k≠ 0 → 2<C> - Ck = 1/2 – 0 = ½^
**- GG|0> = (1/2)(-|0> + ∑k |k>)
- = (1/2)(-|0> + |1> + |2> + |3>)**


Solution Continued

- |ψ> = |1> = 1·|1>
- C 1 = 1, C k≠ 1 = 0
- <C> = (1)/4 = ¼
- 2<C> = ½
- C 1 → 2<C> - C 1 = ½ -1 = -1/2
- C k≠ 1 → 2<C> - Ck = 1/2 – 0 = ½^
**- GG|1> = (1/2)(-|1> + |0> + |2> + |3>)**


### • GG|0> = (1/2)(-|0> + |1> + |2> + |3>)

### • GG|1> = (1/2)(|0> - |1> + |2> + |3>)

- In the same way:
- GG|2> = (1/2)(|0> + |1> - |2> + |3>)
- GG|3> = (1/2)(|0> + |1> + |2> - |3>)
- GG|n> = (1/2) (-|n> + ∑kǂn|k>)


1) One creates superposition of all possible

states in the x-register and computes the function
y(x): |0, 0> → (1/√Dx) ∑k|k, 0>

→(1/√Dx) ∑k|k, f(k)>

= (1/√Dx) ( **|k 0 ,0>** + ∑k≠k0|k, y(k)>) (k 0 = x 0 )

2) One “marks” and then amplifies the amplitude
of the term **|k 0 , 0>** , reducing the amplitudes of
all other terms.

3) One measures the state of the x-register to
obtain value k 0.^18


Graphical Illustration


The Algorithm

- 1. Create superposition of all possible

states in the x-register

- 2. Enter (compute) function y(x)
- 3. Apply PG to the y-register
- 4. Apply GG to the x-register

(with D = Dx).


The Algorithm Continued

- 5.^ Do steps (3) and (4) K times:

K is the integer part of (πDx1/2/4):

K = [πDx1/2/4]

- 6. Make measurement on the x-register to find k 0.
    (The probability of error < ½.)
- 7. Verify that y(k 0 ) = 0. If not, run the program again.


```
The Number of Applications of PG and
GG
```
Examples:

1) For 2 qubits in the x-register (Dx = 4) :

K = [πDx1/2/4] = [π/2] = 1

2) For 3 qubits in the x-register (Dx = 8) :

K = [πDx1/2/4] = [2.2] = 2


Example

- Function y(x) →
- QC must find the value of x corresponding to

y(x) = 0

- (Solution: x 0 = 3)

```
x y(x)
0 2
1 1
2 3
3 0
```

```
0
```
```
1 2 0
```
```
1
```
```
1
```
```
1 2
```
Binary notation: 00 00

1
( / 2 ) ( / 2 ) ( 00 01 10 11 ) 00
2
1
( 00 , 00 01 , 00 10 , 00 11 , 00 )
2

Decimal notation:

```
1
( 0 , 0 1 , 0 2 , 0 3 , 0 )
2
1
( 0 , 2 1 , 1 2 , 3 3 , 0 )
2
```
_Ry Ry_

_f_

ψ

π π ψ

ψ

ψ

ψ ψ

=

= + + +

= + + + =

= + + +

= + + + =

```
x f(x)
0 2
1 1
2 3
3 0
```

- |ψ 2 > = ½^ (|0,2> + |1,1> + |2,3> + |3,0>)
- Apply PG to the y-register:
- PGy |ψ 2 > =

= ½|0,2> + ½|1,1> + ½|2,3> - ½|3,0>) = |ψ 3 >

- Apply GG to the x-register:
- <C> = ∑Ck/Dx = ∑Ck/4 = ¼,^ 2<C> = ½
- Ck^ → 2<C> - Ck = ½ - Ck^
- GG |ψ 3 > =|3,0>
- Measurement on the x-register: x = x 0 = 3
- Lx = 2 is the special case: P(error) = 0^25


Example: the Grover’s Algorithm with 4

Qubits in the x-register

- Dx = 16 (K = 3)
- Let x 0 = 4.
- Initial amplitude

```
x Initial Amplitude
0 0.25
1 0.25
2 0.25
3 0.25
4 0.25
5 0.25
6 0.25
7 0.25
8 0.25
9 0.25
10 0.25
11 0.25
12 0.25
13 0.25
14 0.25
15 0.25
```
(^1). 25
16
=


After the first application
of PG and GG the
amplitude C 4 increases to

0.46875 (not shown).

After the second
application of PG and
GG the amplitude C 4

increases to 0.6875.

```
GG
0.1875
0.1875
0.1875
0.1875
0.6875
0.1875
0.1875
0.1875
0.1875
0.1875
0.1875
0.1875
0.1875
0.1875
0.1875
0.1875
```
```
Second application
of PH and GG
```

- After the third application of PG
    and GG amplitude C 4 increases
    to 0.98.
- Measurement:
- Probability to obtain x = 4
- P = 0.98^2 = .96 = 96%

```
3rd repetition
-0.05078125
-0.05078125
-0.05078125
-0.05078125
0.98046875
-0.05078125
-0.05078125
-0.05078125
-0.05078125
-0.05078125
-0.05078125
-0.05078125
-0.05078125
-0.05078125
-0.05078125
-0.05078125
```

Error Correction


```
Conventional Computer
```
General principle of error correction: Redundancy

- Example: 3-bit redundancy
- 3 bits have the same value (you do not know this
value, it may change in the process of computation).
- You measure the values of the bits.
- If error occurs **one bit** changes its value.
- The measurement shows that this value is different
from the values of two other bits, and you change it.

Example: 000, error 001, measurement, 000.

• (^30)


```
3131
```
```
Quantum Error Correction
with a Spin (Steane, 1996)
```
```
B
```
```
Bn
τ n T
T
```
We wish to preserve the state of an electron
spin |ψ> during a time interval T. Noise pulse of
magnetic field **k** Bn may change this state.

1.We do not know the initial state |ψ>.

2. We do not know anything about the pulse.
How to recover the initial state |ψ>?

## n

# τ

```
τ n
```

( )

( )

( )

( )

```
0 0 1 1
```
```
0 0 1
```
```
1 0 1
```
### ( )

### , ( 2 / )

```
Write the vector of state in the basis :
```
### 1 1

### 0 1 0

### 2 2

### 1 1

### 0 1 1

### 2 2

```
z
n n n B n
```
```
k
```
### R

### B

```
v
C v C v
```
```
v v v
```
```
v v v
```
```
ψ α ψ
```
α ω τ ω μ

```
ψ
```
### →

### = =

### = +

### ⎧ = + ⎧ = +

### ⎪⎪ ⎪⎪

### ⎨ ⎨

### ⎪ = − ⎪ = −

### ⎪⎩ ⎪⎩

### !


Error Pulse

```
/ 2
/ 2
```
```
/ 2 / 2
0
```
```
/ 2 / 2
0 1 0 1
```
```
0 1
```
( ) 0 0
( ) 1 1
1 1
( ) ( ) ( 0 1 ) ( 0 1 )
2 2
1
= ( ) ( )
2

=cos( / 2 ) sin( / 2 )

```
i
z
i
z
i i
z z
```
```
i i
```
_R e_

_R e_

_R v R e e_

```
v v e v v e
```
```
v i v
```
```
α
α
```
```
α α
```
```
α α
```
```
α
α
```
```
α α
```
```
α α
```
```
−
```
```
−
```
```
−
```
```
=
=
```
```
= + = +
```
```
⎡⎣ + + − ⎤⎦
```
```
−
```

In the Same Way:

_Rz_ (α) _v_ 1 = cos(α / 2 ) _v_ 1 − _i_ sin(α / 2 ) _v_ 0


New Quantum Gates

- N’:
- N’|v 0 > = |v 1 >,
- N’|v 1 > = |v 0 >
- CN’ 12 :
- CN’ 12 |v 0 v 0 > = |v 0 v 0 >,
- CN’ 12 |v 0 v 1 > = |v 0 v 1 >,
- CN’ 12 |v 1 v 0 > = |v 1 v 1 >,
- CN’ 12 |v 1 v 1 > = |v 1 v 0 >.
- (CN^2 )’1,23^35


```
36
```
( )

```
0 0 1 1
```
```
0 0 1 1 0 0
```
- original state of 3 qubits

Encoding-Decoding

```
C v C v
```
```
C v C v v v
```
```
ψ
```
```
ψ
```
```
= +
```
```
= +
```
```
1
```
```
2
```
```
3
```
```
Z
```
```
Z
```
```
Z
```
```
R
or
R
or
R
```
```
M
```
```
M N ʹ/^0 ,^1 N ʹ/^1 ,^1
```
```
N ʹ/ 1 , 0 N ʹ/^1 ,^1
```
```
N ʹ/ 1 , 1
```
```
v 0 , v 1 - basis
```

( )

```
( )
( )
```
```
0 0 0 1 1 0 0 0 0 0 0 1 1 0 0
2
1 , 23 0 0 0 0 0 1 1 1 1 1
```
```
1 1 0 0 1 0 0
1 1 0 1 1
0 0 0 0 0
```
### ( )

```
/ 2. Let noise pulse acts on the first spin.
cos | sin | |
cos | sin | |
cos | si
```
```
z
```
```
C v C v v v C v v v C v v v
```
```
CN C v v v C v v v
```
```
R C v i v v v
C v i v v v
C v v v iC
```
```
ψ
```
```
ψ ψ
β α
ψ β β
β β
β
```
### = + = +

### ʹ = + =

### =

### = > − > > +

### + > − > >=

### = > − 1 0 0

```
1 1 1 1 1 0 1 1 2
2
1 , 23 2 0 0 0 0 0 1 1 1
1 1 0 0 1 0 1 1 3
```
```
n |
cos | sin | |
```
( ) | cos | sin |

```
cos | sin | |
```
```
v v v
C v v v iC v v v
CN C v v v iC v v v
C v v v iC v v v
```
```
β
β β ψ
ψ β β
β β ψ
```
### > +

### + > − >= >

### ʹ >= > − > +

### + > − >= >


```
3 0 0 0 0 0 1 1 1
1 1 0 0 1 0 1 1
23 0 0 23
0 0 0 0 1 1 0 0
2 2 2 2
0 1
0 0 0 0 1 1 0 0
2
0 1
```
| cos | sin |
cos | sin |
: )| No more gates
cos | cos |
|
cos cos | |
cos | cos |

```
cos | |
```
```
a
```
```
C v v v iC v v v
C v v v iC v v v
M A v v
C v v v C v v v
```
```
C C
C v v v C v v v
```
```
C C
```
```
ψ β β
β β
```
```
β β
ψ
β β
β β
```
```
β
```
### >= > − > +

### + > − >

### >

### > + >

### >=

### +

### > + >

### =

### +

( )

```
2
```
### 0 | 0 1 | 1 | 0 0

```
= C v > + C v > ⊗ v v >
```

( )

```
3 0 0 0 0 0 1 1 1
1 1 0 0 1 0 1 1
```
```
23 1 1 23
0 1 1 1 1 0 1 1
```
(^22)
0 1
0 1 1 0 1 1
{| cos | sin |
cos | sin | }

### : )|

sin | sin |
|
sin | |

```
| | |
```
```
b
```
```
C v v v iC v v v
C v v v iC v v v
```
```
M B v v
iC v v v iC v v v
```
```
C C
```
```
C v C v v v
```
```
ψ β β
β β
```
```
β β
ψ
β
```
### >= > − > +

### + > − >

### >

### − > − >

### >= →

### +

### → > + > ⊗ >


( )

( )

( )

```
23 1 1 23
```
```
0 1 1 0 1 1
```
```
1 2 3 0 1 1 0 1 1
```
```
0 0 1 1 0 0
```
{ : ) | - Continued}

| | |

N N N | | |

| | |

_M B v v_

_C v C v v v_

_C v C v v v_

_C v C v v v_

>

> + > ⊗ >

ʹ ʹ ʹ > + > ⊗ >

= > + > ⊗ >


Adiabatic (Analog) Quantum

Computer


Ising Spin System

```
Hamiltonian:
```
```
0
1 , 1
```
```
,
```
```
L z L z z
B k k kn k n
k k n
```
```
H μ B σ J σ σ
= =
```
= −∑ + ∑

Many mathematical problems are equivalent
to the problem of the ground state
of the Ising spin system in the external magnetic field
with special values of local magnetic fields _Bk_ and the
interaction constants _J_ kn.


```
Example: Problem of Maximum
Independent Set (Graph Theory)
```
- Vertices: 1,2,3,4
- Edges (links): (1,2), (2,3), (2,4)
- Independent set of vertices:

(1,3), (1,4), (1,3,4), (3,4)

- Max independent set

(1,3,4)

### •

```
2
```
(^34)
1


Corresponding Ising Spin System

- Instead of 4 vertices we consider 4 spins.
- Uniform magnetic field: - **k** B.
- Instead of links we engineer the Ising interaction
    between the spins with J >> μBB > 0.
- Ising interaction is much greater than the
    interaction with the magnetic field (Zeeman
    interaction). The ground state:

```
J
```
```
J
```
```
J
```
```
1 2
```
```
B 3 4
```
```
Z
```

- In the ground state the maximum independent
    set corresponds to the set of spins in the state |
    0>
- Measuring the state of all the spins we obtain
    the maximum independent set (1,3,4).

```
J
```
```
J
```
```
J
```
```
1 2
```
```
B 3 4
```
```
Z
Ground
state:
ψ 0 = 0100
```

Lecture 12 Continued.


How to Get the Ground State?

- For a system of interacting qubits the initial state
    |ψi> is, normally, not the ground state |ψ 0 >.
- It takes a huge amount of time to evolve to the
    ground state in the Ising spin system. In
    classical physics researches use thermal
    annealing to obtain the state of the minimum
    energy.
- For a quantum system we need a “quantum
    annealing”.


Quantum Annealing

- 1. We change the initial Ising Hamiltonian H 0 by

```
applying a strong external magnetic field in the
transversal direction.
```
- 2. The ground state of the new Hamiltonian can
    be easily achieved.
- 3. When we slowly reduce the strong external
    field we return to the initial Hamiltonian H 0.
- 4. In many cases in the process of reduction of
    the additional field the qubits all the time remain
    in the ground state, so at the end they come to
    the ground state of H 0. 3


```
Adiabatic Theorem in Quantum
Mechanics
```
_A quantum system remains in its ground
state if the Hamiltonian changes slowly
enough so that_ **_all the time_** _there is the_
**_energy gap_** _between the ground state and
the first excited state._


Adiabatic Spin QC

- Strong magnetic field **B** 1 points along **the x-**

```
axis. Reducing B 1 one comes to the ground
state of the initial Hamiltonian. (The energy gap
remains non-zero all the time .)
```
```
B 1
```
```
x
```
(^12) μ _BB_ 1 >> _J_
3 4
( )
1
0 1 0
0
1 /
_L
B x
k
H H_ μ _B t t_ σ
−
=
= − ∑ −


The End of Lecture 12.


Summary of Lecture 12

- Phase gate.
- Grover’s gate.
- Grover’s algorithm for the search in the
    unsorted data.
- Steane’s algorithm for error correction.
- Ising spin system.
- Adiabatic quantum computation.


State-of-Art in Quantum

Computation

Physical Implementation of QC


```
Main Criteria for Physical
Implementation of the Universal
Quantum Computer
```
1. Scalable system of qubits
2. Initialization of qubits |00...0>
state
3. Long decoherence times (about
106 gate time)
4. Universal set of quantum gates
5. Qubit readout (single-qubit
measurement)


Superconducting Qubit

- Transmon


**Josephson junction
is a thin dielectric
layer between two
superconductors.**

```
Symbol for JJ
```
```
Brian Josephson, 1962:
tunneling of Cooper pairs
```

**Superconducting LC Circuit with JJ:
non-linear inductance of JJ makes energy**

**levels unequally spaced.**


Example: Niobium Transmon

Niobium: critical temperature 13
9.3 K


Transmon: Typical Parameters

- Dipole SC antenna of 1 mm length
- Dielectric layer about 100 nm
- f = 5 GHz
- 2-qubit gate time is about 50 ns
- Decoherence time is up to 500 μs


IBM Superconducting QC

- Record 1120 qubit quantum processor
- T. J. Watson Research Lab, in Yorktown
    Heights, about an hour’s drive from
    Manhattan.
- The whole IBM machine is called the
    Quantum System Two.
-


IBM Quantum System 2


Jay Gambetta – the Head of the IBM QC team


Adiabatic Superconducting

“Quantum” Computer

- D-Wave QC


```
D-Wave Systems
(Founded in Canada, in 1999)
```
- Geordie Rose, the Founder of D-Wave


- Currently, the only commercial quantum
    computer is an adiabatic quantum computer.
- Interaction between the superconducting qubits
    in D-Wave QC can be described as an effective
    Ising interaction.


```
Google and NASA operate with
D-Wave 2X (1152 qubits) in
```
NASA Ames Research Center in

California.


Ion Trap QC

```
+ +
```
```
1000 volts, trapped ions
10 MHz
```
```
end view
```
_V
x_

```
ti me
‘=’
```
```
Axial confinement by electrostatic (quadratic) potential.
Radial confinement by oscillating quadrupole potential.
```

```
QC-Market
```
- 1) Companies developing superconducting
    quantum processors:
- IBM, Google, Rigetti (California), ...
- Ion trap qubits: IonQ (Maryland), ...
- 2) Companies developing software for QC:
- Q-CTRL (Australia), Riverlane (England),...
- Website “quantum computingreport.com”:
- More than 100 start-ups around the globe.
- On the same website – jobs, news, ...


Quantum Communication


Photons

- Photons are the most convenient for
    quantum information and for experiments
    with the entanglement.


Polarized Light

**- E** = **n** yE 0 cos(ωt) – vertical
**- E** = **n** xE 0 cos(ωt) – horizontal
- 450 and - 45^0 :
**- E** = 2-1/2E 0 { **n** x + **n** y} cos(ωt)
**- E** = 2-1/2E 0 { **n** x - **n** y} cos(ωt)
- Circular polarization:

right-hand (counterclockwise)

**- E** = E 0 { **n** xcos(ωt) + **n** ysin(ωt)}

and left-hand (clockwise)

**- E** = E 0 { **n** xcos(ωt) - **n** ysin(ωt)}


Photon Polarization

- Polarization states of a photon:
- 1) Vertical and horizontal: |v> and |h>
- 2) 45^0 and -45^0 : |+> and |->)
- 3) Circular polarization:

Right-hand (counterclockwise) |R>

and left-hand (clockwise) |L>


Qubit Description

- 1) Standard basis.
- |0> and |1> → |v> and |h>
- 2) |v> - basis
- |v 0 > and |v 1 > →^ |+> and |->
- 3) |w> - basis
- |w 0 > and |w 1 > → |R> and |L>


**Security in Quantum**

**Communication**


Cryptography

- Initial information: plain text
- Information is encrypted with a key (password)
- Then decrypted

_Alice Bob_

```
key
```
```
information
classical channels
```
_Eve_


Symmetric Key.

- Classical example. **One Time Pad** :
- Addition modulo 2 for every couple of bit
    values.
- Alice:
- 01001 – plain text
- 11000 – key
- 10001 – encoded cipher:


Decription

- Bob:
- xxxxx – plain text - 01001
- 11000 – key
- 10001 – encoded cipher from Alice
- Main problem: **how to transfer a key?**


Ground Based QKD: Bennett and

Brassard (BB84)

```
Alice Bob
```
```
Mz
```
```
Mx
```
```
Mz
```
```
Mx
```
```
Mz
```
```
Mx
```
```
Photons
```
```
classical channel
```
_Eve_


```
34
```
Protocol for Alice and Bob

- I. Alice takes the first qubit
- 1. Alice randomly selects M (e.g. Mx)
- 2. Alice makes measurement of the state: (e.g. |
    v 0 >) and sends the qubit to Bob.
- The state |v 0 > corresponds to the value of the
    key λ 1 = 0.
- 3. Bob randomly selects M
- 4. Bob makes measurement
-


- Two possibilities:
- (A) Bob selects the same M as Alice
- → He obtains the same value λ 1.
- (B) Bob selects the other M


- II. Alice and Bob use a classical channel
- Alice and Bob inform each other about their M
    (but not about their outcome of measurement!)
- If Alice and Bob selected the same M they keep
    λ 1 as the first value of the key
- If not, then Alice and Bob discard the first value.
- III. Alice takes the second qubit and so on


BB84 and Eve

- Eve intercepts a qubit sent by Alice, randomly
    selects M, and sends the qubit to Bob.
- Success for Eve: she selects the same M as
    Alice and Bob
- →She obtains the same value λ 1.
- →She does not change the state of the qubit.
- →She does not corrupt communication between
    Alice and Bob and remains invisible.
- Probability of success = ½.


- For every bit accepted for the key by Alice
    and Bob the probability of success for Eve
    is ½.
- For a 20-bit key the probability of success
    for Eve is (1/2)^20 ≈ 10 -6!


Examples of Commercial Quantum

Communication

- ID Quantique (Swiss firm) sells commercial
    quantum encryption devices for Swiss
    banks.
- They transmit polarized photons along a
    fiber-optic cable by 110 km.


Commercial Quantum Networks

- Chinese state media:
- 1) The commercial quantum network based on
    fiber optics is operating in the province of
    Shandong.
- 2) 2000-km quantum communication network is
    operating between Shanghai and Beijing.
- The networks provide secure telephone and
    data communication.


Entanglement Based Quantum Key

Distribution (QKD)

- 1. Entangled photons are sent from the
    space station to the ground stations (to
    Alice and Bob)
- 2. Alice chooses a measurement basis and
    informs Bob about it.
- 3. Alice and Bob make measurement in the
    same basis: the same outcome for Alice
    and Bob.
- No chance for Eve.


Generation of Entangled Photons

```
42
```
```
Example. Parametric down-
conversion with a UV laser and
crystal
Barium Borate – BaB 2 O 4 (BBO)
in low temperature phase.
```


Alain Aspect, John Clauser and Anton Zeilinger have
won the 2022 Nobel Prize in Physics for experiments
with entangled photons.


Transmission of Entangled Photons

- Ground based transmission.
- Example:
- European Space Agency routinely
    transmits entangled photons over a
    distance of 144 km between the two
    Canary Islands.
- Losses: N = N 0 exp(-R/R 0 )
- R 0 is about 100 km.



- What about transmission of entangled
    photons in space?
**- The same,** but losses are much smaller:
- N = N 0 (R 0 /R)^2


```
Space Based Transmission of Entangled
Photons
```
In 2016 Chinese Academy of Science
launched the first quantum satellite with
nickname Micius (or Mozi, after the
ancient Chinese scientist Mo Di).
(m = 600 kg, h = 500 km)

The entangled photons were sent from
Micius to the ground stations separated
by more than 1000 kilometers (next
slide).



```
Intercontinental Quantum Key
Distribution
```
- A joint China-Austria team reported
    entanglement based quantum key
    distribution between the quantum satellite
    Micius and ground stations near Beijing and
    Vienna (7600 km).



```
First Intercontinental Quantum
Communication (2018)
```
- A picture of Micius (5.34 kB) was
    transmitted from Beijing to Vienna, and a
    picture of Schrödinger (4.9 kB) from
    Vienna to Beijing, using approximately 80
    kbit key with one-time-pad.


Quantum Teleportation


Basic Idea

```
Entangled
```
```
classical
channel
```

Quantum Circuit Diagram

```
⎧⎪ψ A
⎨
⎪⎩
```
_Alice_ :

```
Bob :
```
### H M

### M

```
σ z / 1 σ x /^1
```
```
classical
channel
```
```
Transfer of a qubit state
Absolutely secure transfer of information
```

```
0 1
```
```
0 0 1
```
```
0 0 0 1 1
12 0 0 0
```
```
1 1 1
```
```
1 1 0 0
```
```
1
```
| ( | 0 | 1 )

| ( | 0 | 1 ) (| 0 0 | 1 1 ) / 2

| ( | 000 | 011 | 100 | 111 ) / 2

| ( | 000 | 011

```
| 110 | 101 ) / 2 |
1
| [ (| 000 | 100 ) (| 011 | 111 )
2
(| 010 | 11
```
```
A
```
```
A A B A B
```
_C C_

_C C_

```
C C C C
CN C C
```
_C C_

_H C C_

_C_

```
ψ ψ ψ ψ ψ ψ
>= > + >
```
>= > + > ⊗ > + >

```
>= > + > + > + >
>= > + > +
```
+ > + > = >

>= > + > + > + > +

+ > − 0 >) + _C_ 1 (| 001 > − | 101 >)] =|ψ 2 >

Proof for M1,2→|00>


( )

```
2 0 0
```
```
1 1
1 , 2
```
```
0 1
```
(^322)
0 1
0 1
1
| [ (| 000 | 100 ) (| 011 | 111 )
2
(| 010 | 110 ) (| 001 | 101 )]
:| 00
| 000 | 001 / 2
|
/ 4 | | / 4
| 00 ( | 0 | 1 ) | 00 | _A
C C
C C
M
C C
C C
C C_
ψ
ψ
ψ
>= > + > + > + > +
+ > − > + > − >
>
> + >
>= =
+
= > ⊗ > + > = > ⊗ >


```
0 1
```
```
0 0 1
```
```
0 0 0 1 1
12 0 0 0
```
```
1 1 1
```
```
1 1 0 0
```
```
1
```
| ( | 0 | 1 )

| ( | 0 | 1 ) (| 0 0 | 1 1 ) / 2

| ( | 000 | 011 | 100 | 111 ) / 2

| ( | 000 | 011

```
| 110 | 101 ) / 2 |
1
| [ (| 000 | 100 ) (| 011 | 111 )
2
(| 010 | 11
```
```
A
```
```
A A B A B
```
_C C_

_C C_

```
C C C C
CN C C
```
_C C_

_H C C_

_C_

```
ψ ψ ψ ψ ψ ψ
>= > + >
```
>= > + > ⊗ > + >

```
>= > + > + > + >
>= > + > +
```
+ > + > = >

>= > + > + > + > +

+ > − 0 >) + _C_ 1 (| 001 > − | 101 >)] =|ψ 2 >

Proof for M1,2→|01>


( )

```
2 0 0
```
```
1 1
1 , 2
```
```
0 1
```
(^322)
0 1
0 1
3
3 4 0 1
1
| [ (| 000 | 100 ) (| 011 | 111 )
2
(| 010 | 110 ) (| 001 | 101 )]
:| 01
| 011 | 010 / 2
|
/ 4 | | / 4
| 01 ( | 1 | 0 )
Bob applies gate:
| | 01 ( | 0 | 1 ) | 01 |
_x
x A
C C
C C
M
C C
C C
C C
C C_
ψ
ψ
σ
σ ψ ψ
>= > + > + > + > +
+ > − > + > − >
>
> + >
>= =
+
= > ⊗ > + >
>= > ⊗ > + > = > ⊗ >


Ground-Based Teleportation

- NIST, Colorado:
- Quantum teleportation of a photon state by
    a distance of about 100 km using an
    optical fiber.


Space-Based Teleportation

- Micius team reported quantum
    teleportation of single-photon qubits from
    the ground to satellite with a distance up to
    **1400 km**.


- Details.
- To perform the experiment, the team
    created entangled pairs of photons on the
    ground at a rate of about **4,000 per**
    **second**.
-
- They beamed one of the entangled
    photons to the satellite and then perform
    teleportation.


```
Another Application of the
Entanglement: Quantum Radar
```
The simplest theoretical scenario.

1. You wish to verify if there is a reflecting object in
some direction (θ,φ) and if “yes” find the distance to
the object. Assume for simplicity that the frequency
and polarization of a photon do not change after
reflection.
2. You can send a bunch of photons with various
frequencies. Example: photons a, b, c, ... with
frequencies fa, fb, ...). If there is a reflecting object

some of these photons will be reflected back to you.

-

```
63
```

- 3. There are bunches of thermal photons from
    other directions. Also, your adversary may wish
    to deceive you by sending its own photons from
    another direction. How to distinguish your
    reflected photons from the false photons?
- 4. The absolutely secure way to distinguish your
    photons from the false ones is to use a quantum
    radar. The idea is the following. Every traveling
    photon “ptk” with the frequency fk is in the
    entangled state with the corresponding “ home
    photon” phk of the same frequency fk which you
    keep in your resonator.


- 5. If you receive a bunch of photons you
    measure the state of an arriving and the
    corresponding home photons of the same
    frequency in an arbitrary basis. You use different
    measurement bases for different pairs. The
    outcome of the measurement for entangled
    pairs must be the same in any basis.


```
Media Speculations about Quantum
Radar
```
- In 2016 China’s state media reported
    creation of the first quantum radar.
-
- “The radar can detect objects at a range of
    up to 62 miles.”
- (Standard radar – up to 200 miles)


- Thank you for Taking this Course!
- Please, do not forget to send me your
    presentation before 12/11.
- See you on Wednesday, 12/11.
- Now, instead of quiz, please submit evaluation
    of this course.
- Have a Good Winter Break!.


