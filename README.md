# Logs_Analysis
## Enviorment Requirement 
The code is a python3 program, Thus please run with python3.0 or above.
## About the SQL
### Popular Aritcles
I joined 2 talbes whih is the log and the articles talbe. The joined colunm is the slug.
### Popular Author 
I order to get the right anwser, I join 3 talbes together. I user the log and article table to count pageview for each article, then join the article table with the author table to get the name of the auther and sum the page views together of every author.
### error information
In order to get this , I use 2 subquery to get the count for errors and the count for total request by day. Then I divided the error count with the total request. 
## About the out_put_sample
You can run report.py with python3 to get the same output.
Good luck~
