import random

def jogo():
    numeroAdvinha = random.randint(1,50)
    numeroPessoa =  int(input("Digite um numero de 1 a 50: "))
    if (1 <= numeroPessoa <= 50 ):
        if (numeroAdvinha == numeroPessoa):
            print("Parabens você advinhou o numero!!!")
        else:
            print("Numero errado,", numeroAdvinha,"era o numero correto" )
    else:
        print("Numero digitado incorreto!")
def explicacao():
    print("No jogo você tera que advinhar um numero de 1 a 50")

n = 1000
while n != 0:
  print('\n<===================== Jogo da Advinhção ========================>')
  print("1 - Iniciar Jogo")
  print("2 - Como Jogar\n")
  print("0 - SAIR")
  print('<========================= by Jose Felipe ============================>\n')
  n = int(input("Digite a opção desejada: "))
  if n==1:
    jogo()
  elif n==2:
    explicacao()
  elif n==0:
    print("Obrigado por jogar")
    break
  else:
      print("\nOpção invalido")

