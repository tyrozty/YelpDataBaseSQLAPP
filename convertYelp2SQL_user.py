import json
import pymysql

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS user")
    sql = """CREATE TABLE user (
             user_id VARCHAR(100),
             name VARCHAR(100),
             review_count INT,
             yelping_since VARCHAR(100),
             useful INT,
             funny INT,
             cool INT,
             fans INT,
             average_stars FLOAT)"""
    cursor.execute(sql)

def reviewdata_insert(db):
    with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_user.json', encoding='utf-8') as f:
        i = 0
        while True:
            i += 1
            # print('processing line %d' %i + '......')
            try:
                lines = f.readline() 
                review_text = json.loads(lines)  
                result = []
                result.append((review_text['user_id'], review_text['name'],review_text['review_count'],review_text['yelping_since'], review_text['useful'],review_text['funny'], review_text['cool'], review_text['fans'], review_text['average_stars']))
                inesrt_re = "insert into review(user_id, name, review_count, yelping_since, useful, funny, cool, fans, average_stars) values (%s, %s, %s, %s,%s, %s,%s, %s, %s)"
                cursor = db.cursor()
                cursor.executemany(inesrt_re, result)
                db.commit()
            except Exception as e:
                db.rollback()
                print(str(e))
                break

if __name__ == "__main__":  
    db = pymysql.connect('localhost', 'tyrozty', 'Zty+19941007', 'YELP', charset='utf8')
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()
