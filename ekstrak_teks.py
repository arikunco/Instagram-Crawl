from __future__ import division, unicode_literals
#import HTMLParser
import math
from textblob import TextBlob as tb
from nltk.corpus import stopwords
import re
import itertools
import os,time
from subword import subword_1,subword_2,subword_3,chars_to_remove,indostop


# DATA CLEANING
#html_parser = HTMLParser.HTMLParser()

# STOPWORDS (INDONESIAN AND ENGLISH)
ws = stopwords.words('english')
ws.extend(indostop)
#print ws

def clean_doc(dokumen):
    with open(dokumen, 'r') as myfile:
        document = myfile.read()
        # ESCAPING HTML CHARACTERS
        #document = html_parser.unescape(document)
        # REMOVE UTF8 CHARACTERS (SYMBOL INSTEAD OF ASCII)
        document = document.decode("utf8").encode('ascii','ignore')
        # REMOVE PUNCTUATIONS AND HIS/HER OWN INSTAGRAM USERNAME
        for i in chars_to_remove:
            document = document.replace(i,'')
        # DECODING DATA ( transforming information from complex symbols 
        # to simple and easier to understand characters)
            
        # # APOSTHROPES LOOK UP
        APPOSTOPHES = {"'s" : " is", "'re" : " are"} ## Need a huge dictionary
        words = document.split()
        document = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]
        # REMOVE STOPWORDS
        document = [word for word in document if word not in ws]
        document = " ".join(document)
        # STANDARDIZING WORDS  e.g. i looooveee yoooou = i love you   
        document = ''.join(''.join(s)[:2] for _, s in itertools.groupby(document))
        #REMOVE URL 
        document = re.sub(r"http\S+", "", document)
        # SPLIT ATTACHED WORDS e.g. DisplayIsAwesome = Display Is Awesome 
        document = str(" ".join(re.findall('[A-Z][^A-Z]*', document)))
        # convert to lower case
        document = str(document).lower()
        
        
    return document

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

bloblist = []
namaPengguna = []

for file in os.listdir("ABC_all_new"):
    if file.endswith(".txt"):
        namaPengguna.append(str(file)) 
        print(namaPengguna)
        cleaned = tb(clean_doc('ABC_all_new/'+str(file)))
        bloblist.append(cleaned)

for j, blob in enumerate(bloblist):
    #scores = {word: tf(word, blob) for word in blob.words}
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(sorted_words[:20])
    att1 = 0
    att2 = 0
    att3 = 0

    for word, score in sorted_words[:20]:
        for i in subword_1:
            if i in word:
                att1 = att1 + score
            # else:
            #     att1 = att1
        for i in subword_2:
            if i in word:
                att2 = att2 + score
            # else:
            #     att2 = att2
        for i in subword_3:
            if i in word:
                att3 = att3 + score

    # if att1==att2 and att2==att3:
    #     att1 = 0
    #     att2 = 0
    #     att3 = 0
    # elif max(att1, att2, att3) == att1:
    #     att1 = 1
    #     att2 = 0
    #     att3 = 0
    # elif max(att1, att2, att3) == att2:
    #     att1 = 0
    #     att2 = 1
    #     att3 = 0
    # elif max(att1, att2, att3) == att3:
    #     att1 = 0
    #     att2 = 0
    #     att3 = 1
    # if att1==att2 and att2==att3:
    #     pengali= 1
    # else:
    #     pengali = 1/(max(att1,att2,att3))
    pengali = 100

    data_teks = str(namaPengguna[j].replace('.txt',''))+","+str(pengali*att1)+","+str(pengali*att2)+","+str(pengali*att3)+"\n"
    # write data 
    with open("data_text_new11.csv","a") as text_file:
        text_file.write(data_teks)
    
    