# Web Scrapping
   The Api Scrapping to get information abount website.

## Technical specifications of the environment

* **Python** - `v3.0`
* **uvicorn** - `v0.21.1`
* **fastapi** - `v0.94.1`
* **docker** - `v20.10.17`
* **selenium** - `4.8.2`
* **beautifulsoup4** - `4.11.2`
* **python-dotenv** - `1.0.0`
* **python-decouple** - `1.0.0`
* **webdriver-manager** - `3.8.5`


## Installation
 clone the repository

###  Transaction
git clone https://github.com/josepootargaez/summary-transactions.git  
cd summary-transactions
 ### run the next comands to active the docker container and deploy api

    docker build -t summary-transactions .

    docker run -it -p 8000:8000 -v /app summary-transactions

### show api 
http://localhost:8000/docs

## optional
 ### run without docker and run in local 
    pip install -r requirements.txt
    uvicorn main:app --reload

### finally install front aplication
https://github.com/josepootargaez/summary-transactions-front.git