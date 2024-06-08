#importing packages necessary for the program
import numpy as np
import pandas as pd
#importing package names which creates random names
import names as nm 
import random as rd
from datetime import timedelta, datetime


#Declaring the number of rows for our database
n = 1000
#creating all the dataframes for 4 tables
df_names = pd.DataFrame()
df_service_record = pd.DataFrame()
df_personal_details = pd.DataFrame()
df_health_data= pd.DataFrame()


#creating 1000 random names for the database.
def names():
    global names
    names = [] 
    for i in range(0, n) : 
        names.append(nm.get_full_name()) 
  
        
#creating 1000 unique employee ids for the database.        
def empid():
    global empid
    empid = np.random.choice(10000000, n, replace = False)
    rd.shuffle(empid)
    
    
empid()
names()
    

#Creating the dataframe for names table
df_name = pd.DataFrame({
    'emp_id' : empid,
    'names' : names})


#Converting the dataframe to csv file
df_name.to_csv('C:/Users/anton/OneDrive/Desktop/UH/Modules/Data Mining and Discovery/SQL_ASSIGNMENT_1/names.csv', index = False)


#creating rank for 1000 police officers    
def ranks():
    #Assigning all the ranks in the police department
    ranks = ['Commissioner', 'Deputy commissioner',  'Assistant commissioner', 
             'Deputy assistant commissioner',  'Commander' ,
             'Chief superintendent', 'Superintendent' ,'Chief inspector',
             'Inspector', 'Police sergeant', 'Police constable' ]
    global ranks_data 
    #Assigning the probabilities for each rank using p .
    ranks_data = np.random.choice(ranks, 1000, 
    p = [0.01, 0.02, 0.035, 0.035, 0.05, 0.05, 0.1, 0.1, 0.15, 0.15, 0.3 ])

ranks()


#Function to assign to police stations to police officers
def police_station():
    police_stations = ['26 Shepherds Bush Road', 'Acton Police Station',
'2 Town Square', 'Bethnal Green Police Station', 'Bexleyheath Police Station',
'Brixton Police Station', 'High Street', 'Charing Cross Police Station ',
'Chingford Police Station', 'Colindale Police Station',
 'Croydon Police Station', 'Dagenham Police Station', 'Edmonton Police Station'
 'Forest Gate Police Station',
'Harrow Police Station & Annexes' ,'Hayes Police Station', 
'Hounslow Police Station', 'Ilford Police Station' ,'Islington Police Station' ,
'Kensington Police Station',
'Kentish Town Police Station' ,'Kingston Police Station' ,
'Lavender Hill Police Station',
'43 Lewisham High Street' ,'Mitcham Police Station' ,
'Plumstead Police Station',
'Romford Police Station' ,'Stoke Newington Police Station',
 'Sutton Police Station' ,
'Tottenham Police Station' ,'Twickenham Police Station' ,
'Walworth Police Station',
'Wembley Police Station' ,'Wimbledon Police Station' ,'88 Church Street']
    global stations_data 
    stations_data = np.random.choice(police_stations, 1000) 
 
police_station()


def office_timings():
    office_timing = ['12:00 - 07:00', '06:00 - 13:00', '13:00 - 19:00', '19:00 - 01:00']
    p = [0.2, 0.2, 0.3, 0.3] 
    global office_timings_data 
    office_timings_data = np.random.choice(office_timing, n, p)
    
office_timings()
 
#Creating the dataframe for service record   
df_service_record = pd.DataFrame({
    'empid' : empid,
    'rank' : ranks_data,
    'police_staion' : stations_data,
    'office_timing' : office_timings_data
    })


