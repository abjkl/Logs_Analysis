# Logs_Analysis
Logs_Analysis is the third project for Full Stack Web Developer course.

## Enviorment

### Python
In order to run the program, you should have the environment for **Python 3**.
You can install python3.7 by downloading files from [Python.org](https://www.python.org/getit/) 

### Module-psycopg2
The python program import psycopg2 module to control the PostgreSQL database. In order to run the program properly, you should install **psycopg2** at first

You can install **psycopg2** with the code ```pip3 install psycopg2```

### PostgreSQL
The data is stored use PostgreSQL. You can install PostgreSQL by downloading files from [https://www.postgresql.org/](https://www.postgresql.org/) 

### Data
You can download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) . You will need to unzip this file after downloading it. The file inside is called newsdata.sql. 

To build the reporting tool, you'll need to load the site's data into your local PostgreSQL database.

To load the data, use the command '''psql -d news -f newsdata.sql'''.

Makesure your data is in the same file with report.py

## How to use
### Run The Program
1. **Makesure your data is in the same file with report.py**
2. Then use the comand '''python3 report.py'''
3. The out come of the program will give you the answer for **popular articles,authors and error inforamation**

## Document

### report.py
This file can generate the outcome for the following issues:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Out come sample
You can also get the anwser by reviewing the '''out_come_sample.txt'''.
