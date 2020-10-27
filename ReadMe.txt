READ ME ----------------------------------------------------


main()
No changes just remember to add os.chdir() if your files are not in the same directory as this script
global totdf will need to reflect the columns in which you plan on merging



mergeData()
Will use logic to merge csv and txt files using a similar format. You can change the individual code logic for if 'txt' or if 'csv' to match what your new files have
mtotdf & df will need to reflect the colums in which you plan on merging

sentimentAnalysis(sentimentcolumn, keycolumn)

**inputs**
sentimentcolumn = whatever dataframe column you would like to run sentiment on
keycolumn = key that is associated with that record

example for this HW sentimentAnalysis('Purpose:','Name:')
can change these variables to output more than one record if needed using last 2 iloc commands

**output**
best sentiment , best key, worst sentiment, worst key(of highest & lowest both)




mostUsedTokens(num, column)

**inputs**
num = how many tokens you want to retrieve
column = which column you would like to get the tokens from

example for this HW mostUsedTokens(10, 'Purpose:')

**output**
an array of value_counts() which shows the token and amount it shows up
