s = input()
string = str(s)
num = [0] * 26
for i in range(len(string)):
    num[ord(string[i])-97] += 1
num = list(map(str,num))
print(' '.join(num))
