# 2016_Nov_28_text_collocation_counting
---------
###Counting how many collocations for each word in 于光中詩集 
---------
count_col(word,char[,feature1,feature2,feature3])
 * input: word char (pandas data frames)
          
 * a funciton counting the number of collocations in a script, adding a new column called "#collocations" to the data frame char, and saving the result to the column.
 * see fake_generate_LogNormal_crazy_version.ipynb for examples.
