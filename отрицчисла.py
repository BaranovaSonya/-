chislo = int(input())
dvoi = ''
while chislo > 0 :
  dvoi = str(chislo%2) + dvoi
  chislo = chislo//2
print (dvoi)

