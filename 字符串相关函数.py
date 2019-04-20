# -*- coding: utf-8 -*-
"""
@author: Yaxin LI
"""
#############################################################
#字符串相关函数整理
#############################################################

#1.大写元音字母
def uppercase(word):
    vowels = "aeiou"   
    nothing_msg = "Nothing to convert!"

    count=0
    if word.isalpha()==True:
        t=list(word)
        for i in range(len(t)):
            if (t[i] in vowels)==True:
                t[i]=t[i].upper()
        msg="".join(t)
        if msg!=word:
        #already converted
            print(msg)
            return msg
        else:
            print(nothing_msg)  
            return None
    else:
        print("Error: you should enter string without spaces")
        return None
 
    
print(uppercase("well hello there"))
print(uppercase("hello"))
print(uppercase("HI"))




#2. 字符串清理
def clean_words(wordlist):
    """ Takes a list of strings and capitalizes words, removes blank spaces around any of them.
    Returns a cleaned list."""
    # TYPE YOUR CODE HERE.
    length=[]#empty list
    for i in range(len(words)):
        words[i]=words[i].strip()
        words[i]=words[i].capitalize()
        length=length+[len(words[i])]
    print (words)
    print (length)
    return words


words = ['34', 'fred  ', '25', '35.5', '24', 'india']
clean_words(words)




#3. 取出特定格式字符串中的数字
def get_number(stringinput):
    """ 
    Your stringinput should be characters+":"+numbers. The function will print the float part after the :
    and also return it.
    """
    
    index=stringinput.find(":")
    index=index+1
    try:
        number=float(stringinput[index:])
        return number
    except:
        return None
    
    
mystring = 'X-DSPAM-Confidence:0.8475'
get_number(mystring)




#4.由列表生成字符串
def print_string(wordlist):
    # TYPE YOUR CODE HERE.
    delimiter=" "
    output=delimiter.join(words)
    print(output)    
    

words = ["Yes", "Dave", "I", "can", "do", "that!"]
print_string(words)



#5. 用户输入许多姓名，函数将找出最长及最短姓名；遇到特定名称即结束
def bob_loop():
    bob_msg = "oh, not you, Bob!"
    other_msg = "Hi {name}! Good to see you!"  
    longest_msg = "Longest name was {longest_name}" 
    shortest_msg = "Shortest name was {shortest_name}"
    error_msg = "Error: you must enter a string!"
    longest_name = ""
    shortest_name = "justgiveshortestnameastring"
    while True:
        name=input("Please enter your name:")
        if name.isalpha()==False:
            print(error_msg)
        else:
            if name !="Bob":
                print(other_msg.format(name=name))
                if len(name)>len(longest_name):
                    longest_name=name
                if len(name)<len(shortest_name):
                    shortest_name=name
            else:
                print(bob_msg)
                print(longest_msg.format(longest_name=longest_name),";",shortest_msg.format(shortest_name=shortest_name))
                break
                
bob_loop()


