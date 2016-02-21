import json
import csv
import os
from pprint import pprint
#import pandas as pd
#import numpy as np

for file in os.listdir("hasil_json_imagga"):
    if file.endswith(".txt"):
 	with open('hasil_json_imagga/'+str(file)) as data_file:    
		data = data_file.read()
		data = data.replace("'", "")
		data = data.replace(", {\"results\": [", "pemisah {\"results\": [")
		data = data.split('pemisah ')
	count = 0

	for data_file in data:
		j = str(data_file)
		j = j.replace("[{\"results\":", "{\"results\":")
		j = j.replace("}]}]}]", "}]}]}")
		#print j

		
		d = json.loads(j)
		jumlah_image = int(len(d['results']))
		#print jumlah_image
		

		for i in range(0,jumlah_image): #jumlah dari image
			datacsv = open('rekap'+str(file)+'.csv', 'a')
			csvwriter = csv.writer(datacsv)
			emp_data = d['results'][i]["categories"]
			for tagging in emp_data:
				if count ==0:
					header = tagging.keys()
					#csvwriter.writerow(header)
					count += 1
				csvwriter.writerow(tagging.values())
			#count = 0 
		datacsv.close()

	sums = {}
	with open('rekap'+str(file)+'.csv') as rekaphasil:
			#rekaphasil.next()
		reader = csv.reader(rekaphasil)
		for row in reader:
			if row[1] not in sums: 
				sums[row[1]] = float(row[0])
			else: 
				sums[row[1]] += float(row[0])
		#print str(file)
		print sums
	for i in sums:
		try: 
			att4 = sums["food drinks"]
		except KeyError:
			att4 = 0 

	for i in sums:
		try:
			att5 = sums["pets animals"]
		except KeyError:
			att5 = 0 

	for i in sums:
		try:
			att6 = sums["nature landscape"]+sums["beaches seaside"]+ sums["sunrises sunsets"]+sums["streetview architecture"]
		except KeyError: 
			att6 = 0



	# if max(att4, att5, att6) == att4:
	# 	att4 = 1
	# 	att5 = 0
	# 	att6 = 0
	# if max(att4, att5, att6) == att5:
	# 	att4 = 0
	# 	att5 = 1
	# 	att6 = 0
	# if max(att4, att5, att6) == att6:
	# 	att4 = 0
	# 	att5 = 0
	# 	att6 = 1

	#normalis = 1 #ada 30 image yang dipakai 

	if 'food_' in str(file):
		output = 1
	elif 'pet_' in str(file):
		output = 2
	elif 'traveling_' in str(file):
		output = 3

	# if att4==att5 and att5==att6:
	normalis = 30
	# else:
	# 	normalis = (max(att4,att5,att6))


	dataImage = str(file).replace('.txt','').replace('hasil_','')+","+str(att4/normalis)+","+str(att5/normalis)+","+str(att6/normalis)+","+str(output)+'\n'
	#dataImage = str(file).replace('.txt','').replace('hasil_','')+","+str(att4)+","+str(att5)+","+str(att6)+","+str(output)+'\n'

	with open("data_image_new_10.csv","a") as text_file:
		text_file.write(dataImage)

	os.remove('rekap'+str(file)+'.csv')
		

		