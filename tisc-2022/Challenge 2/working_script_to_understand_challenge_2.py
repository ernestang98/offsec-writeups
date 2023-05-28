import numpy as np

SECRET_KEY = np.round(np.random.rand(8,8)).astype("int")
print(SECRET_KEY)

def func1(s):
    return np.fromiter(list(s), dtype="int").reshape(8,1)

for i in range(8):
    input_vector = input("give me stuff:\n")
    input_vector = func1(input_vector)
    print(SECRET_KEY @ input_vector)
    output_vector = (SECRET_KEY @ input_vector) & 1 # if odd then 1 if even then 0
    print(output_vector)


# based on their input vector, i need to know the secret key so that i can predict the final vector

"""
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

[0 1 1 0 0 1 1 0]
[0 0 0 1 1 1 0 1]
[1 1 1 1 1 1 1 1]
[0 1 0 1 0 0 0 1]
[0 1 1 0 1 1 1 1]
[1 1 0 1 0 1 1 0]
[0 1 0 1 0 1 1 1]
[0 0 1 1 1 0 0 0]

# TISC{d0N7_R0lL_Ur_0wN_cRyp70_7a25ee4d777cc6e9}
# https://stackoverflow.com/questions/27385633/what-is-the-symbol-for-in-python
# https://docs.microsoft.com/en-us/cpp/cpp/bitwise-and-operator-amp?view=msvc-170
"""
