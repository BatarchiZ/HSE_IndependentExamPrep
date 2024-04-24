a, b, c, d = map(int, input().split())


def f(x: float) -> float:
   return a * x ** 3 + b * x ** 2 + c * x + d


left = -10 ** 9
right = 10 ** 9

while right - left > 10 ** -6:
   mid = (left + right) / 2
   if f(left) * f(mid) > 0:
       left = mid
   else:
       right = mid
root = (left + right) / 2
print(root)