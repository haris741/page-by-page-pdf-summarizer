import time

import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.by import By
pdfFileObj = open('JFQ-68_99-104_Stejskal.pdf', 'rb') #give the file path of pdf
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
total_num_pages=pdfReader.getNumPages()
list=[]
for i in range(total_num_pages):


    driver = webdriver.Chrome()
    driver.get("https://quillbot.com/summarize")
    element=driver.find_element(By.ID,"inputBoxSummarizer")
    pageObj = pdfReader.getPage(i)
    element.send_keys(pageObj.extractText())
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div[2]/div/div/div/button").click()
    time.sleep(5)
    print("\nPage",i+1,"\n")
    print(driver.find_element_by_css_selector("#outputBoxSummarizer").get_attribute("innerText"))
