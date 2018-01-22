
# coding: utf-8

# # Movie Ratings Scraper

# In[103]:


#import urllib, urllib2
from bs4 import BeautifulSoup
import pandas as pd
from requests import get


# In[104]:



#url="https://www.reddit.com/r/gameofthrones/"
url='http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response=get(url)
#content = urllib2.urlopen(url).read()
#print(content)

#print(response.text[:100000000])
names = []
ratings = []
metascore = []

#movie_def = pd.DataFrame({'movie':names,'ratings':ratings,'score':metascore})

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)


movie_contains = html_soup.find_all('div' ,class_='lister-item mode-advanced')
print(type(movie_contains))

print(len(movie_contains))
first_movie = movie_contains[0]

first_movie_name = first_movie.h3.a.text
print(first_movie_name)

first_movie_imdb = float(first_movie.strong.text)
print(first_movie_imdb) 

movie_score = first_movie.find('span' ,class_='metascore favorable')
print(int(movie_score.text))


# In[105]:


for contains in movie_contains:
    if contains.find('div' ,class_='ratings_metascore') is not None:
        name=contains.h3.a.text
        names.append(name)
        
        rating = contains.strong.text
        ratings.append(rating)
        
        movie_metascore = contains.find('span' ,class_='metascore favorable')
        metascore.append(int(movie_metascore.text))
        

movie_def = pd.DataFrame({'movie':names,'ratings':ratings,'score':metascore})
print(movie_def)


# In[106]:


movies = pd.DataFrame(dict(zip(names,ratings,metascore)).items(),columns = ['Movie','Rating','Score'])


# In[107]:


movies.to_csv('movies.csv',index = False)

