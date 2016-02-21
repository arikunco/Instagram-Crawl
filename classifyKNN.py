# usage: python classifyKNN.py <citra/teks/gabung> <dataset.csv>
# sample: python classifyKNN citra data_instagram_new_10.csv 

import pandas as pd 
import numpy as np
from sklearn import cross_validation
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
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
    tick_marks = np.arange(len(YFrame.target_names))    
    plt.xticks(tick_marks, YFrame.target_names, rotation=45)
    plt.yticks(tick_marks, YFrame.target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Baca dataset 
df = pd.read_csv(sys.argv[2])

if sys.argv[1] == 'teks':
    XFrame = df.ix[:,0:3]
elif sys.argv[1] == 'citra':# untuk yang atribut 1 s.d. 3 
    XFrame = df.ix[:,3:6] # untuk yang atribut 4 s.d. 6 
elif sys.argv[1] =='gabung':
    XFrame = df.ix[:,0:6] # untuk semua atribut 
#print XFrame
YFrame = df.ix[:,6:7]

# Konversi ke matriks (numpy array)
X = pd.DataFrame.as_matrix(XFrame)
Y = pd.DataFrame.as_matrix(YFrame)

# Mengacak data, sedemikian sehingga data tidak urut label 1, 2, dan 3
X,xtest,Y,ytest = cross_validation.train_test_split(X,Y,test_size=0,random_state = 1992)
#jmlneighbor = [5,7,9,11,13,15,17]
k = 10 #jumlah fold
print "jml neighbor, akurasi, presisi, recall, fskor"
jmlneighbor = [9]
for j in jmlneighbor:
    # Validasi KFold, dengan K = 10, banyaknya data = len(XFrame)
    cv = cross_validation.KFold(len(XFrame), n_folds=k)
    neigh = KNeighborsClassifier(n_neighbors=j, metric='euclidean')

    akurasi=[] #akurasi 
    outpred = [] #hasil prediksi
    validasi = 1
    fskor = np.zeros(3)
    presisi = np.zeros(3)
    recall = np.zeros(3)

    # Mulai training dan testing selama K kali
    for trained, tested in cv:
    	# Training
        #print Y[trained]
    	neigh.fit(X[trained], np.ravel(Y[trained]))
    	#print '==========='
        #print np.ravel(Y[trained])
        # Testing
    	y_pred = neigh.predict(X[tested])
    	#print y_pred
        # Append hasil testing
    	outpred.extend(y_pred)
    	# Append hasil akurasi 
    	akurasi.append(metrics.accuracy_score(Y[tested],y_pred))
        #fskor.append(metrics.f1_score(Y[tested],y_pred,average='weighted'))
        #presisi.append(metrics.precision_score(Y[tested], y_pred, average=None))
    	#presisi = presisi + metrics.precision_score(Y[tested], y_pred, average=None)
        #recall = recall + metrics.recall_score(Y[tested], y_pred, average=None)
        #fskor = fskor + metrics.f1_score(Y[tested],y_pred,average=None)
        # Print report tiap fold 
    	#print("Fold ke-"+str(validasi)+" Akurasi = "+str(akurasi[validasi-1]))
    	#validasi = validasi + 1

    #print j,',',np.mean(akurasi),',',np.mean(presisi/k),',',np.mean(recall/k),',',np.mean(fskor/k)

    #print(akurasi)
    # print("Akurasi rata-rata = "+str(np.mean(akurasi)))
    # print("Std Deviasi = "+str(np.std(akurasi)))

    # # #beri label pada graphic
    # YFrame.target_names = ['kuliner' ,'memelihara hewan' ,'melancong']
    akurasi = np.mean(akurasi)
    # # Compute confusion matrix
    cm = confusion_matrix(Y,outpred)
    presisi = metrics.precision_score(Y,outpred,average=None)
    recall = metrics.recall_score(Y,outpred,average=None)
    fskor = metrics.f1_score(Y,outpred,average=None)
    np.set_printoptions(precision=2)
    #print 'Confusion matrix, without normalization with k = ',str(j)
    print(cm)
    #print j,',',akurasi,',',presisi,',',recall,',',fskor
 #   plt.figure()
    # plot_confusion_matrix(cm)

    # # Normalize the confusion matrix by row (i.e by the number of samples
    # # in each class)
    # cm_normalized = cm.astype('float')*100 / cm.sum(axis=1)[:, np.newaxis]
    # cm_normalized = np.matrix.round(cm_normalized,decimals = 2)
    # print('Normalized confusion matrix')
    # print(cm_normalized)
    # plt.figure()
    # plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix in percent')

    # plt.show()
