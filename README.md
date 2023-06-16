# :zap: **Medsafe Cycle API for ML** :zap:
<br>

# :large_blue_circle: **Membuat Bucket di Google Cloud Storage** :large_blue_circle:

### :triangular_flag_on_post: **Hal yang harus diperhatikan sebelum membuat bucket** 
1. Pastikan permission akun anda sebagai project owner
2. Pastikan Google Cloud project sudah benar
<br>

### :rocket: **Langkah-langkah** 
1. Pergi ke halaman [Google Cloud Storage > Bucket](https://console.cloud.google.com/storage/browser?project=medsafe-cycle&prefix=&forceOnBucketsSortingFiltering=true)
    <img src="./images/1.png">

2. Klik create
    <img src="./images/2.png">

3. Pada **Name your bucket**, isikan nama bucket sesuai [kriteria](https://cloud.google.com/storage/docs/buckets#naming) dan klik continue
    <img src="./images/3.png">

4. Pada **Choose where to store your data**, pilih jenis lokasi dan lokasi tempat data bucket akan disimpan. Pada bagian ini kami memilih jenis lokasi region dengan lokasi tempatnya di asia-southeast2 (Jakarta) kemudian klik continue
    <img src="./images/4.png">

5. Pada **Choose a storage class for your data**, biarkan secara default tanpa ada yang diubah
    <img src="./images/5.png">

6. Pada **Choose how to control access to objects**, biarkan secara default tanpa ada yang diubah
    <img src="./images/6.png">

7. Pada **Choose how to protect object data**, biarkan secara default tanpa ada yang diubah
    <img src="./images/7.png">

7. Klik create dan tunggu beberapa saat hingga bucket siap digunakan
<br><br>

# :large_blue_circle: **Mengupload model Machine Learning ke Bucket** :large_blue_circle:

### :rocket: **Langkah-langkah** 
1. Klik nama bucket yang telah dibuat

2. Klik upload file dan pilih model ML yang ingin diupload atau bisa dengan cara drag dan drop pada page tersebut
    <img src="./images/8.png">
<br><br>

# :large_blue_circle: **Membuat Service Account** :large_blue_circle:

### :triangular_flag_on_post: **Hal yang harus diperhatikan sebelum membuat service account** 
1. Pastikan telah [mengaktifkan IAM API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https:%2F%2Fconsole.cloud.google.com&_ga=2.171097632.1699224504.1686877784-154771683.1686205328&_gac=1.255542778.1686233180.CjwKCAjw-IWkBhBTEiwA2exyO87jxN04QVtScc_sA9xKaOOdhpO1ei0fFxkzeM74GMqI3K2qkXyKlxoChXwQAvD_BwE)
<br>

### :rocket: **Langkah-langkah** 
1. Pergi ke halaman [IAM & Admin > Service Accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts/create?walkthrough_id=iam--create-service-account&_ga=2.68735121.1699224504.1686877784-154771683.1686205328&_gac=1.113394421.1686233180.CjwKCAjw-IWkBhBTEiwA2exyO87jxN04QVtScc_sA9xKaOOdhpO1ei0fFxkzeM74GMqI3K2qkXyKlxoChXwQAvD_BwE#step_index=1) dan pilih Google Cloud project yang diinginkan
    <img src="./images/9.png">

2. Klik create
    <img src="./images/10.png">

3. Pada **Service account details**, isikan nama service account sesuai keinginan. Kemudian klik create and continue
    <img src="./images/11.png">

4. Pada **Grant this service account access to project**, pilih role sesuai kebutuhan dan klik continue. Dalam hal ini kami memilih role Storage Object Admin
    <img src="./images/12.png">

4. Pada **Grant users access to this service account**, biarkan secara default tanpa ada yang diubah dan klik done
    <img src="./images/13.png">
<br><br>

# :large_blue_circle: **Mengunduh Key Service Account Yang Telah Dibuat** :large_blue_circle:

### :rocket: **Langkah-langkah** 
1. Klik service account yang telah dibuat

2. Klik tab keys
    <img src="./images/14.png">

2. Klik add key > create new key 
    <img src="./images/15.png">

2. Pilih tipenya JSON kemudian klik create maka secara otomatis key tersebut akan terdownload secara otomatis
    <img src="./images/16.png">
<br><br>

# :large_blue_circle: **Membuat Aplikasi App Engine** :large_blue_circle:

### :triangular_flag_on_post: **Hal yang harus diperhatikan sebelum membuat** 
1. Pastikan Google Cloud project sudah benar
<br>

### :rocket: **Langkah-langkah** 
1. Pergi ke halaman [App Engine](https://console.cloud.google.com/appengine/start?) dan pilih Google Cloud project yang diinginkan. Kemudian klik create application dan tunggu beberapa menit
    <img src="./images/17.png">

2. Pada bagian region pilih asia-southeast2 dan select a service account pilih App Engine default service account kemudian klik next
    <img src="./images/18.png">

2. Klik I'll do this letter dan App Engine siap digunakan
    <img src="./images/19.png">
<br><br>

# :large_blue_circle: **Mengclone Repository API Github** :large_blue_circle:

### :rocket: **Langkah-langkah** 
1. Aktifkan cloud shell dan klik open editor
    <img src="./images/20.png">

2. Kemudian clone repository github ini dengan perintah berikut
    ```JavaScript
    git clone https://github.com/firdh0/Medsafe-Cycle.git
    ```

3. Install requirements yang dibutuhkan dengan perintah berikut
     ```JavaScript
    pip install -r requirements.txt
    ```
<br><br>

# :large_blue_circle: **Mengkonfigurasi file** :large_blue_circle:

### :rocket: **Konfigurasi app.yaml** 
Konfigurasi bagian berikut sesuai project anda

```JavaScript
...
# according to the name used
env_variables:
    CREDENTIALS: 'medsafe-cycle-api-ml.json'
    BUCKET_NAME: 'medsafe-cycle-ml'
    MODEL_PATH: 'capstone.h5'
    FLASK_ENV: 'production'
```

### :rocket: **Konfigurasi model.py** 
Konfigurasi bagian berikut sesuai project anda

```JavaScript
...
PROJECT_NAME = 'medsafe-cycle'
CREDENTIALS = 'medsafe-cycle-api-ml.json'
BUCKET_NAME = 'medsafe-cycle-ml'
MODEL_PATH = 'capstone.h5'

MODEL_FILE_PATH = "capstone.h5"
...

def predictions(image_path):
    ...
    # Adjust to the size of the uploaded image
    target_size = (256, 256)  
    ...
    # According to the prediction category used
    class_names = ['Sitoktoksik', 'Infeksius', 'Patologis', 'Farmasi']
```

### :rocket: **Konfigurasi Service Account Key** 
Ganti key pada file `medsafe-cycle-api-ml.json` dengan key yang telah didownload dari service account yang telah dibuat
<br><br>

# :large_blue_circle: **Mendeploy File ke App Engine** :large_blue_circle:

### :rocket: **Langkah-langkah** 
1. Pada open editor, klik Terminal > New Terminal
2. Masuk ke direktori yang akan dideploy dengan perintah berikut
    ```JavaScript
    cd foldername
    ```
3. Deploy dengan perintah berikut
    ```JavaScript
    gcloud app deploy
    ```
4. Ketik Y dan tunggu beberapa saat hingga muncul link yang telah dibuat secara otomatis untuk mengaksesny

# :large_blue_circle: **Endpoint Untuk Prediksi** :large_blue_circle:

### :rocket: **Base_URL** 
```JavaScript
https://medsafe-cycle.et.r.appspot.com
```

### :rocket: **Endpoint Base_URL** 
- Method: GET
- Endpoint: {{baseurl}}
- Body Request: -
- Authorization: -
- Example response:
    ```JavaScript
    {
        "message": "Hello, flask!!",
        "status": 200
    }
    ```

### :rocket: **Endpoint Base_URL/medicalWaste** 
- Method: GET
- Endpoint: {{baseurl}}/medicalWaste
- Body Request: -
- Authorization: -
- Example response:
    ```JavaScript
    {
        "message": "Endpoint called",
        "status": 200
    }
    ```

### :rocket: **Endpoint Base_URL/medicalWaste** 
- Method: POST
- Endpoint: {{baseurl}}/medicalWaste
- Body Request: image file
- Authorization: -
- Example response:
    ```JavaScript
    {
        "data": {
            "category": "Sitoktoksik",
            "probability": 0.7832920551300049
        },
        "message": "Success",
        "status": 200
    }
    ```
