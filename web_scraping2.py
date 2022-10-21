from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
  doc = BeautifulSoup(f, "html.parser")

# Searching html documents
# .find()
# .find_all()

tag = doc.find("option")
attributes = tag.attrs
# print(attributes)

# multiple tags
tags = doc.find_all(["p", "div", "li"])
# print(tags)

# tag with text
tag_text = doc.find_all(["option"], text="Undergraduate")
# print(tag_text)

# tag with text & attributes
tag_text_attr = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
# print(tag_text_attr)

# class names
tag_class_name = doc.find_all(class_="btn-item")
# print(tag_class_name)

# regular expressions
tags_re = doc.find_all(text=re.compile("\$.*"))
for tag in tags_re:
  pass
  # print(tag.strip())

# limit result when searhing
tags_re2 = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in tags_re2:
  print(tag.strip())

# saving changes to document
tags_change = doc.find_all("input", type="text")
for tag in tags_change:
  tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
  file.write(str(doc))