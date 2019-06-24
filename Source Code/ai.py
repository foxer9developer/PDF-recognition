import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

def insertMedicalReport(var1, var2,var3,var4,var5,var6,var7,var8,var9, var10,var11,var12,var13,var14,var15):
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='ai',
                             user='root',
                             password='')

        cursor = connection.cursor(prepared=True)

        sql_insert_query = """ INSERT INTO `medical_report`
                           VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        insert_tuple = (var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15)

        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into python_users table")

    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))

    finally:
       
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

dictionary =	{
  "Name of Patient": "abc",
  "age of Patient": "50",
  "Passport of Patient": "12345",
  "Name of doctor": "xyz",
  "Passport of doctor": "23456",
  "MCR no of doctor": "35",
  "Clinic Address": "Neemrana, Rajasthan",
  "doctor qualification": "MBBS",
  "doctor experience": "4-Year experience",
  "Clinical history of Patient": "5 year",
  "physical/medical exam of Patient": "Yes",
  "Date of examination": "2019-04-08",
  "Relevant examination": "Yes",
  "Patient Diagnosis": "No",
  "Patient medical capacity": "50"

  
}
var1 = dictionary.get('Name of Patient',"Not Available")
var2= dictionary.get('age of Patient')
var3 = dictionary.get('Passport of Patient')
var4 = dictionary.get('Name of doctor')
var5= dictionary.get('Passport of doctor')
var6= dictionary.get('MCR no of doctor')
var7 = dictionary.get('Clinic Address')
var8 = dictionary.get('doctor qualification')
var9= dictionary.get('doctor experience')
var10 = dictionary.get('Clinical history of Patient')
var11 = dictionary.get('physical/medical exam of Patient')
var12= dictionary.get('Date of examination')
var13= dictionary.get('Relevant examination')
var14 = dictionary.get('Patient Diagnosis')
var15= dictionary.get('Patient medical capacity')

print(var1)

#insertMedicalReport(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15)
