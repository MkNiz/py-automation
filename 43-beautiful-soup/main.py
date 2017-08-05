import bs4
from pygame import display

index = open('index.html')
indexSoup = bs4.BeautifulSoup(index, "html.parser")

def displayMatches(selected):
    """Displays the text of selected elements"""
    for ix, el in enumerate(selected):
        print("\t" + str(ix+1) + ".) " + el.getText())
    print("")

print("Title:", indexSoup.select('title')[0].getText())

pars = indexSoup.select('p')
print("Paragraphs:")
displayMatches(pars)
    
links = indexSoup.select('a')
print("Links:")
displayMatches(links)

bigtext = indexSoup.select('.bigtext')
print("With class 'bigtext':")
displayMatches(bigtext)

scraem = indexSoup.select('#scraem')
print("With ID 'scraem':")
displayMatches(scraem)
    