import re

valid_links = []
pattern = r"(w{3})\.([A-Za-z0-9])+(\-[A-Za-z0-9]+)*(\.[a-z]+)+"
text = input()

while text:
    matches = re.search(pattern, text)
    if matches:
        valid_links.append(matches.group(0))
    text = input()
for vali_link in valid_links:
    print(vali_link)
