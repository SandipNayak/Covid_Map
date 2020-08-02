import pandas as pd
import geopandas as gpd
import numpy as np

data=pd.read_html("https://www.statista.com/statistics/1103458/india-novel-coronavirus-covid-19-cases-by-state/")[0]
data.rename(columns = {'Unnamed: 0':'STATE'}, inplace = True)
ind_data=gpd.read_file(r'C:\Users\PC\Desktop\ind shape file\IND_adm1.shp')
sum=0
total=list()
for i in range (len(data)):
    sum=sum+data['Confirmed'][i]+data['Recovered'][i]+data['Deceased'][i]
    total.append(sum)
    sum=0
data['Total']=total
data.drop(data.index[[24]],inplace = True)
data.sort_values('STATE', inplace = True)
print(data)
ind_data.plot(figsize = (10,10))
ind_data.replace("Uttaranchal","Uttarakhand",inplace=True)
ind_data.replace("Orissa","Odisha",inplace=True)
ind_data.drop(ind_data.index[[8,18,24,29]],inplace = True)
ind_data.reset_index(inplace=True)
print(ind_data)
ind_data['Recovered'] = data['Recovered']
ind = ind_data[['NAME_1','geometry','Recovered']]
ind.to_file(r'C:\Users\PC\Desktop\ind\ind.shp')

