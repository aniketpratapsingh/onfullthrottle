# On Full Throttle

## Deploy

To deploy this app with heroku. First make sure docker is running on your system(use docker ps). 
Then install heroku CLI.(if you don't already have it.)
Then run:

heroku login

heroku container:login

heroku create your-app-name
    
heroku container:push web -a your-app-name
    
heroku container:release web -a your-app-name
    
If you want to deploy this in any other docker container service. Just replace "$PORT" with 8000 in Dockerfile.

## Word search

The core logic behind the search is taking the wordlist as pandas dataframe then getting all the words in which the search word occur and taking the starting index of the occurance in another column of the dataframe. Then taking length of each work and storing it in another column. Then sorting the word first index of occurance then by length of the word and at last by frequency of use.


```python
import pandas as pd
```


```python
dataframe = pd.read_csv('./word_search.tsv',sep='\t',header=None)
```


```python
dataframe['index'] = dataframe[0].str.find('sheep')
```


```python
dataframe['len'] = dataframe[0].str.len()
```


```python
list(dataframe.loc[dataframe['index'] != -1].sort_values(by=["index","len",1],ascending=[True,True,False]).head(25)[0].dropna())
```




    ['sheep',
     'sheeps',
     'sheepy',
     'sheeple',
     'sheepdog',
     'sheepish',
     'sheepskin',
     'sheepdogs',
     'sheepfold',
     'sheephead',
     'sheepscot',
     'sheepishly',
     'sheepshead',
     'sheepskins',
     'blacksheep']




```python

```
