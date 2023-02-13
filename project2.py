'''
Escreva um programa que, ao iniciar gera um valor
aleatório de 1 a 10 e permite que o usuário chute um
número até que o valor aleatório gerado no início do
programa seja chutado corretamente. O programa deve
informar caso o chute tenha sido acima, abaixo ou igual
ao valor aleatório gerado no início do programa.

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- valor aleatorio de 1 a 10
- chute do usuario
2. O que devo fazer com estes dados?
-  Eu devo comparar o chute do usúario com o valor aleatório que foi gerado no inicio do programa e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no inicio do programa.
3. Quais são as restrições deste problema?
-  Um valor aleatório de 1 a 10
4. Qual é o resultado esperado?
- Informar caso o chute tenha sido acima, abaixo ou igual
ao valor aleatório gerado no início do programa.
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado ?
input valor aleatorio de 1 a 10
input chute
  if chute > valor aleatorio 
  print chute é maior que o valor gerado 
  if chute < valor aleatorio
  print chute é menor que o valor gerado
  if chute = valor gerado
  print você acertou !!!
'''
import random 

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('Chute é maior que o valor gerado ')
  elif chute < valor_aleatorio:
    print('Chute é menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você Acertou !!!')

  