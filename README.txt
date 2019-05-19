# Author: Tiba Zaki Abdulhameed April 11,2018 Western Michigan University/Al-Nahrain University

Prepare your corpus. All the codes assume utf8 file for Arabic. An example of a corpus is toyCorpus.txt provided
Please change toyCoupus.txt in runWasf.sh to be your crpus file name
you start runnig from
   ./runWasf.sh
This bash script will run count_word.py, produce the features, combine them in a model in python in Build_Wasf_Vec_Model.py
At the end you will get two output file; Vocabulary file corpus.txt.w  , Wasf_model.wfv that contains tuples of (Word StaringFeature EndingFeature)
Please cite the paper 
"Title: Wasf-Vec: Topology-Based Word Embedding for Modern Standard Arabic and Iraqi Dialect Ontology
Authors: TIBA ZAKI ABDULHAMEED, Department of Computer Science, College of Engineering and Applied Sciences,
 Western Michigan University, USA and Department of Computer Science, College of Science, Al-Nahrain University,Iraq
IMED ZITOUNI, Microsoft Research, USA
IKHLAS ABDEL-QADER, Department of Electrical and Computer Engineering, College of Engineering and Applied
Sciences, Western Michigan University, USA" 

