#!/usr/bin/python
from __future__ import print_function
import psycopg2
import tkFileDialog, csv, sys
import names , random


def psql():
		
			# Get name Database
			dbName = "postgres"

			# Get student detail
			studentId = random.randint(1000000000000, 9999999999999)
			studentFirstName =  names.get_first_name()
			studentLastName = names.get_last_name()
			letter = 'A','B','B+','C','C+','D+','D','F'

			
			# Get record from CSV file
			# csvfile = tkFileDialog.askopenfilename(title='Select CSV file',filetypes = [(("CSV files",".csv"),("all files","*.*"))])
			record = readCSV("C:\Users\Trakansak-PC\Desktop\Python_CSVtoDB_PG-master\data\Sarik.csv")
			

			# Connect to DB
			psycopg2_connection = psycopg2.connect(dbname=dbName ,user='postgres', password='123456',port='3000')
			cursor = psycopg2_connection.cursor()

			# Insert Student Data
			cursor.execute("INSERT INTO Students (Student_id,First_name,Last_name)"
				"VALUES (%s,%s,%s);", (studentId,studentFirstName,studentLastName))

			# Insert Transcript
			for term in record:
				for subject in term:
					try:
						cursor.execute(
							"INSERT INTO Student_Records "
							"(SubjectID,SubjectName,Weight,Section,Grade,Term,Student_id) "
							"VALUES (%s,%s,%s,%s,%s,%s,%s);", 
							(subject[0], subject[1], subject[2], subject[3], random.choice(letter), 
							subject[5], studentId))
					except psycopg2.Error as error:
						print("Error: {}".format(error))

			# Check Status Completed
			print ("Complete")
			psycopg2_connection.commit()
			psycopg2_connection.close()


# Import File CSV
def readCSV(csvfile):
	with open(csvfile) as csvfile:
		next(csvfile)
		reader = csv.reader(csvfile)
		record, term = [], []
		for row in reader:			# add Subject to term
			term.append([row[0],row[1],row[2],row[3],row[4],row[5]])
			record.append(term)
			term = []
	return record

def main():
		x = 1
		while True:	
			try:
				psql()
			except Exception:
				pass

main()