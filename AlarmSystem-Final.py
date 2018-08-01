
# coding: utf-8

# In[1]:


#import of needed libraries

import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from IPython.display import display
from IPython.display import Image
import seaborn as sns
import itertools 


# In[2]:


#reading the file
data_file = pd.read_excel(r"C:/Users/bianc/Desktop/Original_TempAverageFINAL.xlsx")


# In[3]:


# Drop NA
#data_file.dropna(inplace=True)


# In[4]:


#make dataframe for time
time=data_file['UTClogTime']


# In[5]:


#make dataframe for cylinder temps
sensors=data_file.loc[:,'NO2 G/E CYL 1 EXH GAS OUTL TMP DegC':'NO2 G/E CYL 7 EXH GAS OUTL TMP DegC']


# In[6]:


#make std dev of cylinders combined per row
std_row=np.std(sensors,1)
data_file['Std Dev'] = std_row


# In[23]:


#calculate upper limit IQR of std dev
q75, q25 = np.percentile(std_row.dropna(), [75 ,25])
iqr = q75 - q25

max = q75 + (iqr*1.5)

print(max)


# In[8]:


#create lists for each cylinder and readings over 420/480
over420_1 = []
over420_2 = []
over420_3 = []
over420_4 = []
over420_5 = []
over420_6 = []
over420_7 = []

over480_1 = []
over480_2 = []
over480_3 = []
over480_4 = []
over480_5 = []
over480_6 = []
over480_7 = []

sd_list = []


# In[9]:


#Add readings Over420 to lists
for row in data_file['NO2 G/E CYL 1 EXH GAS OUTL TMP DegC']:
    if row > 420:
        over420_1.append(row)

for row in data_file['NO2 G/E CYL 2 EXH GAS OUTL TMP DegC']:
    if row > 420:
        over420_2.append(row)

for row in data_file['NO2 G/E CYL 3 EXH GAS OUTL TMP DegC']:
    if row > 420:
        over420_3.append(row)

for row in data_file['NO2 G/E CYL 4 EXH GAS OUTL TMP DegC']:
    if row > 420:
        over420_4.append(row)

for row in data_file['NO2 G/E CYL 5 EXH GAS OUTL TMP DegC']:
    if row > 420:
        over420_5.append(row)


for row in data_file['NO2 G/E CYL 6 EXH GAS OUTL TMP DegC']:
    if row > 420:
        over420_6.append(row)


for row in data_file['NO2 G/E CYL 7 EXH GAS OUTL TMP DegC']:
    if row > 420:
        over420_7.append(row)
                
#Add readings Over480 to lists

for row in data_file['NO2 G/E CYL 1 EXH GAS OUTL TMP DegC']:
    if row > 480:
        over480_1.append(row)

for row in data_file['NO2 G/E CYL 2 EXH GAS OUTL TMP DegC']:
    if row > 480:
        over480_2.append(row)

for row in data_file['NO2 G/E CYL 3 EXH GAS OUTL TMP DegC']:
    if row > 480:
        over480_3.append(row)

for row in data_file['NO2 G/E CYL 4 EXH GAS OUTL TMP DegC']:
    if row > 480:
        over480_4.append(row)

for row in data_file['NO2 G/E CYL 5 EXH GAS OUTL TMP DegC']:
    if row > 480:
        over480_5.append(row)

for row in data_file['NO2 G/E CYL 6 EXH GAS OUTL TMP DegC']:
    if row > 480:
        over480_6.append(row)

for row in data_file['NO2 G/E CYL 7 EXH GAS OUTL TMP DegC']:
    if row > 480:
        over480_7.append(row)


# In[10]:


#Add readings over std dev IQR to lists

for row in std_row:    
    if row > max:
        sd_list.append(row)


# In[11]:


#Add timestamp of readings over std dev IQR to list

stddev_time = []
for k in range (len(time)):
    if data_file['Std Dev'][k] > max:
        stddev_time.append(time[k])


# In[12]:


#Add timestamp of readings over 420 to list for each cylinder

cyl1_420_time = []

for k in range (len(time)):
    if data_file['NO2 G/E CYL 1 EXH GAS OUTL TMP DegC'][k] > 420:
        cyl1_420_time.append(time[k])
        
