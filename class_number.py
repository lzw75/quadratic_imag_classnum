# Program to compute the class number of the quadratic order with discriminant d.
# This only works for negative d. Of course we need d = 0, 1 mod 4.
# Warning: super-unoptimized!

def gcd(a, b):
   a, b = abs(a), abs(b)
   if b > a: a, b = b, a
   while b:
      a, b = b, a % b
   return a
   
  
# Only works for negative discriminant.

def class_number(d):
   if d >= 0: return -1
   if d % 4 != 0 and d % 4 != 1: return 0
   num = 0
   
   a_max = int((-d/3) ** 0.5)
   for a in range(1, a_max+1):
      for b in range(-a+1, a+1):
         t = b*b - d
         if t % (4*a) == 0:
            c = t // (4*a)
            if a < c or (b >= 0 and a == c):
               if gcd(gcd(a, b), c) == 1:
                  # print([a, b, c])
                  num += 1         
   
   return num

   
for d in range(1, 200):
   class_num = class_number(-d)
   if (class_num): print(-d, class_num)
   

