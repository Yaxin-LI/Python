# -*- coding: utf-8 -*-
"""
@author: Yaxin LI
"""
#############################################################
#文件读取与数据处理
#############################################################

import os
os.chdir(r'C:\Users\lenovo\Desktop\Python\attachments')


#1. 从txt文件中读取并统计网址数目
def count_urls(filename):
    """
    Pass in the full path to the file you are searching for URLs.
    Return the total of lines with urls found.
    """
    with open(filename, 'r') as handle:
        count=0        
        # TYPE YOUR CODE HERE.
        for line in handle:
            start_index=line.find("http")
            if start_index==-1:continue
            else:
                count=count+1
                end_index=line.find(" ",start_index)#line.find(strings, begin, end)
                string=line[start_index:end_index]
                string=string.rstrip(")")    
                print(string)

        return count
    
    
filepath = 'mbox-short.txt'
count_urls(filepath)




#2. 统计文件中的词数
from collections import defaultdict
filename = "romeo.txt"
wordcounter = defaultdict(int)

try:
    fhand = open(filename)
except:
    print("File wasn't found or the name is wrong. It has to be in this directory with the notebook.")
    
for line in fhand:
    words = line.split()
    for word in words:
        wordcounter[word] += 1  # this is the same as wordcounter[word] = wordcounter[word] + 1

# print pairs for each dict element: the key and value
for key, val in wordcounter.items():   # items returns a pair for each dict element, the key and value.
    print(key, val)
    
fhand.close() # if doesn't open the file without a "with open(filen) as x:" line, we need to close it manually.




#3. 利用counter 计数

def open_a_file(filename):
    try:
        fhand = open(filename)
        return fhand
    except:
        return None  # if there is an error opening the file


from collections import Counter  # import the Counter


def get_counts(filehandle):
    """ 
     The function will take your filehandle and count the words in the file.
    """
    allwords = []
    for line in fhand:
        words = line.split()
        allwords = allwords + words  # add the words to the list of all words -- this prevents embedded lists
    mycount = Counter(allwords)  # a list of words
    return mycount

fhand = open_a_file("romeo.txt")
if fhand:  # if it didn't return "None"(no error)
    counts = get_counts(fhand)

print("All words in the counter dictionary ordered by frequency:", counts.most_common())  # might be long, beware!
print("Top 5 words", counts.most_common(5))




#4. 读取山峰数据并输出
import pandas as pd
filename = "mountains.csv"
def mountain_height(filename):
    """ Read in a csv file of mountain names and heights.  
    Parse the lines and print the names and heights. 
    Return the data as a dictionary. 
    The key is the mountain and the height is the value.
    """

    mountains = dict()
    msg = "The height of {} is {} meters."
    err_msg = "Error: File doesn't exist or is unreadable."
    t=[]
    try:
        with open(filename, 'r') as handle:
            for line in handle:
                line = line.rstrip("\n")
                t=t+line.split(",")
                for i in t:
                    if '' in t:
                        t.remove('')
                        #print(t)
            for i in range(len(t)):
                if i%3==0:
                    mountains[t[i]]=int(t[i+1])
            for key,value in mountains.items():
                print(msg.format(key,value))
            return mountains
    except:
        print(err_msg)
        return None

    
mountains=mountain_height(filename)




#5. 统计山峰数；输出平均高度
from collections import Counter
from collections import defaultdict
from statistics import mean   # this also exists in numpy if you prefer

def mountain_ranges(filename):
    
    msg = "The average height of {} is {} meters."
    err_msg = "Error: File doesn't exist or is unreadable."
    mountains = dict()
    t=[]
    newlist=[]
    try:
        with open(filename, 'r') as handle:
            for line in handle:
                line = line.rstrip("\n")
                t=t+line.split(",")
                for i in t:
                    if '' in t:
                        t.remove('')
                        #print(t)
            for i in range(len(t)):
                if i%3==2:
                    key=t[i]
                    value=int(t[i-1])
                    mountains.setdefault(key,[]).append(value)
                    newlist.append(key)
                c=Counter(newlist)
            print(c.most_common(2))
            
            
            #print the mean
            for key,value in mountains.items():
                a=value
                print(msg.format(key,mean(a)))
                    
            #return
            return mountains
    except:
        print(err_msg)
        return None
    
mountain_ranges("mountains.csv")
mountain_ranges("highest_mountains.csv")




