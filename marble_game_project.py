import random   #To randomize the betting game
items=['red marble','green marble']

bag=[]
for element in items:       #to make the bag of 4red and 6green
    bag.extend([element]*4)
bag.append('green marble')
bag.append('green marble')
bag[-1]='black marble'  #To replace one green marble with black one
bag[0]='white marble'   #To replace one red marble with white one
total_drawings= 3       #the total round on can play
round=0             #this is the rounds played and will be updated in the loop
money= 1000         #the money the player starts with
result=''       #Message after each round and will be updated in loop

    #while loop with condition that game end if money became half
while money>500:
#for loop to specify the number of rounds to be played
    for drawings in range(1,(total_drawings+1)):
        round=round+1   
        bet=int(input(f'{result}Round{round}\nHow much are you betting? You have {money}$: '))
        draw= random.choice(bag)    #To randomize the drawinngs
        if draw=='green marble':
            money=money+bet
            result=(f'Congratulations! You draw {draw}. You won {bet}$\n')
           
        if draw=='black marble':
            money=money+(bet*10)
            result=(f'Congratulations! You draw {draw}. You won {bet*10}$\n')

        if draw=='white marble':
            money=money-(bet*5)
            if money>500:
                result=(f'Oops! You draw {draw}. You lose {bet}$\n')
                
            else:
                result=(f'Game Over!! You draw {draw}. You lose {bet}$\n')
                print(f'{result}See you next time.')
                break   #break to leave the loop as the condition of game end
            
                
        if draw=='red marble':
            money=money-bet
            if money>500:
                result=(f'Oops! You draw {draw}. You lose {bet}$\n')
                
            else:
                result=(f'Game Over!! You draw {draw}. You lose {bet}$\n')
                print(f'{result}See you next time.')
                break
            
    
   

print(f'You\'ve completed this round\nYou have {money}$ left')
print(f'You played {round} rounds')
#print(bag)
#print(f'You have {len(bag)}marbles in your bag')
