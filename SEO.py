
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt') 


url = "https://tenten.vn/tin-tuc/web-portal/"
 soup = BeautifulSoup(res.text, 'html.parser') 
def seo_analysis(url):
# Save the good and the warnings in lists
    good = []
    bad = []
# Send a GET request to the website
    response = requests.get(url)
# Check the response status code
    if response.status_code != 200:
        print("Error: Unable to access the website.")
        return

# Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
# Extract the title and description
    title = soup.find('title').get_text()
    description = soup.find('meta', attrs={'name': 'description'})['content']

# Check if the title and description exist
    if title:
        good.append("Title Exists! Great!")
    else:
        bad.append("Title does not exist! Add a Title")

    if description:
        good.append("Description Exists! Great!")
    else:
        bad.append("Description does not exist! Add a Meta Description")

# Grab the Headings

for h in soup.find_all(['h1', 'h2', 'h3']):
  hs = ['h1', 'h2', 'h3']
  h_tags = []
  for h in soup.find_all(hs):
    good.append(f"{h.name}-->{h.text.strip()}")
    h_tags.append(h.name)

  if 'h1' not in h_tags:
    bad.append("No H1 found!")

# Extract the images without Alt
    for i in soup.find_all('img', alt=''):
        bad.append(f"No Alt: {i}") 

# Extract keywords
# Grab the text from the body of html
    bod = soup.find('body').text
# Extract all the words in the body and lowercase them in a list
    words = [i.lower() for i in word_tokenize(bod)] #use the tokenize in nltk to get text body
# Grab a list of English stopwords
    sw = nltk.corpus.stopwords.words('Vietnamese')
    new_words = []

# Put the tokens which are not stopwords and are actual words (no punctuation) in a new list
    for i in words:
      if i not in sw and i.isalpha():
        new_words.append(i)

# Extract the fequency of the words and get the 10 most common ones
    freq = nltk.FreqDist(new_words)
    keywords= freq.most_common(10)

# Print the results
    print("Keywords: ", keywords)
    print("The Good: ", good)
    print("The Bad: ", bad)
    
# Call the function to see the results
seo_analysis("https://tenten.vn/tin-tuc/web-portal/")
print (seo_analysis)






from bs4 import BeautifulSoup
import requests

url = "https://tenten.vn/tin-tuc/web-portal/"
res = requests.get(url, timeout=10) #lay text cua url tren
soup = BeautifulSoup(res.text, 'html.parser') #parse html
good=[]
keywords=[]
bad=[]
# Extract the title
title = soup.find('title').text
if title:
   good.append (f"title:{title} ")
else:
   bad.append(f"not found the title!!! ")
#print title vua extract
# print (title)
meta_detail= soup.find('meta', attrs={'name': 'description'}) ['content']
# tim thuoc tinh cua element meta 
# print(meta_detail)
if meta_detail:
   good.append (f"meta desciption:{meta_detail} ")
else:
   bad.append(f"not found the meta!!! ")

#heading
for h in soup.find_all(['h1', 'h2', 'h3']): # defining headings in HTML documents. 
  head_containing = ['h1', 'h2', 'h3']
  h_tags = [] #luu cac tag duoc extract ra
  for h in soup.find_all(h):
    good.append(f"{h.name}-->{h.text.strip()}")
    h_tags.append(h.name)

  if 'h1' not in h_tags:
    bad.append("No H1 found!")

#lay 
for i in soup.find_all('img', enter=''):
    bad.append(f"no enter: {i}")

print (good)
print('')
print (bad)
seo_analysis("https://tenten.vn/tin-tuc/web-portal/")
