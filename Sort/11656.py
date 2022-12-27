s= input()
string = list(s)
suffix = [s]
for i in range(len(string)-1):
    string.pop(0)
    suffix.append(''.join(string))
suffix.sort()
for i in range (len(s)):
    print(suffix[i])