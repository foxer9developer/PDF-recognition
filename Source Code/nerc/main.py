import os
## Set important paths
BASE = os.path.join(os.path.dirname(__file__), "..")
DOCS = os.path.join(BASE, "data", "docs")
def get_documents(path=DOCS):
    """
    Returns a filtered list of paths to PDF files representing our corpus.
    """
    for name in os.listdir(path):
        if name.startswith('p') and name.endswith('.pdf'):
            yield os.path.join(path, name)
# Print the total number of documents
print(len(list(get_documents())))
import re
import nltk
import codecs
import string
import subprocess
import unicodedata
## Create a path to extract the corpus.
CORPUS = os.path.join(BASE, "data", "corpus")
thisdict = {}
def extract_corpus(docs=DOCS, corpus=CORPUS):
    """
    Extracts a text corpus from the PDF documents and writes them to disk.
    """
    # Create corpus directory if it doesn't exist.
    if not os.path.exists(corpus):
        os.mkdir(corpus)
    # For each PDF path, use pdf2txt to extract the text file.
    for path in get_documents(docs):
        # Call the subprocess command (must be on your path)
        document = subprocess.check_output(['pdf2txt.py', path])
        # Encode UTF-u and remove non-printable characters
        document = filter(
            lambda char: char in string.printable,
            unicodedata.normalize('NFKD', document.decode('utf-8'))
        )
        # Write the document out to the corpus directory
        fname = os.path.splitext(os.path.basename(path))[0] + ".txt"
        outpath = os.path.join(corpus, fname)
        with codecs.open(outpath, 'w') as f:
            f.writelines(document)
        with open(outpath, "r") as file:
            data = file.readlines()
            for line in data:
                i = 0
                while i < len(line):
                    if ":" in line[i]:
                        key = line[0:i]
                        value = line[(i+1):(len(line)-2)]
                        thisdict[key] = value
                    i += 1
        print(thisdict)
# Run the extraction
extract_corpus()
# Create an NLTK corpus reader to access text data on disk.
kddcorpus = nltk.corpus.PlaintextCorpusReader(CORPUS, '.*\.txt')
words = nltk.FreqDist(kddcorpus.words())
count = sum(words.values())
vocab = len(words)
print("Corpus contains a vocabulary of {} and a word count of {}.".format(count, vocab))
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
def insertMedicalReport(var1, var2, var3, var4, var5, var6, var7):
    try:
        connection = mysql.connector.connect(host = 'localhost', database = 'ai', user = 'root', password = '')
        cursor = connection.cursor(prepared = True)
        sql_insert_query = """INSERT INTO `medical_report` VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)"""
        insert_tuple = (var1, var2, var3, var4, var5, var6, var7)
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
var1 = thisdict.get('Date of physical examination/mental state examination', "Not Available")
var2 = thisdict.get('Full name of patient', "Not Available")
var3 = thisdict.get('Date of birth of patient', "Not Available")
var4 = thisdict.get('Age of patient', "Not Available")
var5 = thisdict.get('Full name of doctor', "Not Available")
var6 = thisdict.get('Patients clinical history', "Not Available")
var7 = thisdict.get('Diagnosis', "Not Available")
#print(var1 + '\t' + var2 + '\t' + var3 + '\t' + var4 + '\t' + var5 + '\t' + var6 + '\t' + var7)
insertMedicalReport(var1, var2, var3, var4, var5, var6, var7)
