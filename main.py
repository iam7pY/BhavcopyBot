import requests
import shutil
import zipfile
from datetime import date, timedelta
from time import time, sleep



#Telegram Credetials
api_id = '10057219'
api_hash = 'aec3b9b99ec40289affdc51ac921d1a5'
#botTokenfromBotFather
token = '5360470359:AAE0WrM072Lx7VMvF90sJ5_TXWlcnpZgVNA'
groupChatID = "-799170877"
message= ""
telegramURL = f"https://api.telegram.org/bot5360470359:AAE0WrM072Lx7VMvF90sJ5_TXWlcnpZgVNA/sendMessage?chat_id{groupChatID}&text={message}"



adjustment = 0
bhavcopyFlag = 0
checkEvery = 300 #seconds
today = date.today() - timedelta(days=adjustment)
today= today.strftime(("%b-%d-%Y"))
monthAbbreviation = today[:3].upper()
dateDay = today[4:6]
dateYear = today[-4:]



def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

bhavcopyUrl = f"https://www1.nseindia.com/content/historical/DERIVATIVES/2022/{monthAbbreviation}/fo{dateDay}{monthAbbreviation}{dateYear}bhav.csv.zip"
download_file(bhavcopyUrl)
zip_file = bhavcopyUrl[-23:]
fileToextract = zip_file[:-4]
#print("here at line 43")

while(bhavcopyFlag!=1):
    #print("in while")
    try:
        #print("in try")
        with zipfile.ZipFile(zip_file) as z:
            with open(fileToextract, 'wb') as f:
                f.write(z.read(fileToextract))
                print("Extracted", fileToextract)
                bhavcopyFlag = 1
                message = f"Bhavcopy {fileToextract} Downloaded "
                telegramURL = f"https://api.telegram.org/bot5360470359:AAE0WrM072Lx7VMvF90sJ5_TXWlcnpZgVNA/sendMessage?chat_id={groupChatID}&text={message}"
                #print(telegramURL)
                requests.get(telegramURL)

    except:
        #print("in except")
        bhavcopyFlag = 0
        message = f"Bhavcopy for {today} not yet arrived, will check in {checkEvery} seconds"
        telegramURL = f"https://api.telegram.org/bot5360470359:AAE0WrM072Lx7VMvF90sJ5_TXWlcnpZgVNA/sendMessage?chat_id={groupChatID}&text={message}"
        requests.get(telegramURL)
        print(telegramURL)
        #print(f"will check in {checkEvery} seconds")
        sleep(checkEvery - time() % checkEvery)







