#(1.) Download the dataset from https://archive.ics.uci.edu/ml/datasets/Air+quality and save .csv file into /data
import pandas as pd
import datetime as dt
def main():
#(2.) Load the dataset into pandas data frame
    df=pd.read_excel('data/AirQualityUCI.xlsx')    
    #(3.) Create a timeseries data frame
    df = df.rename(columns = {'NO2(GT)':'NO2_GT'})
    #(4.) Remove all the values of NO2(GT) greater than 100 from march 2005 till june 2005
    df2 = df[df.Date.dt.year==2005]
    df2 = df2[df2.Date.dt.month>=3]
    df2 = df2[df2.Date.dt.month<=6]
    df2 = df2[df2.NO2_GT>100]
#print to file
df.to_csv('answer1.csv',sep=',',header=True)
main()
