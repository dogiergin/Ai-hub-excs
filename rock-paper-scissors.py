import random

tkm= ['taş','kağıt','makas']

player1numb=0
player2numb=0
steps=0


while player1numb +player2numb<5:
  steps+=1
  player1_choice=random.choice(tkm)
  player2_choice=random.choice(tkm)
  print(player1_choice+'\t'+player2_choice+'\t'+str(player1numb)+'\t'+str(player2numb))
  if player1_choice==player2_choice:
    continue
  elif player1numb==3 or player2numb==3:
    break
  elif player1_choice== 'taş' and player2_choice == 'makas':
    player1numb +=1
  elif player1_choice=='makas' and player2_choice == 'kağıt':
    player1numb +=1
  elif player1_choice == 'kağıt' and player2_choice == 'taş':
    player1numb +=1
  else:
    player2numb+=1

if player1numb==player2numb:
  print('draw nobody wins \n'+str(player1numb) +'\t'+ str(player2numb))

elif player1numb<player2numb:
  print('player2 won in {} steps \t'.format(steps)+ str(player2numb)+'\t'+ str(player1numb))
else:
  print('player1  Won in {} steps \t'.format(steps) + str(player1numb)+'\t'+str(player2numb))
