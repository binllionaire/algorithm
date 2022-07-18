# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#    *
#   * *
#  *   *
# *******

N=int(input());
j=1;
for i in range(1,N+1):
  if(i==1):
    print(" "*(N-1)+"*");
  elif(i==N):
    print("*"*(N*2-1));
  else:
    print(" "*(N-i)+"*"+" "*j+"*")
    j+=2
