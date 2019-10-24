#!/usr/bin/env python
# coding: utf-8

# ### Text Representation 
# 
# The classifiers and learning algorithms can not directly process the text documents in their original form,as most of them expect numerical feature vectors with a fixed size rather than raw text docs with variable length. Therefore , during the preprocessing step, the texts are converted to a more manageable representation.
# 
# One common approach for extracting features from text is to use the bag of words model: a model where for each document, a resume in our case, the presence (and often the frequency) of words is taken into consideration, but the order in which they occur is ignored. 
# 
# TermFrequency and InverseDocumentFrequency is used for each document.

# In[3]:


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score

import nltk
df = pd.read_csv('clean_data1.csv')
df = df.drop(['Resume'],axis=1)
df.rename(columns={'newer_res':'Resume'},inplace=True)
resume_punc = df["Resume"].copy(deep  = True)
df.head()
#resume_punc


# In[4]:


import string
def rem_punc(s):
    punc = string.punctuation
    return [i for i in s if i not in punc]


# In[5]:


#Remove punctaution for further processing
for ind,i in enumerate(df.itertuples()):
    token = nltk.word_tokenize(i[4])
    #print(token)
    df["Resume"][ind] = " ".join(rem_punc(token))


# In[6]:


import string
from wordcloud import STOPWORDS
def rem_punc(s):
    punc = string.punctuation
    return [i for i in s if i not in punc]

def rem_sw(s):
    sw = set(STOPWORDS)
    #print(sw)
    return [i for i in s if i not in sw]

def preprocess(eval_res):
    try:
        eval_res = eval(eval_res).decode()
    except:
        pass
    eval_res = eval_res.encode("ASCII","ignore").decode()
    length = len(eval_res)
    #eval_res = " ".join(eval_res.split("\n"))
    token = rem_sw(nltk.word_tokenize(eval_res))#Removing punctaution later since we need punctaution for sentence tokenization
    #print(eval_res[:250])
    print(token)
    eval_res = eval_res.lower()
    print(eval_res[:250])
    return eval_res


# In[ ]:





# In[ ]:





# ### Cleaning data and adding in ID for category

# In[7]:


from io import StringIO
col = ['Category', 'Resume']
df = df[col]
df = df[pd.notnull(df['Resume'])]
df.columns = ['Category', 'Resume']
df['category_id'] = df['Category'].factorize()[0]
category_id_df = df[['Category', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Category']].values)

df.head()


# ### Vectorizing docs

# In[8]:


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1,2), stop_words='english')
features = tfidf.fit_transform(df.Resume).toarray()
labels = df.category_id
features.shape


# #### Using chi2 to see correlated items:

# In[9]:


from sklearn.feature_selection import chi2
import numpy as np
N = 2
for Category, category_id in sorted(category_to_id.items()):
    features_chi2 = chi2(features, labels == category_id)
    indices = np.argsort(features_chi2[0])
    feature_names = np.array(tfidf.get_feature_names())[indices]
    #print(feature_names)
    unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
    bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
    #trigrams = [v for v in feature_names if len(v.split(' ')) == 3] 
    print("# '{}':".format(Category))
    print("  . Most correlated unigrams:\n\t. {}".format('\n\t. '.join(unigrams[-N:])))
    print("  . Most correlated bigrams:\n\t. {}".format('\n\t. '.join(bigrams[-N:])))
    print("\n\n")
    #print("  . Most correlated trigrams:\n. {}".format('\n. '.join(trigrams[-N:])))


# **Understanding Why :** 
# 
# Suppose there are N instances, and two classes(say A and B).Given a feature X, we can use Chi Square Test to evaluate its importance to distinguish between the classes. 
# By calculating the Chi square scores for all the features, we can rank the features by the chi square scores, then choose the top ranked features for model training. 
# **Chi Square Test is used in statistics to test the independence of two events.
# In feature selection part of this project , the two events are :** 
# 
# **1.Occurence of a feature**
# 
# **2.Occurence of a Class/Doc category** 
# 
# **Note:** 
# the higher value of the chi^2 score, the more likelihood the feature is correlated with the class, thus it should be selected for model training.
# 

