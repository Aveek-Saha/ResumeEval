import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug import secure_filename
from flask_cors import CORS

import json
import dateutil.parser
import requests

import pandas as pd
from sklearn.svm import LinearSVC
import nltk
import string
from wordcloud import STOPWORDS
from nltk.probability import FreqDist
from string import punctuation
import math
import pickle
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

UPLOAD_FOLDER = os.getcwd() + '/uploaded/'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

fp = open("load_df.bin", "rb")
df = pickle.load(fp)
fp.close()

suggested_skills = dict()

suggested_skills['hr'] = ["Employee Relations","Onboarding","Human Resources Information Software","Performance management","Teamwork and collaboration","Scheduling"]
suggested_skills['designing'] = ["iWork Keynote","Ad Design","Photography","Illustration","Creating Models for Three-dimensional Forms"]
suggested_skills['management'] = ["People Management","Office Management","Conflict Resolution","Negotiating","Delegation"]
suggested_skills['information technology'] = ["Tensorflow","Pytorch","React.js","Vue.js","MongoDB","Spark","Hadoop"]
suggested_skills['education'] = ["Body Language","Disciplining","Relationship Building","Listening","Verbal Communication","Networking"]
suggested_skills['advocate'] = [" Good communication skills","Judgement","Analytical skills","Research skills","People skills"]
suggested_skills['business development'] = ["Communication & Interpersonal Skills","Collaboration Skills","Negotiation & Persuasion skills","Project Management Skills","Research & Strategy","Business Intelligence"]
suggested_skills['health and fitness'] = ["Personal motivation ","Patience","Nutrition","Awareness of safety"]
suggested_skills['agricultural'] = ["Organizational Skills","Management Skills","Organic Integrity","Business Savvy","Analytical and Critical Thinking Skills"]
suggested_skills['bpo'] = [" Knowledge Retention","Organization"," Flexibility","Friendly","Communication Skills"]
suggested_skills['sales'] = ["Product Knowledge","Strategic Prospecting Skills", "Active Listening","Time Management","Objection Handling","Closing Techniques"]
suggested_skills['consultancy'] = ["Leadership","Commercial Awareness","Team Work","Entrepreneurial Skills"]
suggested_skills['digital media']  =["Client Relations","Collaboration","Interviewing Staff","Proofreading","Storytelling"]
suggested_skills['automobile'] = ["Know Latest Trends","programming skills","Practical Knowledge","Communication Skills"]
suggested_skills['food and beverages'] = ["Communication skills","Teamwork","personal hygiene"]
suggested_skills['finance'] = ["Interpersonal skills","Communication skills"," Financial reporting","Analytical ability"]
suggested_skills['apparel'] = ["Artistic Skills","Visualization Skills","Business Sense"]
suggested_skills['engineering'] = ["Statistics","Advanced Physics","Nanotechnology","Structural Analysis"]
suggested_skills['accountant'] = ["Strategic decision-making"," Information technology expertise","Customer service skills","Industry knowledge"]
suggested_skills['building and construction'] =  ["Critical Thinking","Leadership Skills","Time Management","Analytical Thinking"]
suggested_skills['architects'] = ["Design skills","Math and science skills","Drawing Skills"]
suggested_skills['public relations'] =["Communication","Multimedia","Social Media skills"]
suggested_skills['banking'] = ["Numeracy skills","Time Management","Analytical Thinking","Customer service skills"]
suggested_skills['arts'] = ["design skills","Time management skills","interpersonal skills"]
suggested_skills['aviation'] = ["Travel-Friendly","Critical Thinking","Communication Skills"]


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


def rem_punc(s):
    punc = string.punctuation
    return [i for i in s if i not in punc]

def rem_sw(s):
    sw = set(STOPWORDS)
    return [i for i in s if i not in sw]

def preprocess(eval_res):
    try:
        eval_res = eval(eval_res).decode()
    except:
        pass
    eval_res = eval_res.encode("ASCII","ignore").decode()
    eval_res = eval_res.lower()
    return eval_res

col = ['Category', 'Resume']
df = df[col]
df = df[pd.notnull(df['Resume'])]
df.columns = ['Category', 'Resume']
df['category_id'] = df['Category'].factorize()[0]
category_id_df = df[['Category', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Category']].values)

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1,2), stop_words='english')
features = tfidf.fit_transform(df.Resume).toarray()
labels = df.category_id



x_train, x_test, y_train, y_test = train_test_split(df['Resume'], df['Category'], random_state = 0)

#print(x_train)

count_vect = CountVectorizer() # bag-of-ngrams model , based on frequency count
x_train_counts = count_vect.fit_transform(x_train)

tfidf_transformer = TfidfTransformer() #passing the word:word count
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

classifier = LinearSVC().fit(x_train_tfidf, y_train)


def do_ml(filename):
	test_resume = convertPDFtoText(filename)
	#print(test_resume)


	resume = preprocess(test_resume)#remove stop words etc
	sent = nltk.sent_tokenize(test_resume)
	puncu = punctuation
	word_token = nltk.word_tokenize(test_resume)#tokenize preprocessed text for scoring
	summary = summarize(sent,test_resume)
	predclass = classifier.predict(count_vect.transform([test_resume]))
	predclass  =predclass[0]
	
	return [summary, predclass]
	
def score(data):
	score = 0
	for i in data['education']:
		if i['studyType'][0].lower()=='b':
		    x = float(i['gpa'])-6
		    gpa_score = 0
		    if(x>0):
		        score+=20*x
		

	score+= 7*len(data['awards'])
	score+= 3*len(data['skills'])
	score+= 10* len(data['projects'])
	for i in data['projects']:
		if i['published']=='1':
		    score+=40
	for i in data['education']:
		if i['studyType'][0].lower()=='b':
		    score+=100
		if i['studyType'][0].lower()=='m':
		    score+=100
		if i['studyType'][0].lower()=='p':
		    score+=300
	work_days = 0
	for i in data['work']:
		if(i['startDate']=='null'):
		    break
		end  = dateutil.parser.parse(i['endDate'])
		start  = dateutil.parser.parse(i['startDate'])
		exp  = end - start
		work_days +=abs(exp.days)
		company_name = i['company']
		r = requests.get("http://www.google.com/search?query=" + company_name)
		rating = 0
		s = str(r.text)
		pos = s.find('aria-label="Rated')
		if(pos != -1):
		    try:
		        rating = float(s[pos+17:pos+20])
		    except:
		        rating = 0
		
		if(rating>=4):
		    score+=50
		    
	work_months  = work_days//30    
	score += 15*work_months
	ex='Excellent Resume!'
	good = 'Good Resume!'
	bad = 'Resume Can Be Improved!'
	if(score>=500):
		result = ex
	if(score>300 and score<500):
		result = good
	if(score<=300):
		result = bad
		
	return result



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        print("File recieved")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            
        res = do_ml(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        suggestions = ""
        if(res[1].lower() in suggested_skills):
        	suggestions = ", ".join(suggested_skills[res[1].lower()])
        
        return jsonify({'summary': res[0], 'category': res[1], 'suggest': suggestions})
    return """
    <!doctype html>
    <title>Uploaded Files</title>
    <h1>Uploaded Files</h1>
    
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))


@app.route("/rate", methods=['POST'])
def rate():
    rating = "No rating"
    summary = "This is a resume summary"
    category = "IT"
    if request.method == 'POST':
    	data = request.get_json()
    	print(request)
    	rating = score(data)
    return jsonify({'rating': rating})

if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
