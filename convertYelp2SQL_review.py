import json
import pymysql

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS review")
    sql = """CREATE TABLE review (
             review_id  VARCHAR(100),
             user_id  VARCHAR(100),
             business_id VARCHAR(200),
             stars INT,
             text VARCHAR(10000) NOT NULL,
             useful INT,
             funny INT,
             cool INT)"""
    cursor.execute(sql)

def reviewdata_insert(db):
    with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_review.json', encoding='utf-8') as f:
        i = 0
        while True:
            i += 1
            # print('processing line %d' %i + '......')
            try:
                lines = f.readline() 
                review_text = json.loads(lines)  
                result = []
                result.append((review_text['review_id'], review_text['user_id'],review_text['business_id'],review_text['stars'], review_text['text'], review_text['useful'],review_text['funny'], review_text['cool']))
                inesrt_re = "insert into review(review_id, user_id, business_id, stars, text, useful,funny, cool) values (%s, %s, %s, %s,%s, %s,%s, %s)"
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
