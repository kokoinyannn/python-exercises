'''
Write To A File 
Exercise 21
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:
Ask the user to specify the name of the output file that will be saved.
'''

import requests
from bs4 import BeautifulSoup

url='https://www.nytimes.com/'
a=requests.get(url)
print(a,file=open('output_a.txt','w'))
soup=BeautifulSoup(a.text)
print(soup,file=open('output_soup.txt','w'))
filename=input('Please name the file: ')+'.txt'
for story_heading in soup.find_all(class_="story-heading"):
    print(story_heading.text, file=open(filename,'a'))