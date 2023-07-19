#!/usr/bin/env python
# coding: utf-8

# In[344]:


import requests
from  selenium  import webdriver
from bs4 import BeautifulSoup as bs
import random 
import time
from selenium.webdriver.common.by import By



#proxies_list is a txt file scrapped from some public website and url for that website is url='https://geonode.com/free-proxy-list'
#we put proxies in unchecked list and after checking their connectivity status, keeping them in working , notworkinglist 
#get_rNDOM_PROXY IS  taking random prxy from list if we dont give any input to proxy in get function
#check_proxy is feeding proxy one by one to get function and checking with url provided as indent.me tells us abut conectivity of our proxy to server
#in get we find response from requests.get and see the status of our provided proxy with the url 
#we use try and except method to avoif errors
#with url='http://ident.me/'  we have exceeded limits of connection even though we put 30s delay as well. 
#we should specify no. of times to connect with a website , now using alternative of this 
#url='http://checkip.dyndns.org/'
#



proxies_list=open(r"C:\Users\vicky\OneDrive\Desktop\rotating_proxies_list.txt",'r').read().strip().split('\n')
unchecked=set(proxies_list[1:1000])  #limited to 10 for test
working = set() 
not_working = set() 
VALID_STATUSES = [200, 301, 302, 307, 404]


def get_random_proxy():
    available_proxies=tuple(unchecked.union(working))
    if not available_proxies:
        raise Exception('No proxies available')
    return random.choice(available_proxies)    

def check_proxies():
    #proxies = proxies_list[0:10] # limited to 10 to avoid too many requests 
    #here we put url in get that is used to check proxy
    for proxy in list(unchecked): 
        get("https://icanhazip.com/", proxy) 
     
    
def reset_proxy(proxy): 
    unchecked.add(proxy) 
    working.discard(proxy) 
    not_working.discard(proxy) 
 
def set_working(proxy): 
    unchecked.discard(proxy) 
    working.add(proxy) 
    not_working.discard(proxy) 
 
def set_not_working(proxy): 
    unchecked.discard(proxy) 
    working.discard(proxy) 
    not_working.add(proxy)


def get(url,proxy=None):
    if not proxy:
        proxy=get_random_proxy()
    try:
        response=requests.get(url,proxies={'http': f"http://{proxy}"}, timeout=60)
        if response.status_code in VALID_STATUSES:
            set_working(proxy)
        else:
            set_not_working(proxy)
        #print(response.status_code,response.text)
        
    except Exception as e:
        set_not_working(proxy)
        raise e #raise exception
        
        
 

 
# real scraping part comes here 
def main(): 
    result=check_proxies()
    #result = get("http://ident.me/") 
    #print(result.status_code) # 200 
    #print(result.text) # 152.0.209.175 
 
main()



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[275]:





# In[ ]:





# In[324]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[152]:





# In[ ]:





# In[223]:





# In[261]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[243]:





# In[271]:





# In[ ]:





# In[274]:





# In[ ]:





# In[ ]:





# In[233]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[428]:





# In[ ]:





# In[ ]:




