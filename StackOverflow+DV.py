
# coding: utf-8

# # Stack over flow tag counts data visualization

# In[127]:


from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd


# In[128]:


website='https://stackoverflow.com/tags'
#response=get(website)
page=urllib.urlopen(website)

web_page = page.read()
page.close()


# In[129]:



html_stack = BeautifulSoup(web_page, 'html.parser')

stack_name = html_stack.find_all('a', class_='post-tag')
print(stack_name[0].text)

stack_count = html_stack.find_all('span', class_='item-multiplier-count')
print(stack_count[0].text)

tags = []
tags_count = []


# Loop iterates to get all tags and it's count

# In[130]:


for stack_list in html_stack:
    if stack_list.find('a' ,class_='post-tag') is not None:
        
        tag=stack_list.find_all('a', class_='post-tag')
        tags.append((stack_name[0].text))
        
        tag_count = stack_list.find_all('span' ,class_='metascore favorable')
        tags_count.append(int(stack_count.text))
      


# In[ ]:


stackoverflow_tags = pd.DataFrame({'tag name':tags,'tag count':tags_count})
print(stackoverflow_tags)

