from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents # get children

# print(trs[0].next_sibling) # next
# print(trs[1].previous_sibling) # previous
# .next_siblings will get a generator object
# .parent will give parent
# .descendants - gives everything after
# .children

prices = {}

for tr in trs[:10]:
  name, price = tr.contents[2:4]
  fixed_name = name.p.string
  fixed_price = price.a.span.string

  prices[fixed_name] = fixed_price

print(prices)
