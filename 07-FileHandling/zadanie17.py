with open('tekst.txt', 'r') as first, open('copylines.txt','a') as second:
    for line in first:
        for words in line.split():
            second.write(words+'\n')