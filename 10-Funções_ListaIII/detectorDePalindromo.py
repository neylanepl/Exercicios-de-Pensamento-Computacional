def principal():  
  texto = input("Digite o texto:")
  
  textj = ""
  for i in texto:
    if i != " ":
      textj = textj + i
  
  print("O inverso de '" + textj + "' é '" + inverso(textj) + "'")
  
  if textj == inverso(textj):
      print("Temos um palíndromo!")
  else:
      print("NÃO temos um palíndromo!")

def inverso(t):
  cont = len(t)
  invertido = ""
  for j in range(cont-1,-1,-1):
    invertido = invertido + t[j]
    
  return invertido
  

principal()
