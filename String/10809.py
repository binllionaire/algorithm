s = input()
string = str(s)
num = [-1] * 26
for i in range(len(string)):
    if(num[ord(string[i])-97] == -1):
        num[ord(string[i])-97] = i
num = list(map(str,num))
print(' '.join(num))