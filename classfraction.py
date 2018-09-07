def gcd(m,n):
   while m%n != 0:
       oldm = m
       oldn = n

       m = oldn
       n = oldm%oldn
   return n


class Fraction:

   def __init__(self,top,bottom):

       self.num = top
       self.den = bottom

   def show(self):
       print(self.num,"/",self.den)

   def __str__(self):
       return str(self.num)+"/"+str(self.den)

   def __add__(self,otherfraction):

       newnum = self.num*otherfraction.den + self.den*otherfraction.num
       newden = self.den * otherfraction.den
       common = gcd(newnum,newden)

       return Fraction(newnum//common,newden//common)

   def __eq__(self, otherfraction):
       firstnum = self.num * otherfraction.den
       secondnum = otherfraction.num * self.den

   def __sub__(self, otherfraction):

       newnum = self.num*otherfraction.den - self.den*otherfraction.num
       newden = self.den * otherfraction.den
       common = gcd(newnum,newden)

       return Fraction(newnum//common,newden//common)

   def __mul__(self, otherfraction):

       newnum = self.num*otherfraction.num
       newden = self.den * otherfraction.den
       common = gcd(newnum,newden)

       return Fraction(newnum//common,newden//common)    
 
   def __truediv__(self, otherfraction):

       newnum = self.num*otherfraction.den
       newden = self.den * otherfraction.num
       common = gcd(newnum,newden)

       return Fraction(newnum//common,newden//common)

   def __gt__(self, otherfraction):

      newnum1 = self.num*otherfraction.den
      newnum2 = self.den*otherfraction.num

      if newnum1>newnum2:
          return True
      else:
          return False

   def __lt__(self, otherfraction):

      newnum1 = self.num*otherfraction.den
      newnum2 = self.den*otherfraction.num

      if newnum1<newnum2:
          return True
      else:
          return False




F1 = Fraction(3,5)
F2 = Fraction(4,3)

print(F1-F2)
print(F1*F2)
print(F1/F2)
print(F1>F2)
print(F1<F2)
print(F1==F2)












