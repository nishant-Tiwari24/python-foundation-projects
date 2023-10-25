import string
dict={}
file = open('output.txt','w')

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-1]
print(dict)
with open('input.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
            file.write(data)
            print(data)
file.close()