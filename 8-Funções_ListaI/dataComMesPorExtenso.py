def data_extenso(d,m,a):
  d = int(d)
  m = int(m)
  a = int(a)
  
  if (m % 2 != 0 and m <= 7) or (m % 2 == 0 and m >= 8):
    contDiasMes = 31

  elif m == 2:
  
    if a % 4 == 0:
      if a % 100 == 0: #1900 é divisivel por 100, mas não é por 400 e não é bissexto
        if a % 400 == 0:
          quantDiasAno = 366
        else:
          quantDiasAno = 365
      else:
          quantDiasAno = 366
    else:
      quantDiasAno = 365
    #
    if quantDiasAno == 366:
      contDiasMes = 29
    else:
      contDiasMes = 28
  else:
    contDiasMes = 30


  if d >= 1 and d <= contDiasMes:
    if m >= 1 and m <= 12:
        lista = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        m = lista[m-1]
        return (str(d) + " de " + m + " de " + str(a))
  
  return "Data inválida!"

dia, mes, ano = input("Data no formato DD/MM/AAAA?").split('/')
print(data_extenso(dia,mes,ano))