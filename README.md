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

###  Repository Scrapping
git clone https://github.com/josepootargaez/web-scrapping.git
cd web-scrapping
 ### run the next comands to active the docker container and deploy api

    docker build -t web-scrapping .

    docker run -it -p 8000:8000 -v /app web-scrapping

### show api 
http://localhost:8000/docs

## optional
 ### run without docker and run in local 
    pip install -r requirements.txt
    uvicorn main:app --reload
## test
 ### http://localhost:8000/scrap-web-soriana
 ```
{
     "result": [
        {
            "department": "Vinos, licores y cervezas",
            "url": "https://www.soriana.com/vinos-licores-y-cervezas.html",
            "categories": [
                {
                    "name": "Cervezas",
                    "url": "https://www.soriana.com/vinos-licores-y-cervezas/cerveza",
                    "subcategories": [
                        {
                            "name": "Clara",
                            "url": "https://www.soriana.com/vinos-licores-y-cervezas/cervezas/clara/"
                        },
                        {
                            "name": "Obscura",
                            "url": "https://www.soriana.com/vinos-licores-y-cervezas/cervezas/obscura/"
                        },
                        {
                            "name": "Artesanal",
                            "url": "https://www.soriana.com/vinos-licores-y-cervezas/cervezas/artesanal/"
                        },
                        {
                            "name": "Importada",
                            "url": "https://www.soriana.com/vinos-licores-y-cervezas/cervezas/importada/"
                        }
                    ]
                }
            ]
        }
     ]
}
 ```
 ### http://localhost:8000/scrap-site?url=https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas
```
{
    "result": {
        "url": "https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas",
        "products": [
            {
                "name": "Atún En Aceite Van Camps x 160g x 4und ",
                "url": "https://www.tiendasjumbo.co/atun-en-aceite-van-camps-x-160g-x-4und/p",
                "price": "$ 31.990"
            },
            {
                "name": "Atún En Agua Van Camps x 160g x 4und ",
                "url": "https://www.tiendasjumbo.co/atun-en-agua-van-camps-x-160g-x-4und/p",
                "price": "$ 30.990"
            },
            {
                "name": "Atún Aceite Oliva 3und x 80g Van Camps ",
                "url": "https://www.tiendasjumbo.co/atun-aceite-oliva-3und-x-80g-van-camps/p",
                "price": "$ 14.390"
            },
            {
                "name": "Atún Cuisine&Co lomo aceite soya x4und x160g c-u ",
                "url": "https://www.tiendasjumbo.co/atun-cuisine-co-lomo-aceite-soya-x4undx160gc-u-3444295/p",
                "price": "$ 23.390"
            },
            {
                "name": "Maíz Tierno San Jorge x 2 und.x 190 g ",
                "url": "https://www.tiendasjumbo.co/maiz-tierno-san-jorge-x-2-und-x-190-g/p",
                "price": "$ 13.390"
            },
            {
                "name": "Atún Agua 3und x 80g Van Camps ",
                "url": "https://www.tiendasjumbo.co/atun-agua-3und-x-80g-van-camps/p",
                "price": "$ 16.590"
            },
            {
                "name": "Sardina Tomate x 425g Van Camps ",
                "url": "https://www.tiendasjumbo.co/sardina-tomate-x-425g-van-camps/p",
                "price": "$ 11.990"
            },
            {
                "name": "Atún Cuisine&Co lomitos agua x4und x160g c-u ",
                "url": "https://www.tiendasjumbo.co/atun-cuisine-co-lomitos-agua-x4und-x160g-c-u-3444294/p",
                "price": "$ 23.390"
            }
        ]
    }
}
```