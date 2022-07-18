# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#   *
#  **
# ***
#  **
#   *

N=int(input());
i=1;
for i in range(i,2*N) :
  if(i<=N) :
    print(" "*(N-i)+"*"*i);
  else :
    print(" "*(i-N)+"*"*(N-(i-N)));
