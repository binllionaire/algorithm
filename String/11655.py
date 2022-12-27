string = list(input())
for i in range(len(string)):
    if(97 <= ord(string[i]) and 122 >= ord(string[i])):
        if(ord(string[i])+13>122):
            string[i] = chr(96+ord(string[i])+13-122)
        else:
            string[i] = chr(ord(string[i])+13)
    elif(65 <= ord(string[i]) and 90 >= ord(string[i])):
        if(ord(string[i])+13>90):
            string[i] = chr(64 +ord(string[i])+13-90)
        else:
            string[i] = chr(ord(string[i])+13)
print(''.join(string))