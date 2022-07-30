import os
import pacient
import refeicao
import aliment0
import informacoes
import relatorios

def menuPrincipal():
  os.system('clear')
  print('==============================================')
  print('================== DIETPLAN ==================')
  print('==============================================')
  print()
  print('\t1 - Menu paciente')
  print('\t2 - Menu alimento')
  print('\t3 - Menu refeição')
  print('\t4 - Informações do projeto')
  print('\t5 - Relatórios')
  print('\t0 - Finalizar programa')
  print()
  print('==============================================')
  esc = input('Selecione sua opção: ')
  return esc
  
#  os módulos que chamam as funções, por isso eles estão em baixo e não em cima delas
# serve para ler uma nova opção - é um incremento no while  
#Módulo principal:
esc = menuPrincipal()
while esc != '0':
  if esc == '1':
    pacient.moduloPaciente()

  elif esc == '2':
    aliment0.moduloAlimento()
    
  elif esc == '3':
    refeicao.moduloRefeic()
    
  elif esc == '4':
    informacoes.moduloInformacoes()

  elif esc == '5':
    relatorios.moduloRelatorios()
    
  else:
    print('Seleção inválida') 
  print()
  
  esc = menuPrincipal()

print()
print('Programa finalizado')

