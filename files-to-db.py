import argparse
import sqlite3
import csv

parser = argparse.ArgumentParser()

parser.add_argument("filename", help="Source file", type=str)
parser.add_argument("database", help="Destination database", type=str)
parser.add_argument("delimiter", help="Delimiter", type=str)

args = parser.parse_args()

con = sqlite3.connect(args.database)
cur = con.cursor()

lines = []

with open(args.filename, "r") as file:
    contents = file.read()
    for entry in contents.split(args.delimiter):
        lines.append(entry)

data = list(zip(range(1, len(lines)), lines))

con.executemany("INSERT INTO ... VALUES (?, ?)", data)

con.commit()
con.close()
