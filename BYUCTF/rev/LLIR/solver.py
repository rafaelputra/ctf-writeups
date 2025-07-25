from z3 import *

a1 = [BitVec(f'a1_{i}', 8) for i in range(37)]

s = Solver()
for ch in a1:
    s.add(ch >= 32, ch <= 126)

s.add(a1[4] == a1[14])
s.add(a1[14] == a1[17])
s.add(a1[17] == a1[23])
s.add(a1[23] == a1[25])
s.add(a1[9] == a1[20])
s.add(a1[10] == a1[18])
s.add(a1[11] == a1[15])
s.add(a1[15] == a1[24])
s.add(a1[24] == a1[31])
s.add(a1[31] == a1[27])
s.add(a1[13] == a1[26])
s.add(a1[16] == a1[29])
s.add(a1[19] == a1[28])
s.add(a1[28] == a1[32])
s.add(a1[36] == ord('}'))
s.add(a1[6] == ord('{'))
s.add(a1[8] == a1[7] - 32)
s.add(a1[0] == ord('b'))
s.add(a1[1] == ord('y'))
s.add(a1[2] == ord('u'))
s.add(a1[3] == ord('c'))
s.add(a1[4] == ord('t'))
s.add(a1[5] == ord('f'))
s.add(a1[20] + a1[9] == a1[31] + 3)
s.add(a1[31] + 3 == a1[0])
s.add(a1[10] == a1[7] + 6)
s.add(a1[8] == a1[9] + 27)
s.add(a1[12] == a1[13] - 1)
s.add(a1[13] == a1[10] - 3)
s.add(a1[10] == a1[16] - 1)
s.add(a1[16] == a1[14] - 1)
s.add(a1[35] == a1[5] - 2)
s.add(a1[5] == a1[21] - 1)
s.add(a1[21] == a1[22] - 1)
s.add(a1[22] == 2 * a1[28])
s.add(a1[33] == a1[32] + 1)
s.add(a1[32] + 1 == a1[34] - 3)
s.add(a1[30] == a1[7] + 1)

if s.check() == sat:
    m = s.model()
    flag = ''.join([chr(m[ch].as_long()) for ch in a1])
    print("Flag:", flag)