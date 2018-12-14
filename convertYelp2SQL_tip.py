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
             tip_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
             text  VARCHAR(1024) NOT NULL,
             date VARCHAR(100),
             likes INT,
             business_id INT,
             user_id  INT,
             PRIMARY KEY (tip_id),
             FOREIGN KEY (business_id) REFERENCES business(business_id)
             ON DELETE RESTRICT ON UPDATE CASCADE,
             FOREIGN KEY (user_id) REFERENCES user(user_id)
             ON DELETE RESTRICT ON UPDATE CASCADE
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
    with open('./business2id.pkl', 'rb') as b:
        business_to_id = pickle.load(b)
    with open('./user2id.pkl', 'rb') as u:
        user_to_id = pickle.load(u)

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
                if review_text['business_id'] in business_to_id: 
                    result.append((review_text['text'], review_text['date'],review_text['likes'],business_to_id[review_text['business_id']], user_to_id[review_text['user_id']]))
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