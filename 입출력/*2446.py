# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

# N=int(input());
# n=N;
# i=0;
# for i in range (i,N-1) :
#   print(" "*i+"*"*(2*n-1));
#   n-=1;

# i=1;
# n=N;
# for i in range (i,N+1) :
#   if(i==1):
#     print(" "*(N-i)+"*"*(N-(N-i)));
#   else:
#     print(" "*(N-i)+"*"*(N-(N-i))+"*"*(N-(N-i)-1));
  

n = int(input())
for i in range(1, n + 1):
  print(" " * (i - 1) + "*" * (2 * (n - i) + 1))
for j in range(1, n):
  print(" " * (n - j - 1) + "*" * ((2 * j) + 1))