while 1:
    try:
        num = [0,0,0,0] #소문자, 대문자, 숫자, 공백 개수
        string = list(input())
        for i in range(len(string)):
            if(97 <= ord(string[i]) and 122 >= ord(string[i])):
                num[0] += 1
            elif(65 <= ord(string[i]) and 90 >= ord(string[i])):
                num[1] += 1
            elif(48 <= ord(string[i]) and 57 >= ord(string[i])):
                num[2] += 1
            elif(ord(string[i]) == 32):
                num[3] += 1
        num = list(map(str,num))
        print(' '.join(num))
    except:
        break
