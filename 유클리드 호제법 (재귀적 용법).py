'''
재귀적 용법은 어디에 쓰지?
-> 수학적 점화식을 코드로 옮길 때 간단하게 활용할 수 있다.
'''

'''
유클리드 호제법 = 두 수의 최대 공약수를 구할 때 쓰는 방법.
A = B * Q + R
,where A, B has the same common factor with B, R.
'''

def gcd(a,b)
  if a%b == 0:
    return b
  return gcd(b,a%b)
