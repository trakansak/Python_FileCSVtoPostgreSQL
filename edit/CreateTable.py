#!/usr/bin/python
from __future__ import print_function
import psycopg2
import tkFileDialog, csv, sys

def main():

	# Get Name Database
	dbName = "postgres"

	# Creating Table on Database
	tables = {}
	tables['Students'] = (
    "CREATE TABLE Students ("
    "	Student_id varchar(13) NOT NULL,	"
    "	First_name varchar(100) NOT NULL,"
    " 	Last_name varchar(100) NOT NULL,"
    " 	PRIMARY KEY (Student_id))")
	tables['Student_Records'] = (
    "CREATE TABLE Student_Records ("
    "  	PK SERIAL PRIMARY KEY,"
    "  	SubjectID varchar(10) NOT NULL,"
    "  	SubjectName varchar(100) NOT NULL,"
    "  	Weight int NOT NULL,"
    "  	Section int NOT NULL,"
	"  	Grade varchar(2) NOT NULL,"
	"	Term	int	NOT NULL,"
	"	Student_id varchar(13) NOT NULL,"
	"	FOREIGN KEY (Student_id) REFERENCES Students(Student_id))")

	# Connect Database
	psycopg2_connection = psycopg2.connect(dbname=dbName ,user='postgres', password='123456',port='3000')
	cursor = psycopg2_connection.cursor()
	
	# Alert Create Tables
	for name, ddl in tables.iteritems():
			print ("Creating table {}: ".format(name), end='')
			cursor.execute(ddl)

	psycopg2_connection.commit()
	psycopg2_connection.close()

main()