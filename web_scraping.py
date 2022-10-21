from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
  doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

tag = doc.title
tag.string = "hello" # modify tag
tag2 = doc.find('a')
tag3 = doc.find_all('p')

# print(tag3)

# Reading from a specific URL:
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
# print(result.text)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
price_one = prices[0].parent
strong = price_one.find("strong")
sup = price_one.find("sup")
print("$" + strong.string + sup.string)