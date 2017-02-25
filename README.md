# 2016_Nov_28_text_collocation_counting
---------
###Counting how many collocations for each word in 于光中詩集
###Counting how many edges between each word in "蛙"
---------
##Function Specs.
count_col(word,char[,feature1,feature2,feature3])
 * input: word char (pandas data frames)
          
 * a funciton counting the number of collocations in a script, adding a new column called "#collocations" to the data frame char, and saving the result to the column.
 * download count_col.py to your desktop, save it to the same folder where the .ipynb files exist. 
 * see fake_generate_LogNormal_crazy_version.ipynb for examples.
 * download count_col.py to your desktop, save it to the same folder where the .ipynb files exist.
 * don't forget to put 
 'from count_col import count_col'
 to the top of your code!
 
count_edges(word[,feaure])
  * input: word (pandas data frames)
  * a funciton counting the number of edges in a script, adding a new column called "#edges" to the data frame word, and saving the result to that column.
  * count_edges has been added to count.py file.
 
