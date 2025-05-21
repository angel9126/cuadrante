x = int (input("ingrese el valor de X:"))
y = int (input("ingrese el valor de y:"))
if  ((x > 0) and (y > 0)):
  print ("punto en el primer cuadrante");
elif((x > 0) and (y < 0)):
  print ("punto en el segundo cuadrante");
elif((x < 0) and (y < 0)):
  print("punto en el tercer cuadrante");
elif ((x < 0) and (y > 0)):
  print("punto en el tercer cuadrante");
else:
  print("punto en el origen")
  
