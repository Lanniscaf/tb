"""
  TOOLS IS BASED IN
  CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
  Copyright (C) 2020  

  DISCLAIMER: This file is for informational and educational purposes only. 
  We are not responsible for any misuse applied to it. All responsibility falls on the user

  ||================================================================================||
  || FRAGMENTS USED FROM https://github.com/Lanniscaf/cctools/blob/master/cctools.py||
  ||================================================================================||

  Adapted BY lanniscaf ALL RIGHTS RESERVED
  """
import requests, json, re
from bs4 import BeautifulSoup

def bincheck(bino):
    binom= str(bino)
    try:
        bino= binom.replace("x","")
        bino= bino.replace("X","")
        bino= bino.split("|")[0]
    except:
        pass
    bino = str(re.sub('([a-zA-Z]){1,}', '', bino))
    if(len(str(bino))<6):
        return 'Invalid Bin'
    if(len(str(bino))>6):
        bino=bino[:6]
    url = 'https://bincheck.io/bin/{0}'.format(bino)
    data = {}
    page = requests.post(url, data=data)
    page = BeautifulSoup(page.content, 'html.parser')
    try:
        bindata = page.find("div", attrs={"class":"card-primary"})
        bindata = bindata.find("div", attrs={"class":"card-body"}).table.tbody
        bindata = bindata.findAll('tr')
    except:
        return False
    titles  = []
    results = []
    for tr in bindata:
        params = tr.findAll('td')
        titles.append((params[0].text).replace('\t',''))
        results.append((params[1].text).replace('\t',''))
    myjson = {}
    for i in range(len(titles)):
        myjson[titles[i]] = results[i]
    
    return myjson
def alternateS(bino):
  binom= str(bino)
  try:
    bino= binom.replace("x","")
    bino= bino.replace("X","")
    bino= bino.split("|")[0]
  except:
    pass
  bino = str(re.sub('([a-zA-Z]){1,}', '', bino))
  if(len(str(bino))<6):
    return 'Invalid Bin'
  if(len(str(bino))>6):
    bino=bino[:6]
  url="http://www.bins.su/"
  data={
    "action":"searchbins",
    "bins":bino,
    "bank":"",
    "country":""
  }
  try:
    page = requests.post(url, data=data)
    page.raise_for_status()
  except:
    return checkear(bino)
  page =BeautifulSoup(page.content,"html.parser")

  result=page.find("div", attrs={"id":"result"}).table
  try:
    result=result.find_all("tr")
  except:
    #error no existe
    return 'Invalid Bin'
  try:
    hed=result[0]
    hed=hed.find_all("td")
    dat=result[1]
    dat=dat.find_all("td")
    cabeceras=[]
    datos=[]
    for i in range(len(hed)):
        cabeceras.append(hed[i].text)
    for i in range(len(dat)):
        datos.append(dat[i].text)
    date='*Valid* '
    for i in range(len(datos)):
      if(datos[i] != '' and datos[i]!=' '):
        date+= '*{}:* _{}_\n'.format(cabeceras[i],datos[i])
      else:
        date+= '*{}:* _{}_\n'.format(cabeceras[i],'None')
    return date
  except:
    return 'Error desconocido'
def checkear(bin):
    bin= str(bin)
    try:
        bin= bin.replace("x","")
        bin= bin.replace("X","")
        bin= bin.split("|")[0]
    except:
        pass
    bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
    lenLuhn=len(str(bin))
    sinccheck=bin[:16]
    bin = str(bin)
    bin = re.sub('([a-zA-Z]){1,}', '', bin)
    try:
        unks = 0
        url='https://lookup.binlist.net/'+str(bin)
        try:
            page = requests.get(url)
            page.raise_for_status()
        except:
            return alternateS(bin)
        
        
        page= page.content.decode()
        dic = json.loads(page)
        try:
            luhn = dic['number']['luhn']
        except:
            luhn = 'Unk'
            unks+=1
        try:
            luhnLen = dic['number']['length']
        except:
            luhnLen = 'Unk'
            unks+=1
       
        brand = dic['scheme']
        
        try:
            brand2 = dic["brand"]
        except:
            brand2 = ''
            unks+=1
        try:
            tipe = dic["type"]
        except:
            tipe = 'Unk'
            unks+=1
        try:
            prepaid = dic["prepaid"]
        except:
            prepaid = 'Unk'
        country= dic["country"]["name"]
        try:
            emoji = dic["country"]["emoji"]
        except:
            emoji = ""
        try:
            bank = dic["bank"]['name']
        except:
            bank = 'Unk'
            unks+=1
        try:
            urlBank = dic["bank"]["url"]
        except:
            urlBank = 'Unk'
            unks+=1
        try:
            phoneBank = dic["bank"]["phone"]
        except:
            phoneBank = 'Unk'
            unks+=1
        try:
            city = dic["bank"]["city"]
        except:
            city = 'Unk'
            unks+=1
        datosS = """Valid Bin:{}
Brand: {} - {}
Type: {}
Prepaid: {}
Country: {}
Bank: {}
Telefono del banco: {}
Ciudad: {}
Url del banco: {}
""".format(bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank)
        
        if(unks<=7):
            return datosS
        else:
            return alternateS(bin)
        
    except:
        return('Invalid Bin')