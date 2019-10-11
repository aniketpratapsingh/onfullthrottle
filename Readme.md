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
dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>the</td>
      <td>23135851162</td>
    </tr>
    <tr>
      <td>1</td>
      <td>of</td>
      <td>13151942776</td>
    </tr>
    <tr>
      <td>2</td>
      <td>and</td>
      <td>12997637966</td>
    </tr>
    <tr>
      <td>3</td>
      <td>to</td>
      <td>12136980858</td>
    </tr>
    <tr>
      <td>4</td>
      <td>a</td>
      <td>9081174698</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>333328</td>
      <td>gooek</td>
      <td>12711</td>
    </tr>
    <tr>
      <td>333329</td>
      <td>gooddg</td>
      <td>12711</td>
    </tr>
    <tr>
      <td>333330</td>
      <td>gooblle</td>
      <td>12711</td>
    </tr>
    <tr>
      <td>333331</td>
      <td>gollgo</td>
      <td>12711</td>
    </tr>
    <tr>
      <td>333332</td>
      <td>golgw</td>
      <td>12711</td>
    </tr>
  </tbody>
</table>
<p>333333 rows × 2 columns</p>
</div>




```python
dataframe['index'] = dataframe[0].str.find('sheep')
```


```python
dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>index</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>the</td>
      <td>23135851162</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>of</td>
      <td>13151942776</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>and</td>
      <td>12997637966</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>to</td>
      <td>12136980858</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>a</td>
      <td>9081174698</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>333328</td>
      <td>gooek</td>
      <td>12711</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>333329</td>
      <td>gooddg</td>
      <td>12711</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>333330</td>
      <td>gooblle</td>
      <td>12711</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>333331</td>
      <td>gollgo</td>
      <td>12711</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <td>333332</td>
      <td>golgw</td>
      <td>12711</td>
      <td>-1.0</td>
    </tr>
  </tbody>
</table>
<p>333333 rows × 3 columns</p>
</div>




```python
dataframe['len'] = dataframe[0].str.len()
```


```python
dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>index</th>
      <th>len</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>the</td>
      <td>23135851162</td>
      <td>-1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>of</td>
      <td>13151942776</td>
      <td>-1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>and</td>
      <td>12997637966</td>
      <td>-1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>to</td>
      <td>12136980858</td>
      <td>-1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>a</td>
      <td>9081174698</td>
      <td>-1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>333328</td>
      <td>gooek</td>
      <td>12711</td>
      <td>-1.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>333329</td>
      <td>gooddg</td>
      <td>12711</td>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>333330</td>
      <td>gooblle</td>
      <td>12711</td>
      <td>-1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>333331</td>
      <td>gollgo</td>
      <td>12711</td>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td>333332</td>
      <td>golgw</td>
      <td>12711</td>
      <td>-1.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
<p>333333 rows × 4 columns</p>
</div>




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
