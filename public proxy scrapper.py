#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import requests
from  selenium  import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


url=''  # website of  url that i scrapped , so this all finding of all elements is done XPATH which may have been changed so change xpaths accordingly
driver=webdriver.Chrome()
driver.get(url)
html=driver.page_source



ip=[]
port=[]
click_iterations=100  #clicking see more button to go on next page or scroll through infinte page 

for _ in range(click_iterations):
    ip_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/div/div[2]/div[3]/div/div[2]/div/div/div/table/tbody/tr/td[1]/span')
    port_elements=elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/section/div/div[2]/div[3]/div/div[2]/div/div/div/table/tbody/tr/td[2]/span')
    ip+=[element.text for element in ip_elements ]
    port+=[element.text for element in port_elements ]
    
    try:
        # Find the "See More" button element
        see_more_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/section/div/div[2]/div[3]/div/div[2]/nav/div[3]/div[2]/button/span')
        # Click the "See More" button
        see_more_button.click()
        
        # Wait for the new content to load
        time.sleep(20)
    
    except Exception:
        # If the "See More" button is not found, break the loop
        break

        
proxies=[]
for i in range(len(ip)):
    proxies.append(ip[i]+':'+port[i])   #making a proper list of full proxy that is ip and port name   
    
#saving that list of proxies in a text file as text file 
    
with open(r"C:\Users\vicky\OneDrive\Desktop\rotating_proxies_list.txt",'w') as tfile:
     tfile.write('\n'.join(proxies))           
        
        
        

