import keyword

print(keyword.kwlist)

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print('%8s ' % x, keyword.iskeyword(x))