cyl2_420_time = []

for k in range (len(time)):
    if data_file['NO2 G/E CYL 2 EXH GAS OUTL TMP DegC'][k] > 420:
        cyl2_420_time.append(time[k])
        
cyl3_420_time = []

for k in range (len(time)):
    if data_file['NO2 G/E CYL 3 EXH GAS OUTL TMP DegC'][k] > 420:
        cyl3_420_time.append(time[k])
        
cyl4_420_time = []

for k in range (len(time)):
    if data_file['NO2 G/E CYL 4 EXH GAS OUTL TMP DegC'][k] > 420:
        cyl4_420_time.append(time[k])
        
cyl5_420_time = []

for k in range (len(time)):
    if data_file['NO2 G/E CYL 5 EXH GAS OUTL TMP DegC'][k] > 420:
        cyl5_420_time.append(time[k])
        
cyl6_420_time = []

for k in range (len(time)):
    if data_file['NO2 G/E CYL 6 EXH GAS OUTL TMP DegC'][k] > 420:
        cyl6_420_time.append(time[k])
        
cyl7_420_time = []

for k in range (len(time)):
    if data_file['NO2 G/E CYL 7 EXH GAS OUTL TMP DegC'][k] > 420:
        cyl7_420_time.append(time[k])


# In[13]:


#Add timestamp of readings over 480 to list for each cylinder

cyl1_time = []
for k in range (len(time)):
    if data_file['NO2 G/E CYL 1 EXH GAS OUTL TMP DegC'][k] > 480:
        cyl1_time.append(time[k])
        
cyl2_time = []
for k in range (len(time)):
    if data_file['NO2 G/E CYL 2 EXH GAS OUTL TMP DegC'][k] > 480:
        cyl2_time.append(time[k])
        
cyl3_time = []
for k in range (len(time)):
    if data_file['NO2 G/E CYL 3 EXH GAS OUTL TMP DegC'][k] > 480:
        cyl3_time.append(time[k])
        
cyl4_time = []
for k in range (len(time)):
    if data_file['NO2 G/E CYL 4 EXH GAS OUTL TMP DegC'][k] > 480:
        cyl4_time.append(time[k])
        
cyl5_time = []
for k in range (len(time)):
    if data_file['NO2 G/E CYL 5 EXH GAS OUTL TMP DegC'][k] > 480:
        cyl5_time.append(time[k])
        
cyl6_time = []
for k in range (len(time)):
    if data_file['NO2 G/E CYL 6 EXH GAS OUTL TMP DegC'][k] > 480:
        cyl6_time.append(time[k])
        
cyl7_time = []
for k in range (len(time)):
    if data_file['NO2 G/E CYL 7 EXH GAS OUTL TMP DegC'][k] > 480:
        cyl7_time.append(time[k])


# In[14]:


#combined Cyl vs SD lists

cyl1_SD_time = []
cyl1_xtemp = []
cyl1_SD = []

cyl2_SD_time = []
cyl2_xtemp = []
cyl2_SD = []

cyl3_SD_time = []
cyl3_xtemp = []
cyl3_SD = []

cyl4_SD_time = []
cyl4_xtemp = []
cyl4_SD = []

cyl5_SD_time = []
cyl5_xtemp = []
cyl5_SD = []

cyl6_SD_time = []
cyl6_xtemp = []
cyl6_SD = []

cyl7_SD_time = []
cyl7_xtemp = []
cyl7_SD = []


# In[15]:


#Zipped lists of timestamp plus list combined

cyl1_420 = list(zip(cyl1_420_time,over420_1))
cyl2_420 = list(zip(cyl2_420_time,over420_2))
cyl3_420 = list(zip(cyl3_420_time,over420_3))
cyl4_420 = list(zip(cyl4_420_time,over420_4))
cyl5_420 = list(zip(cyl5_420_time,over420_5))
cyl6_420 = list(zip(cyl6_420_time,over420_6))
cyl7_420 = list(zip(cyl7_420_time,over420_7))

