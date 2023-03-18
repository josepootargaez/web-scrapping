import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from decouple import config
from webdriver_manager.chrome import ChromeDriverManager
def scrap():
    try:
        urlWeb  = config("URL_WEB")
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=fake-useragent')
        options.add_argument('--disable-notifications')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage') 
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get(urlWeb)
        driver.implicitly_wait(30)
        l =driver.find_element(By.CSS_SELECTOR,"body > div.page > header > nav > div > div > button")
        driver.execute_script("arguments[0].click();", l)
        driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/div/div[2]/ul/div')
        soup = BeautifulSoup(driver.page_source,'html.parser')
        eq = soup.find_all('li',class_='nav__cat')
        depart = list()
        for li in eq:
            div = BeautifulSoup(str(li),'html.parser')
            departamentSelector=div.select_one('li > ul > li.nav__cat--level2__header-selected > a')
            departament = BeautifulSoup(str(departamentSelector),'html.parser')
            departament = departament.get_text().replace('\n', '')
            if str(departament) !='None': 
                url=departamentSelector['href']
                formatDepartament=foarmatString(departament)
                listCategories=list()
                categories=div.select(f'ul#cat-{formatDepartament} > li > a.nav__cat--level2__toggle')
                for listCat in categories:
                    listsubCategorias=list()
                    textCategory=listCat.get_text().replace("\n", "")
                    subcategories=div.select(f'ul#cat-{formatDepartament} > li > #cat-{foarmatString(textCategory)} > li > a.nav__cat--level2__toggle')
                    for listsubcat in subcategories:
                        urlSubCategory=listsubcat['href']
                        listsubCategorias.append({"name":listsubcat.get_text().replace("\n", ""),"url":f'{urlWeb}{urlSubCategory}'})
                    urlCategory=listCat.get_text().replace("\n", "")
                    listCategories.append({"name":listCat.get_text().replace("\n", ""),"url":f'{urlWeb}/{formatDepartament}/{foarmatString(urlCategory)}',"subcategories":listsubCategorias})
                depart.append({"department":departament,"url":url,"categories":listCategories})
        return depart
    except Exception as inst:
        print(inst)
        return {"error":str(inst)}



        
def getWebSite(link):
    
    try:
        urlWeb  = link
        web=urlWeb.split("/")
        web=f'{web[0]}//{web[2]}'
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=fake-useragent')
        options.add_argument('--disable-notifications')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage') 
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get(urlWeb)
        driver.implicitly_wait(30)
        listArticle=list()
        soup = BeautifulSoup(driver.page_source,'html.parser')
        soup=soup.find_all("div",class_="vtex-search-result-3-x-galleryItem--gallery-css")
        for div in soup:
            html = BeautifulSoup(str(div),'html.parser')
            title=html.select_one("section > a > article > div > div.vtex-flex-layout-0-x-flexColChild--ppal-shelf > div > h3")
            price=html.select_one("#items-price > div > div")
            url=div.a['href']
            listArticle.append({"name":title.get_text().replace("\n", ""),"url":f'{web}{url}',"price":price.get_text().replace("\n", '')})
        listElemnt=[{"url":urlWeb,"products":listArticle}]
        return listElemnt[0]
    except Exception as inst:
        print(inst)
        return {"error":str(inst)}
    
def foarmatString(string):
        formatString=string.lower()
        if(formatString=="cervezas"):
            formatString="cerveza"
        formatString=formatString.replace(",", '')
        formatString=formatString.replace(" ", '-')
        formatString=formatString.replace("á", 'a')
        formatString=formatString.replace("é", 'e')
        formatString=formatString.replace("í", 'i')
        formatString=formatString.replace("ó", 'o')
        formatString=formatString.replace("ú", 'u')
        return formatString
        
        