# ### Multi-Class Classifier: Features and Design
# 
# To train supervised classifiers, we first transformed the “Resumes” into a vector of numbers. We explored vector representations such as TF-IDF weighted vectors and also made sure there is some kind of correlation using the Chi^2 test to confirm that predictions are possible with these features that can be extracted from the documents. 
# 
# After having this vector representations of the text we can train supervised classifiers to train unseen “Resumes” and predict the “Job Category” on which they fall. After all the above data transformation, now that we have all the features and labels, it is time to train the classifiers. There are a number of algorithms we can use for this type of problem. 
# 
# 
# Naive Bayes Classifier: the one most suitable for word counts is the multinomial variant:

# In[26]:


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

x_train, x_test, y_train, y_test = train_test_split(df['Resume'], df['Category'], random_state = 0)

#print(x_train)

count_vect = CountVectorizer() # bag-of-ngrams model , based on frequency count
x_train_counts = count_vect.fit_transform(x_train)

tfidf_transformer = TfidfTransformer() #passing the word:word count
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

classifier = LinearSVC().fit(x_train_tfidf, y_train)


# ### Testing it on an unseen pdf resume

# In[13]:


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convertPDFtoText(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    string = retstr.getvalue()
    retstr.close()
    return string


# In[14]:


test_resume = convertPDFtoText("sample_input.pdf")
print(test_resume)


# In[15]:


from nltk.probability import FreqDist
from string import punctuation
import math
def summarize(doc,words):
    score={}
    fd = FreqDist(words)
    for i,t in enumerate(doc):
        score[i] = 0
        for j in nltk.word_tokenize(t):
            if j in fd:
                score[i]+=fd[j]
    
    r = sorted(list(score.items()),key=lambda x:x[1],reverse=True)[:math.floor(0.60*len(doc))]
    r.sort(key=lambda x:x[0])
    l = [doc[i[0]] for i in r]
    return "\n\n".join(l)


# **We pass the resume extracted from the pdf using OCR through preprocess function to bring it down to the same state as the trained data, and use this for classification and summarization**

# ## Summary of Test Resume

# In[29]:


resume = preprocess(test_resume)#remove stop words etc
sent = nltk.sent_tokenize(test_resume)
puncu = punctuation
word_token = nltk.word_tokenize(test_resume)#tokenize preprocessed text for scoring

print(summarize(sent,test_resume))


# ## Predicted Label for Test Resume

# In[30]:


print(classifier.predict(count_vect.transform([test_resume])))


# ### Comparisons between models

# In[24]:


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score


models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]


CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])


# In[26]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df, 
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.show()


# In[27]:


cv_df.groupby('model_name').accuracy.mean()


# As we can observe an SVM and the Logistic regression models seem to be doing better with accuracy of around 60-70%.
# 
# 
# 
# ### Linear SVC:
# 

# In[28]:


model = LinearSVC()
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.30, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
#y_pred2 = model.predict([test_resume])
from sklearn.metrics import confusion_matrix


conf_mat = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(conf_mat, annot=True, fmt='d',
            xticklabels=category_id_df.Category.values, yticklabels=category_id_df.Category.values)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()


# **As we can clearly see from the visualization that a vast majority of the predicted values lie on the diagonal representing True Positive values**

# In[ ]:


### RELEVANCE RANKING #########

# work exp
# Education
# projects
import re

anish =  convertPDFtoText("anish.pdf")
rel = 0
resume = preprocess(anish)#remove stop words etc
sent = nltk.sent_tokenize(anish)
puncu = punctuation
word_token = nltk.word_tokenize(anish)

x = 'internship experience'
y = 'education'
z = 'projects'
w = 'publications'
indx = re.search(x,resume)
if(y in resume):

if(w in resume):
    print(resume.index(w))
if(z in resume):
    print(resume.index(z))
    

str1 = resume[indy:indx.end()+1]
if('bachelor' in resume or 'b.tech' in resume):
    rel+=10
ind = re.search(' gpa|cgpa', resume)
gpa = resume[ind.end()+2:ind.end()+6]
gpa = float(gpa)
if(gpa>9):
    rel+=20
elif(gpa>8 and gpa<9):
    rel+=10
else:
    rel+=5
    #gpa = map(int,gpa)

if('master' in resume):
    rel+=50
    
regex = '.*\(.*\) *$'
companies = re.match(regex, resume)