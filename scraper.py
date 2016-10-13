import requests
from bs4 import BeautifulSoup
import time
from PIL import Image
from StringIO import StringIO



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
  try:
    return [(link.string,link['href']) for link in navbar_links if link and link.has_attr('href')]
  except Exception as e:
    print e 
    return [] 
  
def get_logo(url):
  html = requests.get(url)
  soup = BeautifulSoup(html.text, "html.parser")
  logos = []
  for link in soup.find_all('a'):
    logos.extend(link.find_all('img'))
  if len(logos) == 0:
    logos = soup.find_all('img')
  return logos[0]['src']
 

def rgb2hex(r, g, b):  
  return '#{:02x}{:02x}{:02x}'.format(r, g, b)  

def get_colors(image_url):
  response = requests.get(image_url)
  img = Image.open(StringIO(response.content))
  img_rgb = img.convert('RGB')
  colors = img_rgb.getcolors()
  try:
    return [rgb2hex(*color[1]) for color in colors if color[0] > 100] 
  except Exception as e:
    print e
    return []
  
if __name__ == "__main__":
  
  print get_colors(get_logo("http://www.francolawgroup.com"))
    
