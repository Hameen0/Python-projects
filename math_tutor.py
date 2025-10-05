print('Project - Math Tutor')
import random, time
number_of_ques= int(input('Enter the number of questions you want to answer: '))
highest_multiplier= int(input('Enter the highest numer you want to work with: '))
correct=[]
wrong=[]
time_taken=[]
ques_ans=[]

i=1
while i<=number_of_ques:
    x=random.randint(0,highest_multiplier)
    y=random.randint(0,highest_multiplier)
    
    start=time.time()
    u_answer=int(input(f'Q{i} Multiply {x}X{y}, input answer: '))
    ans=int(x*y)
    end=time.time()
    time_spent=round(end-start)
    time_taken.append(time_spent)
    
    ques_ans.append(f'{x}X{y}={ans} you input: {u_answer}')
   
    
    if u_answer==ans:
        correct.append(1)
        print('Correct')
    else:
        wrong.append(1)
        print('wrong answer')
        
    i+=1
    
print('Thank you for using the math calculator')
print(f' You got {sum(correct)}/{number_of_ques}')
print(f'{100*(sum(correct)/number_of_ques)}% correct')
print(f' it took you {sum(time_taken)} seconds to answer all questions')
for t,num in zip(time_taken, range(1, number_of_ques+1)):
     print(f' You spent {t}seconds in question{num}.')

for qans in ques_ans:
   print(qans)
