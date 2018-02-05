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
    "DROP TABLE Students CASCADE")
	tables['Student_Records'] = (
    "DROP TABLE Student_Records CASCADE")

	# Connect Database
	psycopg2_connection = psycopg2.connect(dbname=dbName ,user='postgres', password='123456',port='3000')
	cursor = psycopg2_connection.cursor()
	
	# Alert Create Tables
	for name, ddl in tables.iteritems():
			print ("Deleting table {}: ".format(name), end='')
			cursor.execute(ddl)

	psycopg2_connection.commit()
	psycopg2_connection.close()

main()
