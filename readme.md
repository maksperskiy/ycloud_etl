<div align="center">
  <h1>Currencies ETL using Yandex Cloud</h1>
</div>

<br />

## Table of Contents

- [About the Project](#about-the-project)
  * [About the Solution](#about-the-solution)
  * [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Postman collection](#postman-collection)
- [Usage](#usage)
  

## About the Project
Project provides endpoints to collect currency rates from CBR API to the Postgre database manually for given date and periodically every day for current date and returns currency rates from database for given date.

### About the Solution

There is one Cloud Function was creted to solve this task:
 - Import currencies - sends request to CBR API with given date to get currency rates and insert them in created table. This function is called periodically by Timer trigger.
Also, API was written with FastAPI Python framework and provides two functional endpoints:
 - Get currencies - Returns currency rates for given date. (Today by default)
 - Import currencies - Calls Yandex Cloud Function to import currencies into database for gived date. (Today by default)



### Tech Stack

<details>
  <summary>Yandex Cloud</summary>
  <ul>
    <li><a href="https://cloud.yandex.ru/services/functions/">Cloud Functions</a></li>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://cloud.yandex.ru/services/managed-postgresql/">Managed Service for PostgreSQL</a></li>
    <li><a href="https://cloud.yandex.ru/docs/functions/operations/trigger/timer-create/">Timer trigger</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <a href="https://www.postgresql.org/">PostgreSQL</a>
</details>


## Getting Started


### Prerequisites

1. Upload source code in the **Cloud Function** you need to make zip file with source code starting **bash** script: 

```bash
 make zip
```

2. Create Service account that will invoke this function.

### Installation

1. Create Cloud Functions 

<img src="docs/images/create_func.png" alt="env files screenshot" />

In the Editor select "zip-file" **Method**, and upload zip file

As **Entrypoint** set:
 - src.functions.import_currencies.import_currencies_handler for Import currencies Function


Set Environment Variables

`DB_HOST` - host to database

`DB_PORT` - port to database

`DB_USER` - database's user

`DB_PASSWORD` - user's password

`DB_NAME` - name of the database

These Environment Variables you should to add in "Environment Variables" in the Cloud Function Editor.

<img src="docs/images/envs.png" alt="env files screenshot" />

For Initialize database Function create **Trigger** and set Timer setting "Cron expession" as **"0 9 ? * * *"**.

Select Service account.

Create version.

> There is **Link to invoke** in Cloud Function Overview. It's a endpoint to call. To call this endpoint outside make this function be **public**. 

2. Pushing to Yandex Cloud Conteiner Registry

Create registry in "Container Registry" in Yandex Cloud.

Login into Docker Registry:

```bash
make login
```

Build image:

```bash
make image
```

Tag image:

```bash
docker tag tes-etl cr.yandex/{REGISTRY_ID}/tes-etl:latest
```

Push image:

```bash
docker push cr.yandex/{REGISTRY_ID}/tes-etl
```

Create container in "Serverless Containers" selecting image and service account.

### Postman collection

To call enpoints use **docs/ETL Yandex Cloud.postman_collection.json**


## Usage

> **Test access token:** eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.Kye0_JmjrXRxuPumxWPfYmAUTOLwXQrJXjnQnh-S8VA

SWAGGER ENPOINT: https://d5d3mdq1cofd75iahcah.apigw.yandexcloud.net/docs

<span style="color:red">Authorization token should be provided in **x-auth** header for endpoints.</span> 

Now you can collect currency rates from CBR API to your database calling Import currencies Function from API with Authorization token and also with date_req (required date) query string param in the date format (For, example: 2022-10-11) format (By default setted current date).
https://bba0fqtnqub81soff7qf.containers.yandexcloud.net/api/v1/currency/import?date_req=2022-11-15?date_req=22/10/2022

To get all currency rates for a needed date you should call the Get currencies Function with token and also with date_req query string param.
https://bba0fqtnqub81soff7qf.containers.yandexcloud.net/api/v1/currency?date_req=2022-11-15?date_req=22/10/2022

Example of Get currencies Function's response:

```json
{
  "data": [
    {
      "code": "R01235",
      "numCode": 840,
      "charCode": "USD",
      "nominal": 1,
      "name": "Доллар США",
      "value": 60.3982,
      "dateReq": "2022-11-15"
    },
    {
      "code": "R01239",
      "numCode": 978,
      "charCode": "EUR",
      "nominal": 1,
      "name": "Евро",
      "value": 62.1554,
      "dateReq": "2022-11-15"
    }
  ]
}
```