cyl1 = list(zip(cyl1_time,over480_1))
cyl2 = list(zip(cyl2_time,over480_2))
cyl3 = list(zip(cyl3_time,over480_3))
cyl4 = list(zip(cyl4_time,over480_4))
cyl5 = list(zip(cyl5_time,over480_5))
cyl6 = list(zip(cyl6_time,over480_6))
cyl7 = list(zip(cyl7_time,over480_7))

#Std Dev list

SD = list(zip(stddev_time,sd_list))


# In[16]:


#Creating dataframes for lists

df_cyl1_420 = pd.DataFrame(cyl1_420, columns=['Time','Cyl 1>420'])
df_cyl2_420 = pd.DataFrame(cyl2_420, columns=['Time','Cyl 2>420'])
df_cyl3_420 = pd.DataFrame(cyl3_420, columns=['Time','Cyl 3>420'])
df_cyl4_420 = pd.DataFrame(cyl4_420, columns=['Time','Cyl 4>420'])
df_cyl5_420 = pd.DataFrame(cyl5_420, columns=['Time','Cyl 5>420'])
df_cyl6_420 = pd.DataFrame(cyl6_420, columns=['Time','Cyl 6>420'])
df_cyl7_420 = pd.DataFrame(cyl7_420, columns=['Time','Cyl 7>420'])

df_cyl1 = pd.DataFrame(cyl1, columns=['Time','Cyl 1>480'])
df_cyl2 = pd.DataFrame(cyl2, columns=['Time','Cyl 2>480'])
df_cyl3 = pd.DataFrame(cyl3, columns=['Time','Cyl 3>480'])
df_cyl4 = pd.DataFrame(cyl4, columns=['Time','Cyl 4>480'])
df_cyl5 = pd.DataFrame(cyl5, columns=['Time','Cyl 5>480'])
df_cyl6 = pd.DataFrame(cyl6, columns=['Time','Cyl 6>480'])
df_cyl7 = pd.DataFrame(cyl7, columns=['Time','Cyl 7>480'])

df_SD = pd.DataFrame(SD, columns=['Time','Std Dev>IQR'])


# In[17]:


#combined Cyl vs SD

for k in range (len(time)):
    if data_file['NO2 G/E CYL 1 EXH GAS OUTL TMP DegC'][k] > 480 and data_file['Std Dev'][k] > max:
        cyl1_SD_time.append(time[k])
        cyl1_xtemp.append(data_file['NO2 G/E CYL 1 EXH GAS OUTL TMP DegC'][k])

for k in range (len(time)):
    if data_file['NO2 G/E CYL 2 EXH GAS OUTL TMP DegC'][k] > 480 and data_file['Std Dev'][k] > max:
        cyl2_SD_time.append(time[k])
        cyl2_xtemp.append(data_file['NO2 G/E CYL 2 EXH GAS OUTL TMP DegC'][k])
        cyl2_SD.append(data_file['Std Dev'][k])
        
for k in range (len(time)):
    if data_file['NO2 G/E CYL 3 EXH GAS OUTL TMP DegC'][k] > 480 and data_file['Std Dev'][k] > max:
        cyl3_SD_time.append(time[k])
        cyl3_xtemp.append(data_file['NO2 G/E CYL 3 EXH GAS OUTL TMP DegC'][k])
        cyl3_SD.append(data_file['Std Dev'][k])
        
for k in range (len(time)):
    if data_file['NO2 G/E CYL 4 EXH GAS OUTL TMP DegC'][k] > 480 and data_file['Std Dev'][k] > max:
        cyl4_SD_time.append(time[k])
        cyl4_xtemp.append(data_file['NO2 G/E CYL 4 EXH GAS OUTL TMP DegC'][k])
        cyl4_SD.append(data_file['Std Dev'][k])
        
for k in range (len(time)):
    if data_file['NO2 G/E CYL 5 EXH GAS OUTL TMP DegC'][k] > 480 and data_file['Std Dev'][k] > max:
        cyl5_SD_time.append(time[k])
        cyl5_xtemp.append(data_file['NO2 G/E CYL 5 EXH GAS OUTL TMP DegC'][k])
        cyl5_SD.append(data_file['Std Dev'][k])
        
