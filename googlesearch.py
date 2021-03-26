#!/usr/bin/env python
# coding: utf-8

# In[33]:


from selenium import webdriver
import csv

driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://www.google.com/search?gs_ssp=eJzj4tTP1TcwsjQrNDJg9OLNSyxKzUspSlTIzU_JBABf3Afv&q=narendra+modi&oq=nare&aqs=chrome.1.69i57j46i67j0i67j0i10i131i433j46i175i199j0j46j0l2.3844j0j15&sourceid=chrome&ie=UTF-8')
f=open('h.csv','w',newline='',encoding="utf-8")
writer=csv.writer(f)
writer.writerow(['Search_Result_Title','Search_Result_Link','Serch_Result_Description'])

for element in driver.find_elements_by_xpath('//div[@class="g"]'):
    title = element.find_element_by_xpath('.//h3').text
    link = element.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
    detail = element.find_element_by_xpath('.//span[@class="aCOpRe"]').text
    writer.writerow([title,link,detail])
    print(title,link,detail)
    
f.close()
driver.quit()


# In[45]:


from selenium import webdriver
import pandas as pd
import csv

driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://www.google.com/search?gs_ssp=eJzj4tTP1TcwsjQrNDJg9OLNSyxKzUspSlTIzU_JBABf3Afv&q=narendra+modi&oq=nare&aqs=chrome.1.69i57j46i67j0i67j0i10i131i433j46i175i199j0j46j0l2.3844j0j15&sourceid=chrome&ie=UTF-8')


for element in driver.find_elements_by_xpath('//div[@class="g"]'):
    title =element.find_element_by_xpath('.//h3').text
    link = element.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
    detail = element.find_element_by_xpath('.//span[@class="aCOpRe"]').text
    dict={"Search_Result_Title":[title],"Search_Result_Link":[link],"Serch_Result_Description":[detail]}
    df=pd.DataFrame.from_dict(dict)
    print(df)
    print(df.to_csv('h1.csv')



    
    
    


# In[ ]:




