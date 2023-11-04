'''This file reads in json data from the NYT Bestsellers API
    it then stores information from that data in multiple dictionaries.
    These dictionaries are Title, Author, and Description.'''

import json

with open('NYT bestsellers - full overview - current.json') as f:
    data = json.load(f)

results = data['results']
lists = results['lists']

bestseller_list = [] #list of the lists of best sellers
titles = [] #all titles in the bestsellers lists
description_dict = {} #quick look up of descriptions for each book

for i in range(len(lists)):
    bestseller_list.append(lists[i].get('books')) #get only the books from the bestseller list
    for j in range(len(bestseller_list[i])):
        title = bestseller_list[i][j].get('title') #within the book list, get the title
        description = bestseller_list[i][j].get('description') #within the book list, get the description
        titles.append(title) #list of titles
        description_dict[title] = description #dictionary with title as key and description as value