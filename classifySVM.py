# usage: python classifyKNN.py <citra/teks/gabung> <dataset.csv>
# sample: python classifySVM citra data_instagram_new_10.csv 

import pandas as pd 
import numpy as np
from sklearn import cross_validation
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split, KFold
from sklearn.metrics import confusion_matrix
from sklearn import metrics,svm
import sys

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    #plt.colorbar()
    for i, cas in enumerate(cm):
        for j, c in enumerate(cas):
            if c>0:
                plt.text(j-.2, i+.2, c, fontsize=14)
            else:
                plt.text(j-.2, i+.2, '0',fontsize=14)
    tick_marks = np.arange(len(yFrame.target_names))    
    plt.xticks(tick_marks, yFrame.target_names, rotation=45)
    plt.yticks(tick_marks, yFrame.target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

df = pd.read_csv(sys.argv[2])

if sys.argv[1] == 'teks':
    XFrame = df.ix[:,0:3]
elif sys.argv[1] == 'citra':# untuk yang atribut 1 s.d. 3 
    XFrame = df.ix[:,3:6] # untuk yang atribut 4 s.d. 6 
elif sys.argv[1] == 'gabung':
    XFrame = df.ix[:,0:6] # untuk semua atribut 
else:
    print "isi argumen ini dengan 'teks' atau 'citra' atau 'gabung'"

yFrame = df.ix[:,6:7]
X = pd.DataFrame.as_matrix(XFrame)
Y = pd.DataFrame.as_matrix(yFrame)

X,xtest,Y,ytest = cross_validation.train_test_split(X,Y,test_size=0,random_state = 1992)
cv = cross_validation.KFold(len(XFrame), n_folds=10)

with open('data.txt', "a") as text_file:
    text_file.write(format(X))
    text_file.write(format(Y))
'''
#kernelnya = ['rbf','linear','poly','sigmoid']
#print "jenis kernel, akurasi, presisi, recall, fskor"
kernelnya = ['linear']

for kern in kernelnya:
    clf = SVC(decision_function_shape='ovo', random_state=0, kernel = kern, cache_size = 200, max_iter = -1)

    outpred = []
    akurasi=[] #akurasi 
    outpred = [] #hasil prediksi
    validasi = 1
    fskor = np.zeros(3)
    presisi = np.zeros(3)
    recall = np.zeros(3)

    for trained, tested in cv:
        clf.fit(X[trained], np.ravel(Y[trained]))
        y_pred = clf.predict(X[tested])
        outpred.extend(y_pred)
        akurasi.append(metrics.accuracy_score(Y[tested],y_pred))
        #print("Fold ke-"+str(validasi)+" Akurasi = "+str(results[validasi-1]))
        #validasi = validasi + 1
    #print np.mean(fskor)
    #print("Akurasi rata-rata = "+str(np.mean(results)))
    #print("Std Deviasi = "+str(np.std(results)))
    # print str(np.mean(results))
    # print str(np.std(results))
    # #yFrame.target_names = ['kuliner' ,'memelihara hewan' ,'melancong']
    akurasi = np.mean(akurasi)
    # # Compute confusion matrix
    cm = confusion_matrix(Y,outpred)
    presisi = metrics.precision_score(Y,outpred,average=None)
    recall = metrics.recall_score(Y,outpred,average=None)
    fskor = metrics.f1_score(Y,outpred,average=None)
    np.set_printoptions(precision=3)
    #print kern,',',akurasi,',',presisi,',',recall,',',fskor
 #  
    # # Compute confusion matrix
    # cm = confusion_matrix(y, outpred)
    # np.set_printoptions(precision=2)
    # print('Confusion matrix, without normalization',str(kern))
    print(cm)
    # # plt.figure()
    # # plot_confusion_matrix(cm)

    # # # Normalize the confusion matrix by row (i.e by the number of samples
    # # # in each class)
    # cm_normalized = cm.astype('float')*100 / cm.sum(axis=1)[:, np.newaxis]
    # cm_normalized = np.matrix.round(cm_normalized,decimals = 2)
    # print('Normalized confusion matrix')
    # print(cm_normalized)
    # plt.figure()
    # plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix')
    # plt.show()
    '''

