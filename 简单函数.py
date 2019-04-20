# -*- coding: utf-8 -*-
"""
@author: Yaxin LI
"""
#############################################################
#简单函数
#############################################################

#1. 单位转换
def convert():
    """ The function will prompt for the input, check for
    valid numeric positive input (not a string and not 0) and give error feedback if it's not 
    valid. It will print the value in stones if the input was a valid number and return the result.
    """
    
    err_msg1 = "Error: You must enter a positive number!"
    err_msg2 = "Error: You must enter a number!"
    
    prompt = "Enter a weight in pounds:"
    kilos = input(prompt)
    try:
        stones = float(kilos) * 0.157473  # float, not int!
        if stones <= 0:
            print(err_msg1)
            return   # return nothing
        print("Your input is equal to " + str(stones) + " stones.")
        return stones  # return the answer
    except:
        print(err_msg2)
        return  # return nothing

    
convert()




#2. 生成随机数
import random

def get_rand_int(arg1, arg2):
    """ Takes 2 integer arguments, and returns a random integer between them.
    Return None if the arguments aren't 2 different integers.
    """   
    if type(arg1) != int or type(arg2) != int:
        return None    
    if arg1 == arg2:
        return None        
    return random.randint(arg1, arg2)

def print_random():
    """ Prompt the user to input an integer > 0, and return a random integer between 0 and
    their input value.  Print the required error if their input is not appropriate.
    """
    prompt = "Please enter an integer greater than 0:"
    err_msg = "Invalid input: You must input an integer greater than 0 for your input."

    arg2 = input(prompt)   
    try:
        arg2 = int(arg2)  # try to convert to an int.
    except:
        print(err_msg)
        return 
    if arg2 <= 0:
        print(err_msg)
        return 

    #double check
    result = get_rand_int(0, arg2)
    if result != None:
        print("Your random number is " + str(result))
        return result
    else:
        print(err_msg)
        return 

print_random()




#3. 计算连续复利
def compound_interest(principal, rate, years):    
    '''
    Return the compound interest after 'years' from an original 'principal' at a nominal interest 'rate' 
    '''
    assert principal >= 0, "positive placement"
    assert rate >= 0, "positive interest rate"
    assert years > 0, "strictly positive number of years"
    assert type(years) == int, "integer number of years"
    return principal * ((1 + rate) ** years - 1)

compound_interest(1000, 0.02, 5)




#4. 对原字典的数值型value增加一个定值
def addtovalue(dictionary):
    '''
    Add one to each numeric value of the dictionary, return the dict.
    '''
    dictionary_new={}
    for key,value in dictionary.items():
        try:
            dictionary_new[key]=dictionary[key]+1
        except:
            dictionary_new[key]=dictionary[key]
    return dictionary_new

testdict = { 'fred': 3.3, 'marie': '5', 'jean': 14, 'angus': 44, 'amine': None}

result = addtovalue(testdict)
result