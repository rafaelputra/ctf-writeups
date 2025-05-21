# LLIR

> Checker? I hardly know her!

Diberikan file checker.ll yang kemungkinan ini adalah Intermediate Representation (IR) dari LLVM. Langsung saja buka mainnya.

```c
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [64 x i8], align 16
  store i32 0, ptr %1, align 4
  %3 = call i32 (ptr, ...) @printf(ptr noundef @.str.1)
  %4 = call i32 (ptr, ...) @printf(ptr noundef @.str.2)
  %5 = call i32 (ptr, ...) @printf(ptr noundef @.str.3)
  %6 = getelementptr inbounds [64 x i8], ptr %2, i64 0, i64 0
  %7 = load ptr, ptr @stdin, align 8
  %8 = call ptr @fgets(ptr noundef %6, i32 noundef 64, ptr noundef %7)
  %9 = getelementptr inbounds [64 x i8], ptr %2, i64 0, i64 0
  %10 = call i32 @checker_i_hardly_know_her(ptr noundef %9)
  %11 = icmp ne i32 %10, 0
  br i1 %11, label %12, label %14
```

Terdapat call function checker_i_hardly_know_her, setelah dibuka memiliki alur logika yang panjang, langsung saja compile ke binary.

`$ clang checker.ll -o checker`

Lanjut decompile menggunakan IDA

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char s[76]; // [rsp+0h] [rbp-50h] BYREF
  int v5; // [rsp+4Ch] [rbp-4h]

  v5 = 0;
  printf("Welcome to this totally normal flag checkern\n");
  printf("We're going to use a little bit of a different compiler tho\n");
  printf("Ever heard of clang? What makes it different than gcc?\n");
  fgets(s, 64, stdin);
  if ( (unsigned int)checker_i_hardly_know_her(s) )
  {
    printf("You win!!\n");
    return 0;
  }
  else
  {
    printf("Womp womp\n");
    return 1;
  }
}
```

Program akan meminta input kita lalu input kita diproses dalam fungsi checker_i_hardly_know_her.

```c
_BOOL8 __fastcall checker_i_hardly_know_her(const char *a1)
{
  bool v2; // [rsp+7h] [rbp-9h]

  v2 = 0;
  if ( a1[4] == a1[14] )
  {
    v2 = 0;
    if ( a1[14] == a1[17] )
    {
      v2 = 0;
      if ( a1[17] == a1[23] )
      {
        v2 = 0;
        if ( a1[23] == a1[25] )
        {
          v2 = 0;
          if ( a1[9] == a1[20] )
          {
            v2 = 0;
            if ( a1[10] == a1[18] )
            {
              v2 = 0;
              if ( a1[11] == a1[15] )
              {
                v2 = 0;
                if ( a1[15] == a1[24] )
                {
                  v2 = 0;
                  if ( a1[24] == a1[31] )
                  {
                    v2 = 0;
                    if ( a1[31] == a1[27] )
                    {
                      v2 = 0;
                      if ( a1[13] == a1[26] )
                      {
                        v2 = 0;
                        if ( a1[16] == a1[29] )
                        {
                          v2 = 0;
                          if ( a1[19] == a1[28] )
                          {
                            v2 = 0;
                            if ( a1[28] == a1[32] )
                            {
                              v2 = 0;
                              if ( a1[36] == 125 )
                              {
                                v2 = 0;
                                if ( a1[6] == 123 )
                                {
                                  v2 = 0;
                                  if ( a1[8] == a1[7] - 32 )
                                  {
                                    v2 = 0;
                                    if ( !strncmp(a1, "byuctf", 6uLL) )
                                    {
                                      v2 = 0;
                                      if ( a1[20] + a1[9] == a1[31] + 3 )
                                      {
                                        v2 = 0;
                                        if ( a1[31] + 3 == *a1 )
                                        {
                                          v2 = 0;
                                          if ( a1[10] == a1[7] + 6 )
                                          {
                                            v2 = 0;
                                            if ( a1[8] == a1[9] + 27 )
                                            {
                                              v2 = 0;
                                              if ( a1[12] == a1[13] - 1 )
                                              {
                                                v2 = 0;
                                                if ( a1[13] == a1[10] - 3 )
                                                {
                                                  v2 = 0;
                                                  if ( a1[10] == a1[16] - 1 )
                                                  {
                                                    v2 = 0;
                                                    if ( a1[16] == a1[14] - 1 )
                                                    {
                                                      v2 = 0;
                                                      if ( a1[35] == a1[5] - 2 )
                                                      {
                                                        v2 = 0;
                                                        if ( a1[5] == a1[21] - 1 )
                                                        {
                                                          v2 = 0;
                                                          if ( a1[21] == a1[22] - 1 )
                                                          {
                                                            v2 = 0;
                                                            if ( a1[22] == 2 * a1[28] )
                                                            {
                                                              v2 = 0;
                                                              if ( a1[33] == a1[32] + 1 )
                                                              {
                                                                v2 = 0;
                                                                if ( a1[32] + 1 == a1[34] - 3 )
                                                                  return a1[30] == a1[7] + 1;
                                                              }
                                                            }
                                                          }
                                                        }
                                                      }
                                                    }
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return v2;
}
```

Terdapat komparasi per-karakter input yang sangat panjang. Lanjut saja gunakan z3 solver.

```python
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
```

Didapatkan flagnya byuctf{lL1r_not_str41ght_to_4sm_458d}