for k in range (len(time)):
    if data_file['NO2 G/E CYL 6 EXH GAS OUTL TMP DegC'][k] >= 480 and data_file['Std Dev'][k] >= max:
        cyl6_SD_time.append(time[k])
        cyl6_xtemp.append(data_file['NO2 G/E CYL 6 EXH GAS OUTL TMP DegC'][k])
        cyl6_SD.append(data_file['Std Dev'][k])
        
for k in range (len(time)):
    if data_file['NO2 G/E CYL 7 EXH GAS OUTL TMP DegC'][k] > 480 and data_file['Std Dev'][k] > max:
        cyl7_SD_time.append(time[k])
        cyl7_xtemp.append(data_file['NO2 G/E CYL 7 EXH GAS OUTL TMP DegC'][k])
        cyl7_SD.append(data_file['Std Dev'][k])


# In[18]:


#Cyl vs Std Dev lists

cyl1_comb = list(zip(cyl1_SD_time,cyl1_xtemp,cyl1_SD))
cyl2_comb = list(zip(cyl2_SD_time,cyl2_xtemp,cyl2_SD))
cyl3_comb = list(zip(cyl3_SD_time,cyl3_xtemp,cyl3_SD))
cyl4_comb = list(zip(cyl4_SD_time,cyl4_xtemp,cyl4_SD))
cyl5_comb = list(zip(cyl5_SD_time,cyl5_xtemp,cyl5_SD))
cyl6_comb = list(zip(cyl6_SD_time,cyl6_xtemp,cyl6_SD))
cyl7_comb = list(zip(cyl7_SD_time,cyl7_xtemp,cyl7_SD))


# In[19]:


df_cyl1_comb = pd.DataFrame(cyl1_comb, columns=['Time','Cyl 1>480','Std Dev>IQR'])
df_cyl2_comb = pd.DataFrame(cyl2_comb, columns=['Time','Cyl 2>480','Std Dev>IQR'])
df_cyl3_comb = pd.DataFrame(cyl3_comb, columns=['Time','Cyl 3>480','Std Dev>IQR'])
df_cyl4_comb = pd.DataFrame(cyl4_comb, columns=['Time','Cyl 4>480','Std Dev>IQR'])
df_cyl5_comb = pd.DataFrame(cyl5_comb, columns=['Time','Cyl 5>480','Std Dev>IQR'])
df_cyl6_comb = pd.DataFrame(cyl6_comb, columns=['Time','Cyl 6>480','Std Dev>IQR'])
df_cyl7_comb = pd.DataFrame(cyl7_comb, columns=['Time','Cyl 7>480','Std Dev>IQR'])


# In[20]:


#make final dataframe of all cylinder data for output to file

outlier_data = [df_cyl1_420, df_cyl2_420, df_cyl3_420, df_cyl4_420, df_cyl5_420, df_cyl6_420, df_cyl7_420, df_SD]
outlier_result = pd.concat(outlier_data,axis=1)

xtreme_data = [df_cyl1, df_cyl2, df_cyl3, df_cyl4, df_cyl5, df_cyl6, df_cyl7]
xtreme_result = pd.concat(xtreme_data,axis=1)

combined_data = [df_cyl1_comb, df_cyl2_comb, df_cyl3_comb, df_cyl4_comb, df_cyl5_comb, df_cyl6_comb, df_cyl7_comb]
combined_result = pd.concat(combined_data,axis=1)

total_data = [df_cyl1_420, df_cyl2_420, df_cyl3_420, df_cyl4_420, df_cyl5_420, df_cyl6_420, df_cyl7_420, df_SD, df_cyl1, df_cyl2, df_cyl3, df_cyl4, df_cyl5, df_cyl6, df_cyl7]
total_result = pd.concat(total_data,axis=1)


# In[22]:


#output to Excel

writer = pd.ExcelWriter(r"C:/Users/bianc/Desktop/Alarm_Output_File_G2.xlsx", engine='xlsxwriter')

outlier_result.to_excel(writer, 'Outliers', index=False)

#xtreme_result.to_excel(writer, 'Extreme Outliers', index=False)

combined_result.to_excel(writer, 'Extreme Outliers', index=False)

writer.save()

#CSV file
total_result.to_csv(r"C:/Users/bianc/Desktop/Alarm_Output_File_G2.csv")

