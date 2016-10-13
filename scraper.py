import requests
from bs4 import BeautifulSoup
import time


logo = [] 
links_visited = 0

def get_navbar_links(url):
  global navbar_links
  html = requests.get(url)
  soup =  BeautifulSoup(html.text, "html.parser")
  navbar = soup.find_all('ul')
  navbar_links = []
  if len(navbar) > 0:
    for li in navbar[0].find_all('li'):
      navbar_links.append(li.find('a'))
  print navbar_links 
  return [(link.string,link['href']) for link in navbar_links if link and link.has_attr('href')]
    
  
def get_logo(url):
  html = requests.get(url)
  soup = BeautifulSoup(html.text, "html.parser")
  logos = []
  for link in soup.find_all('a'):
    logos.extend(link.find_all('img'))
  if len(logos) == 0:
    logos = soup.find_all('img')
  print logos
  return logos[0]['src']    
 

if __name__ == "__main__":

  print get_logo(raw_input(">>>"))
    
