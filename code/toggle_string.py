'''
Toggle characters in a string
'''
data = raw_input()
data = list(data)
for i in range(len(data)):
    if data[i].isupper():
        data[i] = data[i].lower()
    else:
        data[i] = data[i].upper()

print ''.join(data)
