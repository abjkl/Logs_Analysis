#!/usr/bin/env python3

import psycopg2

# Get popular articles,authors and error proportion from the 'database'

DBNAME = "news"


def get_popular_articles():
    """Return most popular articles from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title as title, views.count as pv "
              "from articles "
              "join (select count(*) as count,substring(path from 10) as slug "
              "from log "
              "where status='200 OK' and path<>'/' group by path) as views "
              "on articles.slug=views.slug order by count desc limit 3;")
    articles = c.fetchall()
    db.close()
    return articles


def get_popular_authors():
    """Return authors and page views from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name, count(*) as pv "
              "from (select substring(path from 10) as slug from log where status='200 OK' and path<>'/') as views "
              "join articles on views.slug=articles.slug "
              "join authors on articles.author=authors.id "
              "group by authors.id "
              "order by pv desc;")
    authors = c.fetchall()
    db.close()
    return authors


def get_error():
    """Return the error percent more than 1% by day."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * "
              "from "
              "(select total.date as date, cast(error.count as FLOAT)/total.count as result from "
              "(select to_char(time,'yyyy-mm-dd') as date,count(*) as count from log  group by date) as total  "
              "join "
              "(select to_char(time,'yyyy-mm-dd') as date,count(*) as count from log "
              "where status='404 NOT FOUND' group by date) "
              "as error "
              "on total.date=error.date order by date DESC) "
              "as C "
              "where result>0.01 "
              "order by result desc;")
    error_date = c.fetchall()
    db.close()
    return error_date


# Generate article、author、error report.

def article_report():
    """Generate article report"""
    article_report_result = "\n".join('''· "%s" — %s views.''' % (title, pv) for title, pv in get_popular_articles())
    return article_report_result


def author_report():
    """Generate author report"""
    author_report_result = "\n".join('''· %s — %s views.''' % (name, pv) for name, pv in get_popular_authors())
    return author_report_result


def error_report():
    """Generate error report"""
    error_result = "\n".join('''· %s — %.2f%%.''' % (date, round(percent*100, 2)) for date, percent in get_error())
    return error_result


# Merge article、author、error reports together to make it easier to understand.

REPORT = '''1. What are the most popular three articles of all time?\n%s\n\n\
2. Who are the most popular article authors of all time?\n%s\n\n\
3. On which days did more than 1%% of requests lead to errors?\n%s'''


def main():
    report = REPORT % (article_report(), author_report(), error_report())
    return report

if __name__ == '__main__':
    print(main())
