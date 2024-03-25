#Author - Anusara N. Gunaratna
# I declare that my work contains no examples of misconduct, such as plagiarism, or Any code taken from other sources is referenced within my code solution. 
# Student ID(UoW): w1953613
# Student ID(IIT) : 20221021 
# Date:14th of December 2022  
#PART 4
'''
Design

Enter student ID
if student ID start with 'w' and there are 7 digits after  
    Enter the credits at pass
        Check if the input is an integer and if the input is within the range
        If not re-enter 
    Enter the credits at defer
        Check if the input is an integer and if the input is within the range
        If not re-enter 
    Enter the credits at fail
        Check if the input is an integer and if the input is within the range
        If not re-enter
    Check if pass credits + defer credits + fail credits = 120
    if not re-enter from the beginning
    If pass credits = 120
        Print Progress
        Append the credits to the list
        
    If pass credits = 100
        Print Progress (module trailer)
        Append credits to the list
    If pass credits >=0 and credits fail<80 
        Print Module retriever
        Append the credits to the list
    Else 
        Print Exclude
        Append the credits to the list
        
    Update the credits as the value and student ID as the key to the dictionary
    
    While True:
        Enter ‘y’ to re enter or ‘q’ to quit
        If input is ‘y’
            Continue(Back to the top)
        Elif input is ‘q’ 
            Print the histogram
            Display the progression outcome with credits at pass, defer and fail
            Transfer the outcome to a text file
            Display Dictionary 
        Else
            Print Invalid input
            Continue(Back to enter ‘y ’ or ‘q’)
    End while

'''

progress=0 
trailer=0
retriever=0
excluded=0
end=None
list_final=[]
global dict_insert
dict_insert={}

def validate(user_input):       #user-define function for validation
    while True:
        try:
            value=int(input('Please enter your credits at '+user_input+':'))
            input_value=[0,20,40,60,80,100,120]
            if value in input_value:
                list_credits.append(value)
                return value
            else:
                print('Out of range\n')
                continue
        except ValueError:
            print('Integer required\n')
            continue
            

def histogram(asterisks,progression_name):      #user-define function for the histogram
    print(progression_name,asterisks,':',end='')
    for count in range(asterisks):
        print('*',end='')
    print('\n',end='')

def list_insert(name):      #user-define function for the list and the dictionary
    list_credits.insert(0,name)
    x=(f'{list_credits[0]}')   
    y=list_credits[1]
    z=list_credits[2]
    a=list_credits[3]
    dict_insert[student_id]=(f'{x} {y}, {z}, {a} ')
    list_final.append(list_credits)

def text_file():        #user-define function for transfering the data into a text file
    with open('Progression Outcomes_part 4.txt','a')as file:
        file.write(str(list_final[count][0]))
        file.write(str(list_final[count][1]))
        file.write(' , ')
        file.write(str(list_final[count][2]))
        file.write(' , ')
        file.write(str(list_final[count][3]))
        file.write('\n')

def main_1():       #part 1 program 
    global list_credits
    list_credits=[]
    while True:
        credits_pass=validate('pass')
        credits_defer=validate('defer')
        credits_fail=validate('fail')
        if credits_pass + credits_defer + credits_fail== 120:
            if credits_pass==120 :
                print('Progress')
                list_insert('Progress -')
                global progress
                progress+=1 
            elif credits_pass==100:
                print('Progress (module trailer)')
                list_insert('Progress (module trailer) -')
                global trailer
                trailer+=1 
            elif credits_pass>=0 and credits_fail<80 :
                print('Module retriever')
                list_insert('Module retriever -')
                global retriever
                retriever+=1 
            else:
                print('Exclude')
                list_insert('Exclude -')
                global excluded
                excluded+=1
            list_credits=[]         
        else:
            print('Total incorrect\n')
            list_credits.clear()
            continue
        break



while True:     #main program
    student_id=input('Please enter your student ID :')
    if student_id.startswith('w'):
        if len(student_id)==8 and student_id[1:9].isdigit()==True:
            if student_id not in dict_insert:
                print('\n')
                main_1()
                while True:
                    re_enter=str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: "))
                    if re_enter.lower()=='y':
                        print('\n')
                        break
                    elif re_enter.lower()=='q':
                        end=True
                        print('--------------------------------------------------------')
                        print('Histogram')
                        histogram(progress,'Progress ')
                        histogram(trailer,'Trailer  ')
                        histogram(retriever,'Retriever')
                        histogram(excluded,'Excluded ')
                        print('\n',progress+trailer+retriever+excluded,'outcomes in total.')
                        print('--------------------------------------------------------')

                        with open('Progression Outcomes_part 4.txt','w')as file:
                            file.write('Part 3:\n')
                        
                        print('Part 2:')
                        for count in range(len(list_final)):
                            print(list_final[count][0],list_final[count][1],',',list_final[count][2],',',list_final[count][3])
                            text_file()

                        print("\nPart 3:\nText file has been created under the name 'Progression Outcomes_part 4'")
                            
                        print('\n')    
                        print('Part 4:')
                        print(*[str(k) + ' : ' + str(v) for k,v in dict_insert.items()])
                        break
                    else:
                        print('Invalid input')
                        continue
                if end==True:
                    break
                else:
                    continue
            else:
                print('This Student_ID already exists.\n')
                continue
        else:
            print("Student ID must contain 7 digits after letter 'w', Please try again!\n")
            continue
    else:
        print("Student ID should start with letter 'w', please try again!\n")
        continue


