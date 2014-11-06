import requests
import re
import json

#creates an elasticsearch bulk file of Pride and Prejudice chapters

text = requests.get("https://www.gutenberg.org/cache/epub/42671/pg42671.txt")
chapters = re.split('CHAPTER .*?\.', text.text)
outfile = open('pride.json', 'w')
lines = []
for idx, ch in enumerate(chapters):
    if idx == 0:    
        continue #skip PG boilerplate

    lines.append(json.dumps({ "index": { "_index": "pride", "_type": "chapter", "_id": idx } }) + '\n')
    lines.append(json.dumps({"text": ch, "chapter": idx }) + '\n')

outfile.writelines(lines)

