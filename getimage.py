
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import urllib.request as ulib
import ast
import os
import tkinter.filedialog

def getURLs(URL):
    driver = webdriver.Chrome(executable_path='[add_chrome_driver_absolute_path]' )
    driver.get(URL)
    page = driver.page_source
    print(page)
    soup = Soup(page, 'lxml')
    desiredURLs = soup.findAll('div', {'class':'rg_meta notranslate'})
    ourURLs = []
    for url in desiredURLs:
        theURL = url.text
        theURL = ast.literal_eval(theURL)['ou']
        ourURLs.append(theURL)
    return ourURLs

def save_images(urls, scrape_directory):
    for i, url in enumerate(urls):
        savePath = os.path.join(scrape_directory, '{:06}.jpg'.format(i))
        try:
            ulib.urlretrieve(url, savePath)
        except:
            print('I failed with', url)

def imagescrape():
    URL= "https://www.google.com/search?q=" + searchTerm + "&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiUouHwrIzjAhULS48KHcXDC44Q_AUIESgC&biw=1036&bih=714&dpr=1.25"
    urls = getURLs(URL)
    for url in urls:
            print(url)
    save_images(urls, scrape_directory)

print("Images are going to downloaded!!")

while True:
    while True:
        print("Please select a directory to save your scraped files.")
        scrape_directory = tkinter.filedialog.askdirectory()
        if scrape_directory == None or scrape_directory == "":
            print("You must select a directory to save your scraped files.")
            continue
        break
    while True:
        searchCount = int(input("Number of search terms: "))
        if searchCount < 1:
            print("You must have at least one search term.")
            continue
        elif searchCount == 1:
            searchTerm = input("Search term: ")
        else:
            searchTerm = input("Search term 1: ")
            for i in range (1, searchCount):
                searchTermPart = input("Search term " + str(i + 1) + ": ")
                searchTerm += "+" + searchTermPart
        break

    while True:
        imagescrape()
    print("Scraping complete.")
    restartScrape = input("Keep scraping? ('y' for yes or 'n' for no) ")
    if restartScrape == "n":
        print("Scraping ended.")
        break
