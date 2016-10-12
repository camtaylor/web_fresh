import requests
from bs4 import BeautifulSoup
import time


logo = [] 
links_visited = 0

def scrape_website(url):
  global navbar_links
  html = requests.get(url)
  print html
  soup =  BeautifulSoup(html.text, "html.parser")
  navbar_links = soup.find_all('a')
  logo = soup.find_all('img')
    
  
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

  get_logo("http://dallaslawyers.com")
    
