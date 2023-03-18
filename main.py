from function import scrap, getWebSite
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(tittle='Web Scraping',description='web scrapping',version='1.0.1')
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrap-web-soriana")
def scrapSoriana():
    result =  scrap()
    if  "error" in result:
        raise HTTPException(
            status_code=500,
            detail="error internal server",
        )
    return {"result":result}

@app.get("/scrap-site")
def scrapWeb(url:str):
    result =  getWebSite(url)
    if  "error" in result:
        raise HTTPException(
            status_code=404,
            detail="page not found",
        )
    return {"result":result}


