#!/usr/bin/env python3
# coding: utf-8
#
### Modules import
import json
from collections import Counter

### Variables initialization
score=0
total_questions=4

### Code
print('\n Python Quiz')
answer=input('\n Do you want to play this quiz ? : (yes/no) ')

if answer.lower()=='yes':

    with open('questionsAnswers.json', "r") as json_file:
        data = json.load(json_file)
        occurrences = data.count("question")
        print(occurrences)
        # c = Counter(item['question'] for item in data)
        for p in data['questionsAnswers']:
            answer=input('\n '+ p['question'])
            if answer.lower()==p['answer']:
                score+=1
                print('\n Right \n')
            else:
                print('\n Wrong \n')
    
    print(" Score =",score)
    note=(score/total_questions*100)
    print(' Response rate :',note,' % \n\n')

else:
    print("\n Have a good day ;-) \n\n")

### End

### Improvments :
# encrypt answer and decrypt in use : tried but not easy at seems
