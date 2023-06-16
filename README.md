# :zap: **Medsafe Cycle API for ML** :zap:
<br>

| ID                 | Name                      | University                               |
|--------------------|---------------------------|------------------------------------------|
| (ML) M166DSX0038   | Riski Dwi Pangestu        | Universitas Diponegoro                   |
| (ML) M309DSY0297   | Itatri Lestari            | Universitas Pendidikan Indonesia         |
| (CC) C151DSX1371   | Amry Yahya                | Universitas Brawijaya                    |
| (CC) C038DSX0821   | Muhammad Firdho Kustiawan | Institut Teknologi Sepuluh Nopember      |
| (MD) A181DSY1252   | Agnes Audya Tiara P       | Universitas Indonesia                    |
| (MD) A181DSY1169   | Avelia Diva Zahra         | Universitas Indonesia                    |



# :large_blue_circle: **Creating a Bucket in Google Cloud Storage** :large_blue_circle:

### :triangular_flag_on_post: **Things to be aware of before creating a bucket**
1. Make sure your account permissions as the project owner
2. Verify that the Google Cloud project is correct
<br>

### :rocket: **Steps**
1. Go to page [Google Cloud Storage > Bucket](https://console.cloud.google.com/storage/browser?project=medsafe-cycle&prefix=&forceOnBucketsSortingFiltering=true)
    <img src="./images/1.png">

2. Click create
    <img src="./images/2.png">

3. In **Name your bucket**, fill in the bucket name according to[criteria](https://cloud.google.com/storage/docs/buckets#naming) dan klik continue
    <img src="./images/3.png">

4. In **Choose where to store your data**, select the type of location and the location where the bucket data will be stored. In this section, we choose the type of region location with the location in asia-southeast2 (Jakarta) then click continue
    <img src="./images/4.png">

5. In **Choose a storage class for your data**, leave it at default without changing anything
    <img src="./images/5.png">

6.  In **Choose how to control access to objects**, leave it at default without anything being changed
    <img src="./images/6.png">

7. In **Choose how to protect object data**, leave it at default without anything being changed
    <img src="./images/7.png">

8. Click create and wait a few moments until the bucket is ready to use
<br><br>

# :large_blue_circle: **Uploading ML models to Bucket** :large_blue_circle:

### :rocket: **Steps**
1. Click the name of the bucket that was created

2. Click upload file and select the ML model you want to upload or you can drag and drop it on the page
    <img src="./images/8.png">
<br><br>

# :large_blue_circle: **Creating a Service Account** :large_blue_circle:

### :triangular_flag_on_post: **Things to consider before creating a service account**
1. Make sure you have [enabled IAM API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https:%2F%2Fconsole.cloud.google.com&_ga=2.171097632.1699224504.1686877784-154771683.1686205328&_gac=1.255542778.1686233180.CjwKCAjw-IWkBhBTEiwA2exyO87jxN04QVtScc_sA9xKaOOdhpO1ei0fFxkzeM74GMqI3K2qkXyKlxoChXwQAvD_BwE)
<br>

### :rocket: **Steps** 
1. Go to page [IAM & Admin > Service Accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts/create?walkthrough_id=iam--create-service-account&_ga=2.68735121.1699224504.1686877784-154771683.1686205328&_gac=1.113394421.1686233180.CjwKCAjw-IWkBhBTEiwA2exyO87jxN04QVtScc_sA9xKaOOdhpO1ei0fFxkzeM74GMqI3K2qkXyKlxoChXwQAvD_BwE#step_index=1) and select the desired Google Cloud project
    <img src="./images/9.png">

2. Click create
    <img src="./images/10.png">

3. In **Service account details**, fill in the name of the service account as desired. Then click create and continue
    <img src="./images/11.png">

4. In **Grant this service account access to project**, select the role as needed and click continue. In this case we chose the Storage Object Admin role
    <img src="./images/12.png">

4. In **Grant users access to this service account**, leave it at default without changing anything and click done
    <img src="./images/13.png">
<br><br>

# :large_blue_circle: **Downloading the Service Account Key** :large_blue_circle:

### :rocket: **Steps**
1. Click the service account that was created

2. Click the keys tab
    <img src="./images/14.png">

2. Click add key > create new key 
    <img src="./images/15.png">

2. Select the JSON type then click create then the key will automatically be downloaded automatically
    <img src="./images/16.png">
<br><br>

# :large_blue_circle: **Creating App Engine Applications** :large_blue_circle:

### :triangular_flag_on_post: **Things to be aware of before making**
1. Verify that the Google Cloud project is correct
<br>

### :rocket: **Steps**
1. Go to page [App Engine](https://console.cloud.google.com/appengine/start?) and select the desired Google Cloud project. Then click create application and wait a few minutes
    <img src="./images/17.png">

2. In the region section select asia-southeast2 and select a service account select App Engine default service account then click next
    <img src="./images/18.png">

2. Click I'll do this letter and App Engine is ready to use
    <img src="./images/19.png">
<br><br>

# :large_blue_circle: **Clone the Github API Repository** :large_blue_circle:

### :rocket: **Steps**
1. Activate cloud shell and click open editor
    <img src="./images/20.png">

2. Then clone this github repository with the following command
    ```JavaScript
    git clone https://github.com/firdh0/Medsafe-Cycle.git
    ```

3. Install the required requirements with the following command
     ```JavaScript
    pip install -r requirements.txt
    ```
<br><br>

# :large_blue_circle: **Configuring files** :large_blue_circle:

### :rocket: **Configure app.yaml**
Configure the following sections according to your project

```JavaScript
...
# according to the name used
env_variables:
    CREDENTIALS: 'medsafe-cycle-api-ml.json'
    BUCKET_NAME: 'medsafe-cycle-ml'
    MODEL_PATH: 'capstone.h5'
    FLASK_ENV: 'production'
```

### :rocket: **Configure model.py**
Configure the following sections according to your project

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

### :rocket: **Configure Service Account Key**
Replace the key in the `medsafe-cycle-api-ml.json` file with the key that was downloaded from the service account that was created
<br><br>

# :large_blue_circle: **Deploying Files to App Engine** :large_blue_circle:

### :rocket: **Steps**
1. In the open editor, click Terminal > New Terminal
2. Enter the directory to be deployed with the following command
    ```JavaScript
    cd foldername
    ```
3. Deploy with the following command
    ```JavaScript
    gcloud app deploy
    ```
4. Type Y and wait a few moments until a link that has been created automatically appears to access it

# :large_blue_circle: **Endpoint For Prediction** :large_blue_circle:

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
