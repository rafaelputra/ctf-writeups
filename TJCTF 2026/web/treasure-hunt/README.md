# tresure-hunt

> Let's go hunt down some treasure! The flag is split into 4 parts. I'll give you the first one right here: tjctf<br><br>treasure-hunt.tjc.tf

Pada challenge ini peserta tidak diberikan source code, ketika halaman web-nya dibuka, isinya sangat sederhana.

```html

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/styles.css">
    <title>Pirates!</title>
</head>

<body>
    <h1>Learn about pirates!</h1>
    <h2>Wow!</h2>
    <form method="POST">
        <input type="submit" value="Learn More">
    </form>
    <img src="/static/ship.png" alt="ship">
    <p hidden>_and_</p>
</body>
</html>
```

Terdapat tag p dengan atribut hidden yang berisi nilai "_and_", mungkin ini bagian dari flagnya. Kita perlu mencari sisanya.

Coba cek pada robots.txt

```
User-agent: *
Disallow: /gold-coffer
Allow: /
```

Terdapat direktori /gold-coffer yang di set disallow, ketika direktori tersebut dibuka kita dapatkan potongan flag "g0ld}"

Selanjutnya kita coba lihat cookies dari devtools, didapatkan potongan flag terakhir "{s1lv3r"

Flag: tjctf{silver_and_gold}