# u

> u

Diberikan file u.py yang berisi source code python yang di obfuscate.

```python
ù,ú,û,ü,ũ,ū,ŭ,ů,ű,ų,ṳ,ṷ,ụ=chr,ord,abs,input,all,print,len,input,pow,range,list,dict,set;ù=[12838,1089,16029,13761,1276,14790,2091,17199,2223,2925,17901,3159,18135,18837,3135,19071,4095,19773,4797,4085,20007,5733,20709,17005,2601,9620,3192,9724,3127,8125];u,U=3,256;ṷ=ü();ʉ=ṳ(ụ([ű(u,û,U) for û in(ų(U))]))[u:ŭ(ù)+u];ṳ=zip;ṷ=[ú(û) for û in(ṷ)];assert(ŭ(ù)==ŭ(ṷ));assert(ũ([û*ü==ū for û,ü,ū in(ṳ(ʉ,ṷ,ù))]));
```

Coba rename beberapa fungsi agar source code mudah dibaca

```python
flag = [12838,1089,16029,13761,1276,14790,2091,17199,2223,2925,17901,3159,18135,18837,3135,19071,4095,19773,4797,4085,20007,5733,20709,17005,2601,9620,3192,9724,3127,8125];

u,U = 3,256;

user_input = input();

key = list(set([pow(u, abs(i), U) for i in(range(U))]))[u:len(flag)+u];

process_input = [ord(i) for i in (user_input)]

assert(len(flag)==len(process_input));

assert(all([i * j == k for i, j, k in zip(key, process_input, flag)]))

```

Source codenya sederhana, terdapat macam-macam huruf Unicode (ù, ú, dst) yang di assign ke beberapa fungsi di python seperti chr, ord, abs, dan lain-lain.

Baris pertama terdapat list hasil encode yang kemungkinan itu adalah flagnya, lanjut ke variabel key yang berisi pembentukan key, terdapat looping fungsi `pow(x, y, z)` (berarti x^y % z), sehingga terjadi operasi modulo dengan u sebagai base, U sebagai mod, dan i sebagai range dari mod, kemudian dengan menggunakan fungsi set maka hasil operasi dengan nilai yang sama (duplikat) akan dihapus, setelahnya dimasukkan ke array dan diakses hanya pada rentang index `u` (3) hingga `len(flag)+u` (33)

Lanjut pada process_input di mana input dari pengguna akan di konversi menjadi integer (unicode) dengan fungsi ord.

Lalu dilakukan pengecekan kondisi len(flag) == len(process_input), dan dilakukan perulangan operasi perkalian integer antara key dengan input yang dicocokkan dengan flag. Tinggal bikin solver buat balikin fungsinya dengan cara membagi deretan list flag dengan key.

```python
flag = [12838, 1089, 16029, 13761, 1276, 14790, 2091, 17199, 2223, 2925, 
          17901, 3159, 18135, 18837, 3135, 19071, 4095, 19773, 4797, 4085, 
          20007, 5733, 20709, 17005, 2601, 9620, 3192, 9724, 3127, 8125]

MOD = 256
BASE = 3

key = list(set([pow(BASE, i, MOD) for i in range(MOD)]))[3:len(flag)+3]

flag_decode = ''.join([chr(i // j) for i, j in zip(flag, key)])
print(flag_decode)
```

Didapatkan flagnya byuctf{uuuuuuu_uuuu_uuu_34845}