flag = [12838, 1089, 16029, 13761, 1276, 14790, 2091, 17199, 2223, 2925, 
          17901, 3159, 18135, 18837, 3135, 19071, 4095, 19773, 4797, 4085, 
          20007, 5733, 20709, 17005, 2601, 9620, 3192, 9724, 3127, 8125]

MOD = 256
BASE = 3

key = list(set([pow(BASE, i, MOD) for i in range(MOD)]))[3:len(flag)+3]

flag_decode = ''.join([chr(i // j) for i, j in zip(flag, key)])
print(flag_decode)