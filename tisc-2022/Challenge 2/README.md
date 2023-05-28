# Solution

Based on the "whitepaper" given, the cryptographic function to crack generates an 8 x 8 matrix made up of zero and ones. We then provide 8 inputs to which the server performs a matrix multiplication before performing a bitwise AND multiplication on the eventual 8 x 1 matrix. After this, the server will issue 8 inputs and we are supposed to (by now) crack the 8 x 8 matrix and perform the matrix multiplication and bitwise AND operation and match the output. 

Example scenario:

```
[x x x x x x x x]
[x x x x x x x x]
[x x x x x x x x]
[x x x x x x x x]
[x x x x x x x x]
[x x x x x x x x]
[x x x x x x x x]
[x x x x x x x x]

Challenge Me #01 <-- 10000000
My Response --> 00100100
Challenge Me #02 <-- 01000000
My Response --> 10111110
Challenge Me #03 <-- 00100000
My Response --> 10101001
Challenge Me #04 <-- 00010000
My Response --> 01110111
Challenge Me #05 <-- 00001000
My Response --> 01101001
Challenge Me #06 <-- 00000100
My Response --> 11101110
Challenge Me #07 <-- 00000010
My Response --> 10101110
Challenge Me #08 <-- 00000001
My Response --> 01111010
```

- By sending `10000000` and receiving `00100100`, we know that row 1 column 1 must be a 0 as the matrix multiplication of row 1 with `10000000` must add up to an even number/must be 0.

- By sending `10000000` and receiving `00100100`, we know that row 2 column 1 must be a 0 as the matrix multiplication of row 1 with `10000000` must add up to an even number/must be 0.

- By sending `10000000` and receiving `00100100`, we know that row 3 column 1 must be a 1 as the matrix multiplication of row 1 with `10000000` must add up to an odd number.

- Continue this process until you crack the entire matrix and solve the challenge

- You can automate this process using a python script along with libraries such as socket or pwntools but I did it manually (lol).

### Flag: 

TISC{d0N7_R0lL_Ur_0wN_cRyp70_7a25ee4d777cc6e9}

### References

1. https://stackoverflow.com/questions/27385633/what-is-the-symbol-for-in-python

2. https://docs.microsoft.com/en-us/cpp/cpp/bitwise-and-operator-amp?view=msvc-170