#Function to assign ages to the police officers
def age():
    df_service_record['age'] = np.random.randint(20, 60 , n)
    #Assigning age to the top tier police officials 
    df_service_record.loc[(df_service_record['rank'] == 'Commissioner') | 
    (df_service_record['rank'] == 'Deputy commissioner') | (df_service_record['rank'] == 'Assistant commissioner') , 'age'] = np.random.randint(40,61, (len(df_service_record[(df_service_record['rank'] == 'Commissioner') | 
    (df_service_record['rank'] == 'Deputy commissioner') | (df_service_record['rank'] == 'Assistant commissioner')])))
    
     
    #Assigning age for mid level officials
    df_service_record.loc[(df_service_record['rank'] == 'Deputy assistant commissioner') | 
    (df_service_record['rank'] == 'Commander') | (df_service_record['rank'] == 'Chief superintendent') | (df_service_record['rank'] == 'Superintendent'), 'age'] = np.random.randint(28,40, (len(df_service_record[(df_service_record['rank'] == 'Deputy assistant commissioner') | 
    (df_service_record['rank'] == 'Commander') | (df_service_record['rank'] == 'Chief superintendent') | (df_service_record['rank'] == 'Superintendent')])))
    

    #Assigning age for lower level officials
    df_service_record.loc[(df_service_record['rank'] == 'Chief inspector') | 
    (df_service_record['rank'] == 'Inspector') | (df_service_record['rank'] == 'Police sergeant') | (df_service_record['rank'] == 'Police constable'), 'age'] = np.random.randint(20,32, (len(df_service_record[(df_service_record['rank'] == 'Chief inspector') | 
    (df_service_record['rank'] == 'Inspector') | (df_service_record['rank'] == 'Police sergeant') | (df_service_record['rank'] == 'Police constable')])))
    global age 
    age = df_service_record['age'].tolist()
                                                                                                                                                                                                           


#Function to assign age to the police officials
def no_of_arrests():
    global no_of_arrests
    
    df_service_record['no_of_arrests'] = np.random.randint(0,150, n)
    #Assigning the number of arrests for top level officials
    df_service_record.loc[(df_service_record['rank'] == 'Commissioner') | 
    (df_service_record['rank'] == 'Deputy commissioner') | (df_service_record['rank'] == 'Assistant commissioner') , 'no_of_arrests'] = np.random.randint(100,150, (len(df_service_record[(df_service_record['rank'] == 'Commissioner') | 
    (df_service_record['rank'] == 'Deputy commissioner') | (df_service_record['rank'] == 'Assistant commissioner')])))
   
    
    #Assigning the number of arrests for mid level officials
    df_service_record.loc[(df_service_record['rank'] == 'Deputy assistant commissioner') | 
    (df_service_record['rank'] == 'Commander') | (df_service_record['rank'] == 'Chief superintendent') | (df_service_record['rank'] == 'Superintendent'), 'no_of_arrests'] = np.random.randint(50,100, (len(df_service_record[(df_service_record['rank'] == 'Deputy assistant commissioner') | 
    (df_service_record['rank'] == 'Commander') | (df_service_record['rank'] == 'Chief superintendent') | (df_service_record['rank'] == 'Superintendent')])))
     
    
    #Assigning the number of arrests for lower level officials
    df_service_record.loc[(df_service_record['rank'] == 'Chief inspector') | 
    (df_service_record['rank'] == 'Inspector') | (df_service_record['rank'] == 'Police sergeant') | (df_service_record['rank'] == 'Police constable'), 'no_of_arrests'] = np.random.randint(0,50, (len(df_service_record[(df_service_record['rank'] == 'Chief inspector') | 
    (df_service_record['rank'] == 'Inspector') | (df_service_record['rank'] == 'Police sergeant') | (df_service_record['rank'] == 'Police constable')])))
    

