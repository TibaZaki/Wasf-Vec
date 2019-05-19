#!/usr/bin/python3
# -*- coding: utf-8 -*-
import struct
import sys 
import codecs
# This code is building Wasf-Vec Model. It will ouput the file Wasf_model.wfv containing lines of (Word StartingFeature EndingFeature )
# Author: Tiba Zaki Abdulhameed April 11,2018 Western Michigan University/Al-Nahrain University
#run call example :python3 classsify.py Reversed_indexed_test.wf indexed_test.wf 
if(len(sys.argv)!=3):print('Arguments error ')
else:
	
	vocab=sys.argv[1]
	 
	 
	with codecs.open(vocab,'r','utf-8') as f:
	  d_Rev = dict(x.rstrip().split(None, 1) for x in f)# save the file as dictioary with word as key and feature is the value
	f.close()
	vocab=sys.argv[2]
	 
	with codecs.open(vocab,'r','utf-8') as f:
	  d_index = dict(x.rstrip().split(None, 1) for x in f)# save the file as dictioary with word as key and feature is the value
	f.close()
		
	v=[]
	w=[]
	for  word, feature in  d_index.items(): #iterate on any words dictionary and  produce Feature vectors
		a=word[::-1]#reverse string
		s=d_Rev[a] #get the feature
		v.append([int(feature),int(s)])
		w.append(word)
	#To produce worf-Features text file	
	with codecs.open('Wasf_model.wfv', 'w','utf-8') as wordFV:
		for i in range(len(w)):
			wordFV.write(w[i]+"\t"+str(v[i][0])+'\t'+str(v[i][1])+'\n')
	#to use it inside this code 
	model = dict(zip(w, v))
        # you can add your further code of using the model here as dictionary data type
