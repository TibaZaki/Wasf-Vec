#!/bin/sh
	c=toyCorpus.txt #this file is prepared coupus
	
	echo "Start counting"
        #PLEASE CHANGE toyCorpus.txt TO YOUR CORPUS FILE NAME
        python3 count_word.py toyCorpus.txt # will output a vocabulary file toyCorpus.txt.w 
	
	echo "cleanup the vocabulary words"
					
	sed -i '/^$/d' ${c}.w  #we need to delete empty lines if exsit 
	#-----------------------------------------------------------------------	
	#Was-Vec vocabulary sort for feature extraction
	sort -u ${c}.w > ${c}.sorted.w
	awk '{print $0 "\t" NR}' ${c}.sorted.w > ${c}.indexed.wf # add column indexing the sorted vocabulary. This file is considered (word,feature pair)
	rev ${c}.sorted.w > ${c}.Reversed.w #reverse the letters order of each word
	sort -u ${c}.Reversed.w > ${c}.Reversed_sorted.w
	awk '{print  $0 "\t" NR }' ${c}.Reversed_sorted.w > ${c}.Reversed_indexed.wf # add column indexing the sorted vocabulary. This file is considered (word, postfix feature pair)
	
	rm ${c}.Reversed.w
	rm ${c}.sorted.w
	rm ${c}.Reversed_sorted.w
	
	python3 Build_Wasf_Vec_Model.py ${c}.Reversed_indexed.wf ${c}.indexed.wf 
	rm ${c}.Reversed_indexed.wf 
	rm ${c}.indexed.wf 
