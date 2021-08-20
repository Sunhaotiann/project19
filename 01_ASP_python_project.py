import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('IMVA.xls', sheet_name="IMVA")
selectAsia = data[['Periods','Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines',
       'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan',
       'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran',
       'Israel', 'Kuwait', 'Saudi Arabia', 'United Arab Emirates']]
print(selectAsia)



datas = selectAsia['Periods'].str.split(' ', n=1, expand=True)
print(datas)
selectAsia = selectAsia.assign(year = datas[0])
print(selectAsia)


asiaData1 = selectAsia[(selectAsia['Periods'] >= str(1978)) & (selectAsia['Periods'] <= str(1988))]
asiaHead = asiaData1.head(3)
asiaTail = asiaData1.tail(3)
print(asiaHead)
print(asiaTail)

selectAsia1 = asiaData1[['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines',
       'Thailand', 'Vietnam', 'China', 'Hong Kong SAR', 'Taiwan', 'Japan',
       'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Iran',
       'Israel', 'Kuwait', 'Saudi Arabia', 'United Arab Emirates']]
selectAsia1 = selectAsia1.replace(',','',regex = True)
selectAsia1 = selectAsia1.replace('na','0',regex = True)
print(selectAsia1)

ty = selectAsia1.astype(int)
print(ty.dtypes)
Notslt = ty.sum()
slt = ty.sum().sort_values(ascending=False)
print("****Sort***")
print(slt.head(3))

#All graph
ps = slt.sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No.of Travellers (In thousands)', fontsize=10)
plt.xticks(index, ps.index, fontsize=7 , rotation=80)
plt.title('All Asia Countries from (Period:1978 - 1987)')
plt.bar(ps.index, ps.values/1000)
plt.tight_layout()
plt.show();

#Top 3 graph
ps = slt.head(3).sort_values(ascending=False)
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('Top 3 Asia Countries from  (In thousands)', fontsize=10)
plt.xticks(index, ps.index, fontsize=7 , rotation=80)
plt.title('All Asia Countries from (Period:1978 - 1987)')
plt.bar(ps.index, ps.values/1000)
plt.tight_layout()
plt.show();
#scrabble graph
ps = slt.sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. of Travaler', fontsize=10)
plt.xticks(index, ps.index, fontsize=7 , rotation=90)
plt.title('1978-1987')
plt.scatter(ps.index, ps.values/1000)
plt.tight_layout()
plt.show();
