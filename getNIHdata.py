# Set path to data:
dataPath = 'C://Users/Shani/Documents/Python/NIHdata/csvFiles/'

# import modules we will need
import pandas
import numpy
import os
import glob
import matplotlib.pyplot as plt

# get a list of all csv files in the data directory
os.chdir(dataPath)
fileList = glob.glob('*.csv')

# get list of column headers
headerFile= open('columnHeadings.txt','r')
headerText = headerFile.read()
columns = headerText.split('\n')

# use pandas to read in the csv files

pieces = []
for file in fileList[:5]:
    frame = pandas.read_csv(file,names=columns,low_memory=False)
    pieces.append(frame)

NIHdata = pandas.concat(pieces,ignore_index=True)

NIHdata

RO1data = NIHdata[NIHdata.ACTIVITY.isin(['R01'])]
RO1data.fillna('Missing')
RO1countryCount = RO1data['ORG_COUNTRY'].value_counts()
RO1countryCount2 = RO1data.groupby('ORG_COUNTRY').size()
RO1costByCountry = RO1data.groupby('ORG_COUNTRY').TOTAL_COST.sum()
RO1byCountryAndIC = RO1data.pivot_table(rows='ORG_COUNTRY',cols='IC_NAME',aggfunc='size')
RO1countryCount.plot(kind='barh')

RO1data.to_csv('RO1data.csv')
RO1countryCount.to_csv('countryCount.csv')
RO1byCountryAndIC.to_csv('RO1byCountryAndIC.csv')


