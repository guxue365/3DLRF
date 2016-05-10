#! /usr/bin/env python
from subprocess import call
import pprint, os, sys,argparse,json,csv


count=0
#path_set=0
model_0_set = 0
model_1_set = 0
model_2_set = 0
model_3_set = 0

HOME_Dir='../datasets/3D models/CVLab/Kinect/ObjectRecognition/Scenes/2011_06_27/configwithbestview'
ConfigUp_Dir='../datasets'

for i in os.listdir(HOME_Dir):
    if i.endswith(".ini"): 
	ConfigPath=HOME_Dir+'/'+i
	#print ConfigPath
        with open(ConfigPath,'rb') as ConfigFile:
		for line in ConfigFile:
			if line.startswith("PATH = "): #and path_set==0:
				PATH=line.rstrip().split(None,2)[2]
				PATH=ConfigUp_Dir+PATH[1:-1]
				PATH=os.path.splitext(PATH)[0]+'_0'+'.ply'
#				path_set = 1
			if line.startswith("MODEL_0 = "): #and model_0_set==0:
				MODEL_0=line.rstrip().split(None,2)[2]
				MODEL_0=ConfigUp_Dir+MODEL_0[1:-1]
				MODEL_0=os.path.splitext(MODEL_0)[0]+'_0'+'.ply'
				model_0_set=1
			if line.startswith("MODEL_1 = "):# and model_1_set==0:
				MODEL_1=line.rstrip().split(None,2)[2]
				MODEL_1=ConfigUp_Dir+MODEL_1[1:-1]
				MODEL_1=os.path.splitext(MODEL_1)[0]+'_0'+'.ply'
				model_1_set=1
			if line.startswith("MODEL_2 = "):# and model_2_set==0:
				MODEL_2=line.rstrip().split(None,2)[2]
				MODEL_2=ConfigUp_Dir+MODEL_2[1:-1]
				MODEL_2=os.path.splitext(MODEL_2)[0]+'_0'+'.ply'
				model_2_set=1
			if line.startswith("MODEL_3 = "):# and model_3_set==0:
				MODEL_3=line.rstrip().split(None,2)[2]
				MODEL_3=ConfigUp_Dir+MODEL_3[1:-1]
				MODEL_3=os.path.splitext(MODEL_3)[0]+'_0'+'.ply'
				model_3_set=1
			if line.startswith("MODEL_0_GROUNDTRUTH = "):
				MODEL_0_GROUNDTRUTH=line.rstrip().split(None,2)[2]
				MODEL_0_GROUNDTRUTH=ConfigUp_Dir+MODEL_0_GROUNDTRUTH[1:-1]
			if line.startswith("MODEL_1_GROUNDTRUTH = "):
				MODEL_1_GROUNDTRUTH=line.rstrip().split(None,2)[2]
				MODEL_1_GROUNDTRUTH=ConfigUp_Dir+MODEL_1_GROUNDTRUTH[1:-1]
			if line.startswith("MODEL_2_GROUNDTRUTH = "):
				MODEL_2_GROUNDTRUTH=line.rstrip().split(None,2)[2]
				MODEL_2_GROUNDTRUTH=ConfigUp_Dir+MODEL_2_GROUNDTRUTH[1:-1]
			if line.startswith("MODEL_3_GROUNDTRUTH = "):
				MODEL_3_GROUNDTRUTH=line.rstrip().split(None,2)[2]
				MODEL_3_GROUNDTRUTH=ConfigUp_Dir+MODEL_3_GROUNDTRUTH[1:-1]
		try:
#			print path_set
			print PATH
			print MODEL_0	
			print MODEL_0_GROUNDTRUTH
			if model_0_set:
				count+=1
				MODEL_name=MODEL_0
				GROUNDTRUTH_name=MODEL_0_GROUNDTRUTH
				call(["../build/fpfh_low_dim", MODEL_0, PATH, MODEL_0_GROUNDTRUTH])
				model_0_set = 0
				print count
			print MODEL_1
			print MODEL_1_GROUNDTRUTH
			if model_1_set:
				count+=1	
				call(["../build/fpfh_low_dim", MODEL_1, PATH, MODEL_1_GROUNDTRUTH])
				model_1_set = 0
				print count
			print MODEL_2
			print MODEL_2_GROUNDTRUTH
			if model_2_set:
				count+=1
				call(["../build/fpfh_low_dim", MODEL_2, PATH, MODEL_2_GROUNDTRUTH])
				model_2_set = 0
				print count
			print MODEL_3
			print MODEL_3_GROUNDTRUTH
			if model_3_set:
				count+=1
				call(["../build/fpfh_low_dim", MODEL_3, PATH, MODEL_3_GROUNDTRUTH])
				model_3_set = 0
				print count
		except:
			pass
    else:
#	path_set=0
	

	
	

        continue
