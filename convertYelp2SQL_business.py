import json
import pymysql
import pickle

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS business")
    sql = """CREATE TABLE business (
             business_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
             business_identifier VARCHAR(256),
             business_name VARCHAR(256),
             location_id INT,
             stars FLOAT,
             review_count INT,
             PRIMARY KEY (business_id),
             FOREIGN KEY (location_id) REFERENCES location(location_id)
             ON DELETE RESTRICT ON UPDATE CASCADE
             )"""
    cursor.execute(sql)
'''
def reviewdata_insert(db):
    with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_business.json', encoding='utf-8') as f:
        i = 0
        while True:
            i += 1
            # print('processing line %d' %i + '......')
            try:
                lines = f.readline() 
                review_text = json.loads(lines)
                result = []
                result.append((review_text['business_id'], review_text['name'],review_text['address'],review_text['stars'],review_text['reveiw_count']))
                inesrt_re = "insert into business(business_id, business_name, location, stars, review_count) values (%s, %s, %s, %s, %d)"
                cursor = db.cursor()
                cursor.executemany(inesrt_re, result)
                db.commit()
            except Exception as e:
                db.rollback()
                print(str(e))
                break
'''
def reviewdata_insert(db):
    with open('./location2id.pkl', 'rb') as d:
        location2id = pickle.load(d)

    with open('./business.pkl', 'rb') as f:
        business_info = pickle.load(f)
        for item in business_info:
            result = []
            result.append((item['business_id'],item['name'],location2id[item['address']],item['stars'],item['review_count']))
            inesrt_re = "insert into business(business_identifier, business_name, location_id, stars, review_count) values (%s, %s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.executemany(inesrt_re, result)
            db.commit()

if __name__ == "__main__":  
    db = pymysql.connect('localhost', 'tyrozty', 'Zty+19941007', 'YELP', charset='utf8')
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()
