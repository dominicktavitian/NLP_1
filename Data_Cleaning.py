
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cross_validation import train_test_split
import os
import re


# In[ ]:

#data read in data


# ## Import Raw Data

# In[3]:

#fake_news = pd.read_csv("fake.csv", delimiter = ',', skipinitialspace=True, encoding='ISO-8859-1')


# In[4]:

#npr = pd.read_csv("fakenews/npr_politics_data_set.csv", delimiter = ',', skipinitialspace=True, encoding='ISO-8859-1')


# In[5]:

#bbc = pd.read_csv("fakenews/BBC_Politics.csv", delimiter = ',', skipinitialspace=True, encoding = 'ISO-8859-1')


# In[6]:

#econ = pd.read_csv("fakenews/econ_politics.csv", delimiter = ',', skipinitialspace=True, encoding='ISO-8859-1')


# In[7]:

npr.head()


# In[8]:

econ.head()


# In[9]:

bbc.head()


# In[10]:

fake_news.head()


# ## Clean Data

# #### 1. Filter the fake_news dataset

# In[11]:

# Only English Language Articles


# In[12]:

fake_news = fake_news[fake_news['language'] == 'english']


# In[13]:

# Only relevant columns


# In[14]:

fake_news = fake_news[['author', 'published', 'title', 'text', 'site_url']]


# #### 2. Combine non fake datasets

# In[15]:

real_news = bbc


# In[16]:

real_news = real_news.append(npr)


# In[17]:

real_news = real_news.append(econ)


# #### 3. Add 'is_fake' column to both datasets

# In[18]:

fake_news['is_fake'] = 1


# In[19]:

real_news['is_fake'] = 0


# #### 3. Define a text cleaning utility function

# In[20]:

def clean(text):
    """
    Returns the cleaned version of the passed in text.
    
    Parameters
    ----------
        text: str
            String representation of text that should be cleaned.
    """
    cleaned_txt = ""
    if isinstance(text, str):
        ps = PorterStemmer()
        cleaned_txt = re.sub('[^a-zA-Z]', ' ', text).lower() # Remove non-ASCII characters
        cleaned_txt = [ps.stem(word) for word in cleaned_txt.split() # Remove the root of non-stop words
                       if word not in set(stopwords.words('english'))]
        cleaned_txt = [word for word in cleaned_txt if wordnet.synsets(word)] # Filter out outliers
        cleaned_txt = ' '.join(cleaned_txt) # Reassign cleaned_text to a string representation
    return(cleaned_txt)


# #### 3. Separate features from outcomes

# In[21]:

fake_features = fake_news.loc[:, fake_news.columns != 'is_fake'].values
fake_outcomes = fake_news.loc[:, fake_news.columns == 'is_fake'].values


# In[22]:

real_features = real_news.loc[:, real_news.columns != 'is_fake'].values
real_outcomes = real_news.loc[:, real_news.columns == 'is_fake'].values


# #### 4. Train/Test Split

# In[89]:

fake_x_train, fake_x_test, fake_y_train, fake_y_test =    train_test_split(fake_features, fake_outcomes, test_size = 0.90)


# In[24]:

real_x_train, real_x_test, real_y_train, real_y_test =    train_test_split(real_features, real_outcomes, test_size = 0.25)


# In[66]:

x_train = np.append(fake_x_train, real_x_train, axis = 0)
x_test = np.append(fake_x_test, real_x_test, axis = 0)
y_train = np.append(fake_y_train, real_y_train, axis = 0)
y_test = np.append(fake_y_test, real_y_test, axis = 0)


# #### 5. Clean the training/test data's text fields

# In[36]:

cleaner = np.vectorize(clean)


# In[38]:

x_train[:, 3] = cleaner(x_train[:, 3])
x_test[:, 3] = cleaner(x_test[:, 3])


# In[90]:

# Run this!!
x_train = pd.read_csv('./Analysis/clean_data/x_train_clean.csv')
x_test = pd.read_csv('./Analysis/clean_data/x_test_clean.csv')


# In[92]:

x_train


# #### 6. Create Bag-of-X Model for train/test 

# In[ ]:

# Last minute additions!


# In[32]:

x,y = pd.read_csv("./Analysis/clean_data/x.csv", index_col=False), pd.read_csv("./Analysis/clean_data/y.csv")


# In[34]:

y = y[['is_fake']]


