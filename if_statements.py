#implementing elif statement for a simpler and more readable program

def class_scores():
    score = eval(input('Enter your score: '))
    if score >= 90:
        print('Your grade is A, Excellent!!!')
    elif score >= 80:
        print('Your grade is B, Very Good!!')
    elif score >= 70:
        print('Your grade is C, Good!')
    elif score >= 60:
        print('Your grade is D, Work hard')
    else:
        print('Your grade is F, FAIL')
class_scores()

''' Results:
Enter your score: 95
Your grade is A, Excellent!!!  
Enter your score: 80
Your grade is B, Very Good!!
Enter your score: 30
Your grade is F, FAIL '''                             
    
    
