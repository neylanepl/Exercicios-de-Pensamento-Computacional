diasTotais = int(input("Quantos dias se passaram?"))


if diasTotais == 0:
  print("Isto equivale a nenhum dia")
elif diasTotais == 1:
  print("Isto equivale a " + str(diasTotais) + "dia")
elif diasTotais == 7:
  print("Isto equivale a " + str(int(diasTotais/7)) + " semana")
elif (diasTotais // 7) == 0:
  print("Isto equivale a " + str(diasTotais) + " dias")
elif (diasTotais % 7) == 0:
  semana = int(diasTotais / 7)
  print("Isto equivale a " + str(semana) + " semanas")
else:
  semana = int(diasTotais / 7)
  dia = diasTotais - (semana * 7)
  if semana == 1 and dia == 1 :
    print("Isto equivale a " + str(semana) + " semana e " + str(dia) + " dia ")
  elif semana > 1 and dia == 1:
    print("Isto equivale a " + str(semana) + " semanas e " + str(dia) + " dia ")
  elif semana == 1 and dia > 1:
    print("Isto equivale a " + str(semana) + " semana e " + str(dia) + " dias ")
  else:
    print("Isto equivale a " + str(semana) + " semanas e " + str(dia) + " dias ")