#Function to assign number of medals to the police officials                                                                                                                                                                                                                         
def no_of_medals():
    global no_of_medals
    df_service_record['no_of_medals'] = np.random.randint(0, 7, n)
    
    #Assigning the number of medals to the top tier police officials 
    df_service_record.loc[(df_service_record['rank'] == 'Commissioner') | 
    (df_service_record['rank'] == 'Deputy commissioner') | (df_service_record['rank'] == 'Assistant commissioner') , 'no_of_medals'] = np.random.randint(5,7, (len(df_service_record[(df_service_record['rank'] == 'Commissioner') | 
    (df_service_record['rank'] == 'Deputy commissioner') | (df_service_record['rank'] == 'Assistant commissioner')])))
   
    
    #Assigning the number of medals for mid level officials
    df_service_record.loc[(df_service_record['rank'] == 'Deputy assistant commissioner') | 
    (df_service_record['rank'] == 'Commander') | (df_service_record['rank'] == 'Chief superintendent') | (df_service_record['rank'] == 'Superintendent'), 'no_of_medals'] = np.random.randint(3,6, (len(df_service_record[(df_service_record['rank'] == 'Deputy assistant commissioner') | 
    (df_service_record['rank'] == 'Commander') | (df_service_record['rank'] == 'Chief superintendent') | (df_service_record['rank'] == 'Superintendent')])))
    

    #Assigning the number of arrests for lower level officials
    df_service_record.loc[(df_service_record['rank'] == 'Chief inspector') | 
    (df_service_record['rank'] == 'Inspector') | (df_service_record['rank'] == 'Police sergeant') | (df_service_record['rank'] == 'Police constable'), 'no_of_medals'] = np.random.randint(0,3, (len(df_service_record[(df_service_record['rank'] == 'Chief inspector') | 
    (df_service_record['rank'] == 'Inspector') | (df_service_record['rank'] == 'Police sergeant') | (df_service_record['rank'] == 'Police constable')])))
   
age()
    

#Function to assign service experience to the police officials
def service_experience():
    df_service_record['service_exp'] = np.random.randint(0, 40, n)
    for i in range(len(age)):
        df_service_record.iloc[i,7] = age[i] - 20

    


no_of_arrests()
no_of_medals()
service_experience()



df_service_record.to_csv('C:/Users/anton/OneDrive/Desktop/UH/Modules/Data Mining and Discovery/SQL_ASSIGNMENT_1/service_record.csv', index = False)


def emailid():
    global email 
    email = []
    #print(names)
    #print(df_personal_details)
    for i in names:
        email.append(((i+"@gmail.com").replace(" ", "")).lower())
    #print(email)


def mobileno():
    global mobile 
    mobile = []
    for i in range(0,1000):
        a = []
        b = ''
        for i in range(0,10):
            a.append(np.random.randint(1,9))
        for i in a:
            b = b+str(i)
        mobile.append(b)

def address():
    global address
    address = []
    postcodes1 = [f'AL{str(i).zfill(2)}' for i in range(1, 2000)]
    postcodes2 = [f'EG{str(i).zfill(2)}' for i in range(1, 2000)]
    postcodes3 = [f'KL{str(i).zfill(2)}' for i in range(1, 2000)]
    postcodes4 = [f'NI{str(i).zfill(2)}' for i in range(1, 2000)]
    postcodes5 = [f'DS{str(i).zfill(2)}' for i in range(1, 2000)]
    address.extend(np.unique(np.random.choice(postcodes1, 200)))
    address.extend(np.unique(np.random.choice(postcodes2, 200)))
    address.extend(np.unique(np.random.choice(postcodes3, 200)))
    address.extend(np.unique(np.random.choice(postcodes4, 500)))
    address.extend(np.unique(np.random.choice(postcodes5, 400)))
    address = address[:1000]
    rd.shuffle(address)
    

emailid()
mobileno()
address()

    
df_personal_details = pd.DataFrame({
    'empid' : empid,
    'name' : names,
    'email' : email,
    'mobileno' : mobile,
    'address' : address
    })


df_personal_details.to_csv('C:/Users/anton/OneDrive/Desktop/UH/Modules/Data Mining and Discovery/SQL_ASSIGNMENT_1/personal_details.csv', index = False)



def height():
    global height
    height = []
    height = (np.random.randint(140, 200, n))

def weight():
    global weight
    weight = []
    weight = np.random.randint(50, 120, n)

def next_of_kin():
    global next_of_kin
    next_of_kin = [] 
    for i in range(0, n) : 
        next_of_kin.append(nm.get_full_name()) 


height()
weight()
next_of_kin()


df_health_data = pd.DataFrame({
    'empid' : empid,
    'age' : age,
    'height' : height,
    'weight' : weight,
    'next_of_kin' : next_of_kin
    })


df_health_data.to_csv('C:/Users/anton/OneDrive/Desktop/UH/Modules/Data Mining and Discovery/SQL_ASSIGNMENT_1/health_record.csv', index = False)