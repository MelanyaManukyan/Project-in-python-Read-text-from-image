n = int(input('please input n: '))
an = int(input('please input an: '))
m = int(input('please input m: '))
am = int(input('please input am: '))
k = int(input('please input k: '))

d = (am - an) // (m - n)
a1 = an - d * (n - 1)
ak = a1 + d * (k - 1)

print(ak)
