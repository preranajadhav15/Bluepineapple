#Create  Inspect  Basic Cleaning


import pandas as pd
#Create a DataFrame from a dict (at least 10 rows)
data={
    'Name': ['Prerana  ','Aaron','Aniket','Rohit','Yuvraj','Dhanesh','Roshan','Arin','Yash','Sakshi'],
    'Join_Date': ['15-12-2025','15-11-2025','23-12-2025','30-06-2023','04-03-2026','26-08-2025','01-01-2026','17-05-2026','13-12-2025','01-01-2026'],
    'Position': ['Cloud Analyst','Data Engineer','DevCon','Data Scientists','Devloper','UI Designer','Cloud Analyst','Data Engineer','Data Scientists','DevCon']
}
df=pd.DataFrame(data)

#Show .head() , .info() , .describe(include="all")
print("Head:\n",df.head()) 

print("Info:\n")
df.info()

print("Describe:\n",df.describe(include='all'))

#Convert a date column to datetime
df['Join_Date']=pd.to_datetime(df['Join_Date'],dayfirst=True)
print("Data type of date:",df['Join_Date'].dtype)

#Trim whitespace from string columns
col=df.select_dtypes(include="object").columns
df[col]=df[col].apply(lambda x : x.str.strip())

print("Head after triming white space:\n",df.head()) 