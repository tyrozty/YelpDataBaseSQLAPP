import json
import pymysql
import pickle
import MySQLdb as db

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS user")
    sql = """CREATE TABLE user (
             user_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
             user_identifier VARCHAR(100),
             user_name VARCHAR(100),
             review_count INT,
             yelping_since VARCHAR(100),
             fans INT,
             average_stars FLOAT,
             PRIMARY KEY (user_id)
             )
             """
    cursor.execute(sql)

def reviewdata_insert(db):
    with open('./../../user.pkl', 'rb') as f:
        user_info = pickle.load(f)
        print(len(user_info))
        for item in user_info:
            result = []
            result.append((item['user_id'], item['name'],item['review_count'],item['yelping_since'], item['fans'], item['average_stars']))
            inesrt_re = "insert into user(user_identifier, user_name, review_count, yelping_since, fans, average_stars) values (%s, %s, %s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.executemany(inesrt_re, result)
            db.commit()

if __name__ == "__main__":
    con = db.connect(user="tyrozty", passwd="Zty+19941007") # your account and password should be chaned here 
    cur = con.cursor()
    cur.execute('CREATE DATABASE yelptest')
    db = pymysql.connect('localhost', 'tyrozty', 'Zty+19941007', 'yelptest', charset='utf8') # your account and password should be chaned here
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()
