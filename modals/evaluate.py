'''from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score,confusion_matrix
from nltk import word_tokenize'''
import pickle
import os

def read(file):
    r=open(file,'r',encoding="utf8")
    boum=r.read()
    d=boum.splitlines()
    v=[]
    x=[]
    y=[]
    for i in d:
        v.append(i.split('\t'))
    for j in v:
        org=word_tokenize(j[1])
        x.append(' '.join(org))
        doc=''
        if str(j[0])=='1':
            doc='positive'
        else:
            doc='negative'
        y.append(doc)
    print('x:'+j[1])
    print('y:'+j[0])     
    print('COUNT  :'+str(len(x)))
    r.close()
    learn(x,y)
'''
def learn(): # To Apply on new Documents
    file=pd.read_table('../data/train.tsv')
    file.loc[file['Sentiment'] == 0, 'Sentiment'] = 'negative'
    file.loc[file['Sentiment'] == 1, 'Sentiment'] = 'somewhat negative'
    file.loc[file['Sentiment'] == 2, 'Sentiment'] = 'neutral'
    file.loc[file['Sentiment'] == 3, 'Sentiment'] = 'somewhat positive'
    file.loc[file['Sentiment'] == 4, 'Sentiment'] = 'positive'

    entr=pd.DataFrame(file,columns=['Phrase']).values.tolist()
    sort=pd.DataFrame(file,columns=['Sentiment']).values.tolist()
    my_stopword_list = ['and','to','the','of']
    entryx=[]
    entryy=[]
    for x in entr:
        entryx.append(str(x[0]))
    for x in sort:
        entryy.append(str(x[0]))

    print("X : "+str(entryx[0]))
    print("Y : "+str(entryy[0]))
    vectorizer = TfidfVectorizer(stop_words=my_stopword_list)
    X = vectorizer.fit_transform(entryx)
    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB()
    X_train, X_test, y_train, y_test = train_test_split(X, entryy, test_size=0.33,shuffle=True )

#    print('Y_train :'+str(y_train))
    clf.fit(X_train, y_train)
    y_pred=clf.predict(X_test)
    pickle.dump(vectorizer, open('tfidf', 'wb'))
    pickle.dump(clf, open('modal', 'wb'))
    print('Accuracy : \n')
    print(accuracy_score(y_test, y_pred))
    print('\nConfusion Matrix :\n')
    print(confusion_matrix(y_test, y_pred)) 
    '''

def evaluate(ent):
    vect=pickle.load(open(os.path.join('modals','tfidf'),'rb'))
    clf=pickle.load(open(os.path.join('modals','modal'),'rb'))
    x=vect.transform([ent])
    lor=clf.predict(x)  
    return str(lor[0])
