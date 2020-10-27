#!/usr/bin/env python
# coding: utf-8

# In[192]:


import os
import pandas as pd
import numpy as np
import re
from textblob import TextBlob
import nltk
#corpus
nltk.download('punkt')
#merged DataFrame to be used in each function
totdf = pd.DataFrame(columns = ['Name:','Purpose:'])
files = []


def main():
    return 0 
def mergeData():
    #local dataframe
    mtotdf = pd.DataFrame(columns = ['Name:','Purpose:'])
    #array of files within this directory
    files = os.listdir()
    for f in files:
        #logic for all text files
        if 'txt' in f:
            file = open(f,'r')
            #splitting text file into individual lines that go into an array
            dataframe = file.read().splitlines()
            #specific logic for individual file
            if f == 'hw2a2.txt':
                #use --- as delimeter
                dataframe = [re.split('---',x) for x in dataframe]
                #popout array of array into one array
                dataframe = [item for elem in dataframe for item in elem]
            #delete empty entries
            dataframe = [x for x in dataframe if x]
            #create a dataframe that has 2 columns (reshape) while deleting all special characters and deleting Name and Purpose while creating columns for Name and Purpose 
            df = pd.DataFrame(np.reshape(np.array([re.sub(r"[^a-zA-Z0-9]+", ' ', x.replace('Name','').replace('Purpose','')) for x in dataframe]),(-1,2)), columns = ['Name:','Purpose:'])
        
        
        #csv logic
        elif 'csv' in f:
            df = pd.read_csv(f)
            #logic for csv with index as first column
            if len(df.columns) == 3:
                df = df.drop(columns = 'Unnamed: 0')
            columns = df.columns.values
            #standardize column names
            df = df.rename(columns = {columns[0]:'Name:',columns[1]:'Purpose:'})
        else:
            df = pd.DataFrame(columns = ['Name:','Purpose:'])
        mtotdf = mtotdf.append(df,ignore_index = True)
    
    #make global df equal to local df
    global totdf 
    totdf = mtotdf
    return 'Data has been merged'
       


def sentimentAnalysis(sentimentcolumn, keycolumn):
    global totdf
    #polarity ranges from -1 (negative) to 1 (positive)
    polarity = []
    #subjectivity ranges from 0 (factual in messaging) to 1 (mostly opinion phrases)
    subjectivity = []
    index = 0
    #iterating through global dataframe for specified column
    for x in totdf[sentimentcolumn]:
        phrase = TextBlob(x)
        #Textblob values for polarity and sentiment are put in seperate arrays
        polarity = polarity + [phrase.sentiment.polarity]
        subjectivity = subjectivity  + [phrase.sentiment.subjectivity]
    #after iteration these arrays are added to the dataframe
    totdf['subjectivity'] = subjectivity
    totdf['polarity'] = polarity
    #bestsentiment is based on the highest polarity with the lowest subjectivity (most positive and most factual)
    bestsentiment = totdf[sentimentcolumn].iloc[totdf.sort_values(by = ['polarity','subjectivity'], ascending = [False,True]).index[0]]
    #key is returned as well to say which company in this case has that purpose
    bestkey = totdf[keycolumn].iloc[totdf.sort_values(by = ['polarity','subjectivity'], ascending = [False,True]).index[0]]
    return bestsentiment, bestkey

def mostUsedTokens(num, column):
    global totdf
    tottokens = []
    #iterate through dataframe for a given column
    for x in totdf[column]:
        #iterate through each purpose in order to retrieve individual words
        for token in TextBlob(x).words:
            tottokens = tottokens + [token]
    #put tokens into dataframe
    tokendf = pd.DataFrame(tottokens,columns = ['Tokens'])
    #use value_counts to find the top num amount of tokens within that column
    topnum = tokendf['Tokens'].value_counts()[:num]
    #return the array of tokens with their values
    return topnum

if __name__ == "__main__":
    main()


