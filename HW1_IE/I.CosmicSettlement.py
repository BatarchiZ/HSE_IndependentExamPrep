n, a, b, w, h = map(int, input().split())

left = 0
right = 2 ** 100
while right > left + 1:
   d = (left + right) // 2
   cnt1 = (w // (a + 2 * d)) * (h // (b + 2 * d))
   cnt2 = (h // (a + 2 * d)) * (w // (b + 2 * d))
   if max(cnt1, cnt2) >= n:
       left = d
   else:
       right = d
print(left)