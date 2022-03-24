import random
import array
import re


print("Welcome To Our Strong Password Checker and Generator !!! ")
print("\n============================================================")
print("\nChoice 1: Test Wheather your Password is strong or not")
print("Choice 2: Create a Strong password")
c=int(input("Enter Your choice: "))

if(c==1):
    password = str(input("Please Enter Your Password: "))
    flag = 0
    while True:
    	if (len(password)<8):
    		flag = -1
    		break
    	elif not re.search("[a-z]", password):
    		flag = -1
    		break
    	elif not re.search("[A-Z]", password):
    		flag = -1
    		break
    	elif not re.search("[0-9]", password):
    		flag = -1
    		break
    	elif not re.search("[_@$]", password):
    		flag = -1
    		break
    	elif re.search("\s", password):
    		flag = -1
    		break
    	else:
    		flag = 0
    		print("Very Nice You Have a Strong Password")
    		break

    if flag == -1:
    	
        print("\nYou Do not Have a Strong Password !!! \nNo Problem \nYou Can Use Our Strong Password Generator")
        c = str(input("Want To Create a strong password (Yes or No) ? : "))
        
        
if(c==2 or c=='Yes' or c=='yes'):
    
    MAX_LEN = int(input("Enter the length of the password you want: "))

    
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
    					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    					'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
    					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    					'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
    		'*', '(', ')', '<']

    
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


    
    for x in range(MAX_LEN - 4):
    	temp_pass = temp_pass + random.choice(COMBINED_LIST)

    	
    	temp_pass_list = array.array('u', temp_pass)
    	random.shuffle(temp_pass_list)


    password = ""
    for x in temp_pass_list:
    		password = password + x
    		
    
    print("\nYour strong password of length",MAX_LEN, "is" ,password)

if(c=='no'or c=='No'):
    print("\nThank You For Using Our Strong Password Checker and Generator :)")  
    
    
        