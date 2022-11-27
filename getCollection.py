from lib2to3.pgen2 import driver
from urllib import response
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

firefox_options = Options()
#firefox_options.add_argument("--headless")
driver = webdriver.Firefox(executable_path=r'./geckodriver',options=firefox_options)
driver.fullscreen_window()

url = 'https://opensea.io/letsGoBrandon-NFT'
response = driver.get(url)
nftDict = []
def divScrappe(div,last_height):
    textVariable = '/html/body/div[1]/div/main/div/div/div/div[5]/div/div[3]/div[3]/div[3]/div[2]/div/div[%s]'%div
    htmltest = driver.find_element_by_xpath(textVariable)
    if htmltest.text == '':
        time.sleep(15)
        textVariable = '/html/body/div[1]/div/main/div/div/div/div[5]/div/div[3]/div[3]/div[3]/div[2]/div/div[%s]'%div
        htmltest = driver.find_element_by_xpath(textVariable)
        print(f"the div is {div}")
        print(htmltest.text)
        driver.execute_script("arguments[0].scrollIntoView();",htmltest)
        nftDict.append(htmltest)

    print(f"the div is {div}")
    print(htmltest.text)
    driver.execute_script("arguments[0].scrollIntoView();",htmltest)
    nftDict.append(htmltest)
   
                                    
    

maxDivs = 0
last_height = 0
for nft in range(1,7600):
    total_height = driver.execute_script("return document.body.scrollHeight;")
    
    
    print(maxDivs)
    if maxDivs == 19:
        print(last_height)
        last_height += 2000
        #driver.execute_script("window.scrollTo(0,{last_height});".format(last_height=last_height))
        time.sleep(10)
        maxDivs = 0
    
    divScrappe(nft,last_height)
    maxDivs += 1

with open ('nftCollections.txt','w') as f:
    for nft in nftDict:
        f.write("%s\n" % nft)
    print("Done writting the file")
# TODO: go through all the nfts 

# TODO: put them on a dictionary 
