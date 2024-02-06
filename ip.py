print("chceš počítat binarni do des 1 nebo des do bin 2")

vyber = int(input("váš výber: "))

if vyber == 1 :

    print("vybral jsi si převod z binární do dec.")

elif vyber == 2 :
  
   print("vybra jsi si převod z desítkové do dvojkové:")
    
   cislo = int(input("Zadej desítkové číslo: "))
   
   x = cislo
   seznam = []

   while x != 0:
     zbytek = x / 2
     seznam.append(zbytek)
     for i in range(start, stop, krok): 
      x = x // 2
     start = len(seznam) - 1
     stop = -1
     krok = -1

     print(seznam[i], end = "")