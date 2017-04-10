'''
A webcrawler that retrieves a specific image from a website and saves it
on your computer
'''

import random
import urllib.request

def download_web_image(url):
	name = random.randrange(1,100)
	full_name = str(name) + '.jpg'
	urllib.request.urlretrieve(url, full_name)

download_web_image('http://www.womenintechnology.co.ke/wp-content/themes/wit/img/logo.png')