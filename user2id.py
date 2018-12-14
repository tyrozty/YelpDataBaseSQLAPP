import json
import pymysql
import pickle

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS user_id")
    sql = """CREATE TABLE user (
             user_id VARCHAR(100)
             user_identifier VARCHAR(100),
             PRIMARY KEY (user_id)
             )
             """
    cursor.execute(sql)

def reviewdata_insert(db):
    with open('./user.pkl', 'rb') as f:
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
    db = pymysql.connect('localhost', 'tyrozty', 'Zty+19941007', 'YELP', charset='utf8')
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()