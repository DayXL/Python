from random import randint

quad = [] #usei lista para representar a matriz, então em vez de quad[i][j], terá quad[i]
i = 1
vdd = False
cont = 0

print('Quadrado mágico')
print()

while vdd == False: #enquanto não achar, ele roda
  while i <= 9: 
    num = randint(1,9)
    if num not in quad: #se o número sorteado não tiver na lista 'quad', ele irá entrar nela, e o contador(i) andará um
      quad = quad + [num]
      i = i + 1  
  
  if i > 9: #após sortear os 9 números, entrará nesse if para comparações
    cont = cont + 1 #contador para ver quantos quadrados precisou até chegar no certo
    if quad[0] + quad[1] + quad[2] == 15: #cada if analisa as possibilidades de soma 15, ao todo são 8, está em forma quad[], pq usei lista
      vdd = True
    else:
      vdd = False
        
    if vdd == True and quad[3] + quad[4] + quad[5] == 15:
      vdd = True
    else:
      vdd = False 
        
    if vdd == True and quad[6] + quad[7] + quad[8] == 15:
      vdd = True
    else:
      vdd = False
        
    if vdd == True and quad[0] + quad[3] + quad[6] == 15:
      vdd = True
    else:
      vdd = False
  
    if vdd == True and quad[1] + quad[4] + quad[7] == 15:
      vdd = True
    else:
      vdd = False
  
    if vdd == True and quad[2] + quad[5] + quad[8] == 15:
      vdd = True
    else:
      vdd = False
  
    if vdd == True and quad[0] + quad[4] + quad[8] == 15:
      vdd = True
    else:
      vdd = False
  
    if vdd == True and quad[2] + quad[4] + quad[6] == 15:
      vdd = True
    else:
      vdd = False
  
  if vdd == False and i > 9: #se após sair do if anterior, a variavel vdd ainda for falsa, e o contador(i) do segundo while for maior q 9, ele irá resetar o contador(i), e irá deixar a lista quad vazia, assim poderá rodar novamente até achar
    i = 1
    quad = []
  else:
    i = 12
    vdd = True
      
print('Precisou de' , cont , 'tentativas.')
print()

for i in range(len(quad)): #printa a lista em forma de matriz
  if i == 3 or i == 6:
    print()
  print(quad[i] , end = ' ')

    





  