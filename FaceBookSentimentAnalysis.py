#VADER = Valence aware dictionary and sentiment reasoner and accounts the intensity of sentiment
#nltk = to analyse the sentiments of human data

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

file = 'filename in excel format'
xl = pd.ExcelFile(file)
dataFrames = xl.parse(xl.sheet_names[0]) #parsing data
dataFrames = xl.list(dataFrames['Timeline']) #removes blank rows
sid = SentimentIntensityAnalyzer()
str1 = 'UTC+05:30' #removing not-required data
for data in sid:
    a = data.find(str1)
    if(a == -1):
        ss=sid.polarity_scores(data) #sentiment analyser
        for k in ss:
            print(k,ss[k])
