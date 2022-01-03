def principal():
    num = int(input('Forneça um número entre 0 e 999:'))
    if num < 0 or num > 999:
        print('Não sei o valor por extenso')
    else:
        print('Número por extenso é ' + extenso(num))
  
def extenso(n):
  u = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
  d1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
  d2 = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
  c = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']      
  
  if n >= 100:
    return cetenas(n,u,d1,d2,c)
  elif n >= 10:
    return dezenas(n,u,d1,d2)
  elif n < 10:
    return unidades(n,u)
    
def cetenas(n_,u_,d1_,d2_,c_):
  if n_ == 100:
    return "cem"
  else:
      snum = str(n_)
      
      centena = snum[0]
      dezena = snum[1]
      unidade = snum[2]
      
      m = c_[int(centena)]
      
      ultimos = int(dezena + unidade)
      
      if ultimos < 10:
        if ultimos == 0:
          return m#duzentos, trezentos..
        else:
          return m + " e " + unidades(int(unidade),u_)#102,101...
   
      return m + " e " + dezenas(ultimos,u_,d1_,d2_)
      
def dezenas(n_,u_,d1_,d2_):
  snum = str(n_)
  dezena = snum[0]
  unidade = snum[1]
      
  i1 = d1_[int(unidade)]
  i2 = d2_[int(dezena)]
  
  if n_ < 20:
    return i1
  else:  
    if int(unidade) != 0:#21,26,35...
      return i2 + " e " + unidades(int(unidade),u_)
    else:#20,30,40...
      return i2
    
def unidades(n_,u_):  
  if n_ == 0:
    return "zero"    
  else:
    return u_[n_]
    
principal()