# In[36]:

x = x[['text']]


# In[59]:

combined = pd.concat([x.reset_index(drop=True), y], axis=1).dropna()


# In[61]:

combined_fake, combined_real = combined[combined.is_fake == 1], combined[combined.is_fake == 0]


# In[63]:

unigram = CountVectorizer(max_features = 1000)
bigram = CountVectorizer(ngram_range=(2,2), max_features = 1000)


# In[64]:

fake_text,real_text = combined_fake.text.values, combined_real.text.values


# In[ ]:

# Fake


# In[65]:

unigram.fit(fake_text)
bigram.fit(fake_text)


# In[73]:

unigrams_fake, bigrams_fake =    unigram.get_feature_names(), bigram.get_feature_names()


# In[72]:

bow_fake = unigram.transform(fake_text)
bobg_fake = bigram.transform(fake_text)


# In[ ]:

# Real


# In[74]:

unigram.fit(real_text)
bigram.fit(real_text)


# In[75]:

unigrams_real, bigrams_real =    unigram.get_feature_names(), bigram.get_feature_names()


# In[76]:

bow_real = unigram.transform(real_text)
bobg_real = bigram.transform(real_text)


# In[ ]:

# Write to csv


# In[82]:

write_csv(bow_fake, unigrams_fake, './Analysis/clean_data/bow_fake.csv')
write_csv(bobg_fake, bigrams_fake, './Analysis/clean_data/bobg_fake.csv')
write_csv(bow_real, unigrams_real, './Analysis/clean_data/bow_real.csv')
write_csv(bobg_real, bigrams_real, './Analysis/clean_data/bobg_real.csv')


# In[ ]:




# In[ ]:




# In[ ]:

#------END-----#


# In[42]:

# Train


# In[43]:

bow_train = unigram.transform(x_train[:,3])
bobg_train = bigram.transform(x_train[:, 3])


# In[44]:

# Test


# In[45]:

bow_test = unigram.transform(x_test[:, 3])
bobg_test = bigram.transform(x_test[:, 3])


# In[62]:

print_list = [("Bag of Words (Train)", bow_train),
             ("Bag of Bigrams (Train)", bobg_train)]


# In[63]:

for (n,r) in print_list:
    print("%s: %s" % (n, r.shape))


# #### 7. Create TF-IDF Model for train/test 

# In[75]:

def get_tfidf(bag):
    """
    Returns a TF-IDF representation of the 
    wordcount "bag"
    
    Parameters
    ----------
        bag: numpy ndarray
    """
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(bag)
    return tfidf


# In[76]:

# Train


# In[77]:

tfidf_train = get_tfidf(bow_train)
tfidf_bobg_train = get_tfidf(bobg_train)


# In[78]:

# Test


# In[79]:

tfidf_test = get_tfidf(bow_test)
tfidf_bobg_test = get_tfidf(bobg_test)


# ## Export Data

# #### 1. Define utility function to create dataframes out of vectorized representations

# In[81]:

def write_csv(matrix, tokens, filepath):
    """
    Writes a csv file to filepath with observations matrix
    and columns tokens. 
    
    Parameters
    ----------
        matrix: numpy ndarray
            Vectorized representation of the text of the observations
        tokens: numpy ndarray
            array mapping from feature integer indices to feature name for matrix
        filepath: str
            path to output csv
    """
    data = pd.DataFrame(data=matrix.toarray(), columns=tokens)
    data.to_csv(filepath)


# #### 2. Get dataframe for each vectorized representation

# In[81]:

# Train


# In[82]:

write_csv(bow_train, unigrams, './Analysis/clean_data/bow_train.csv')
write_csv(bobg_train, bigrams, './Analysis/clean_data/bobg_train.csv')
write_csv(tfidf_train, unigrams, './Analysis/clean_data/tfidf_train.csv')
write_csv(tfidf_bobg_train, bigrams, './Analysis/clean_data/tfidf_bobg_train.csv')


# In[83]:

# Test
write_csv(bow_test, unigrams, './Analysis/clean_data/bow_test.csv')
write_csv(bobg_test, bigrams, './Analysis/clean_data/bobg_test.csv')
write_csv(tfidf_test, unigrams, './Analysis/clean_data/tfidf_test.csv')
write_csv(tfidf_bobg_test, bigrams, './Analysis/clean_data/tfidf_bobg_test.csv')

