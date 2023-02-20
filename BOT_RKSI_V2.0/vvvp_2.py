
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
  
# Opening the html file
HTMLFile = open("pars.html", "r")
  
# Reading the file
index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'lxml')
  
# Using the select method
# Prints the second element from the li tag
print(S.select('li:nth-of-type(2)'))