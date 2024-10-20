string = 'xdfcgh(xdfcgbhjk)fdcgvbhj'
for item in string:
    string = string.replace('(', ' ')
    string = string.replace(')', ' ')
print(string.split()[1])
