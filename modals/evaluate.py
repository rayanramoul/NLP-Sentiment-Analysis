'''from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score,confusion_matrix
from nltk import word_tokenize'''
import pickle

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

'''def learn(entryx,entryy): # To Apply on new Documents
    my_stopword_list = ['and','to','the','of']
    vectorizer = TfidfVectorizer(stop_words=my_stopword_list)
#    print('ENTRY X :'+str(entryx))
    X = vectorizer.fit_transform(entryx)
    clf = MultinomialNB()
    X_train, X_test, y_train, y_test = train_test_split(X, entryy, test_size=0.33,shuffle=True )

    print('to train with : \n0 :'+str(y_train.count(str(0)))+'\n1 :'+str(y_train.count(str(1))))
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
    vect=pickle.load(open('tfidf','rb'))
    clf=pickle.load(open('modal','rb'))
    x=vect.transform([ent])
    lor=clf.predict_proba(x)[0]
    if lor[0]>lor[1]:
        bx=g = float("{0:.4f}".format(lor[0]))
        return 'Negative at '+str(bx*100)+'%'
    else:
        bx=g = float("{0:.4f}".format(lor[1]))
        return 'Positive at '+str(bx*100)+'%'


print(str(evaluate('this is cool and awesome.')))
