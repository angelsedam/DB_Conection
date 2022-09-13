import pymysql
import pandas.io.sql
import pandas as pd
import numpy as np
import psycopg2
import pyodbc

#Connection for public mysq database https://docs.rfam.org/en/latest/database.html
connection = pymysql.connect(host='mysql-rfam-public.ebi.ac.uk',
                                 user='rfamro',
                                 password='',
                                 database='Rfam',
                                 port=4497)

#creating connection
mysqlcursor = connection.cursor()

#creating sql
sql = 'select clan_acc,id,previous_id,description,author from Rfam.clan'
sql_list = 'show tables from Rfam'
#execute sql
mysqlcursor.execute(sql)

#gather sql result
rows = mysqlcursor.fetchall()

#create a data frame from the sql result
dfmysql = pd.DataFrame(np.array(rows),columns=['clan_acc','id','previous_id','description','author'])

#mysql database
print(dfmysql.head(10))

#show tables from database
mysqlcursor.execute(sql_list)
list = mysqlcursor.fetchall()

#print 10 rows
for var in range(10):
    for l in list:
        print(l)
        break

#Close connection
connection.close()


##postgress
#creating connection for public database https://uibakery.io/sql-playground
con = psycopg2.connect("dbname=booking1663079836127xgbnkeaqlzgrvlhw  user=hzozrjzbwcrplgkidtajobhz@psql-mock-database-cloud  password=wsjbvkzezrnzvsovycuyjwja  host=psql-mock-database-cloud.postgres.database.azure.com  port=5432")

#Creating cursor
poscursor=con.cursor()

#Creating sql
pos_sql = 'select * from bookings'

#Executing sql
poscursor.execute(pos_sql)

#Select sql result
select=poscursor.fetchmany(5)
rows= poscursor.fetchall()
dfpos= pd.DataFrame(rows)
print('Postgress database')
print(select)
print(dfpos)

#Close connection
con.close()

##SQL Server

#conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=35.225.183.190;DATABASE=bdpython;UID=sqlserver;PWD=hyune123')
#cursor = conexion.cursor()
#sql = 'SELECT TOP (100) ProductID, Date,Zip , Units, Revenue FROM bi_salesFact' # sentencia SQL
#cursor.execute(sql) #ejecutar sentencia SQL mediante cursor
#rows = cursor.fetchall() #método fetchall
#for row in rows:
#    print(row)

#df2 = pd.DataFrame(np.array(rows),
#                   columns=["ProductID","Date","Zip","Units","Revenue"])
#df2.head()

#conexion.close() # cerrar la conexión