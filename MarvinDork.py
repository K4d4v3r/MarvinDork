import requests, re, time, sys
from bs4 import BeautifulSoup
from colorama import *

'''
@AUTHOR: K$D4V3R
SOLO ENCUENTRAS LO QUE BUSCAS
GOOGLE DORK 
'''

# COLORES Y ESTILOS
reset = Style.RESET_ALL
bright = Style.BRIGHT
green = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
blue = Fore.BLUE
red = Fore.RED
yellow = Fore.YELLOW

google_search = requests.Session()

print(f'''           ||||||||||||,,
           |WWWWWWWWW|W|||,
           |_________|~WWW||,
            ~-_      ~_  ~WW||,
            __-~---__/ ~_  ~WW|,
        _-~~         ~~-_~_  ~W
  _--~~~~~~~~~~___       ~-~_/
 -                ~~~--_   ~_
|                       ~_   |
|   ____-------___        -_  |
|-~~              ~~--_     - | By: K$D4V3R
 ~| ~--___________     |-_   ~_
   | \\`~'/  \\`~'_-~~  |  |~-_-
  _-~_~~~    ~~~   _-~  |  |
 ---.--__         ---.-~  |
 | |    -~~-----~~| |    -
 |_|__-~          |_|__-~
''')
dork = input(f'[{bright}{green}*{reset}] DORK _ GOOGLE ?: ')
num_search = input(f'[{bright}{green}*{reset}] NUM _ GOOGLE (MIN:10/MAX:100) ?: ')
print()
search_value = {
	'q': dork,
	'num': num_search
}

soup = BeautifulSoup(google_search.get('https://www.google.com/search',params=search_value,stream=True).text,'html5lib')

enlace = soup.find_all('a')
history_url = []
for enlaces in enlace:
  link = re.sub(r'\&sa[a-zA-Z0-9\-\_\.\=&\%]*','',enlaces['href'])
  if('/url?q' in link):
    extracted_url = re.sub(r'\/url\?q\=','',link)
    domain = re.findall(r'[a-zA-Z]*\.[a-zA-Z]*',extracted_url)[0]
    if(domain not in history_url):
      history_url.append(domain)
      print(f'[{bright}{cyan}*{reset}] {extracted_url}')
      time.sleep(0.3)
