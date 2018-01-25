# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:34:23 2017

@author: rishabh.mishra
"""

import pandas as pd
import random
import numpy as np

data_jan=pd.read_excel("E:\\30HacksModel\\month_data\\jan.xlsx")                       
data_feb=pd.read_excel("E:\\30HacksModel\\month_data\\feb.xlsx")                       
data_mar=pd.read_excel("E:\\30HacksModel\\month_data\\mar.xlsx")
data_apr=pd.read_excel("E:\\30HacksModel\\month_data\\apr.xlsx")
data_may=pd.read_excel("E:\\30HacksModel\\month_data\\may.xlsx")
data_jun=pd.read_excel("E:\\30HacksModel\\month_data\\jun.xlsx")                      
data_jul=pd.read_excel("E:\\30HacksModel\\month_data\\jul.xlsx")
data_aug=pd.read_excel("E:\\30HacksModel\\month_data\\aug.xlsx")
data_sep=pd.read_excel("E:\\30HacksModel\\month_data\\sep.xlsx")
data_oct=pd.read_excel("E:\\30HacksModel\\month_data\\oct.xlsx")
data_nov=pd.read_excel("E:\\30HacksModel\\month_data\\nov.xlsx")
data_dec=pd.read_excel("E:\\30HacksModel\\month_data\\dec.xlsx")
#data.head()
#data.shape
# X value needs to be taken from the server
from sklearn.externals import joblib
classifier = joblib.load("E:\\30HacksModel\\DTreeModel.pkl")

month = [31,28,31,30,31,30,31,31,30,31,30,31]

pred_day = [ ]

##
#data_month = data_jan.iloc[0, :]
#data_month = pd.DataFrame(data_month)
#data_month = data_month.transpose()
#pred = classifier.predict(data_month)

def getValues(x):
	max = month[int(x)]
	s1=" "
    for i in range(0, max) :
		if x == 0:
			ind=random.randint(0,495)
			data_month = data_jan.iloc[ind, :]
			data_month = pd.DataFrame(data_month)
			data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 1:
			ind=random.randint(0,451)
            data_month = data_feb.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 2:
            ind=random.randint(0,478)
            data_month = data_mar.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 3:
            ind=random.randint(0,449)
            data_month = data_apr.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 4:
            ind=random.randint(0,464)
            data_month = data_may.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 5:
            ind=random.randint(0,449)
            data_month = data_jun.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 6:
            ind=random.randint(0,464)
            data_month = data_jul.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 7:
            ind=random.randint(0,464)
            data_month = data_aug.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 8:
            ind=random.randint(0,469)
            data_month = data_sep.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 9:
            ind=random.randint(0,495)
            data_month = data_oct.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 10:
            ind=random.randint(0,479)
            data_month = data_nov.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
        elif x == 11:
            ind=random.randint(0,495)
            data_month = data_dec.iloc[ind, :]
            data_month = pd.DataFrame(data_month)
            data_month = data_month.transpose()
			s1+=str(classifier.predict(data_month))
    return s1



