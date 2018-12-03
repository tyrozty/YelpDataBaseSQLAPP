import json
import pymysql
import pickle

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS tip")
    sql = """CREATE TABLE tip (
             text  VARCHAR(1024) NOT NULL,
             date VARCHAR(100),
             likes INT,
             business_id VARCHAR(200),
             user_id  VARCHAR(100)
             )"""
    cursor.execute(sql)
'''
def reviewdata_insert(db):
    with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_review.json', encoding='utf-8') as f:
        i = 0
        while True:
            i += 1
            # print('processing line %d' %i + '......')
            try:
                if i == 1001:
                    break
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
'''
def reviewdata_insert(db):
    with open('./../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_tip.json', encoding='utf-8') as f:
        i = 0
        while True:
            i += 1
            try:
                if i == 1001:
                    break
                lines = f.readline() 
                review_text = json.loads(lines)
                result = []
                #print(review_text)
                result.append((review_text['text'], review_text['date'],review_text['likes'],review_text['business_id'], review_text['user_id']))
                inesrt_re = "insert into tip(text, date, likes, business_id, user_id) values (%s, %s, %s, %s, %s)"
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