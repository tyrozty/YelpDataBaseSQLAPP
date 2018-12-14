import json
import pymysql
import pickle

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS location")
    sql = """CREATE TABLE location (
             location_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
             location_identifier VARCHAR(256),
             city VARCHAR(256),
             state VARCHAR(256),
             postal_code VARCHAR(256),
             latitude FLOAT, 
             longitude FLOAT,
             PRIMARY KEY (location_id)
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
                result.append((review_text['address'], review_text['city'],review_text['state'],review_text['postal code'], review_text['latitude'],review_text['longitude']))
                inesrt_re = "insert into location(location_identifier, city, state, postal_code, latitude, longitude) values (%s, %s, %s, %s, %s, %s)"
                cursor = db.cursor()
                cursor.executemany(inesrt_re, result)
                db.commit()
            except Exception as e:
                db.rollback()
                print(str(e))
                break
'''
def reviewdata_insert(db):
    with open('./business.pkl', 'rb') as f:
        business_info = pickle.load(f)
        for item in business_info:
            result = []
            result.append((item['address'],item['city'],item['state'],item['postal_code'], item['latitude'],item['longitude']))
            inesrt_re = "insert into location(location_identifier, city, state, postal_code, latitude, longitude) values (%s, %s, %s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.executemany(inesrt_re, result)
            db.commit()

if __name__ == "__main__":  
    db = pymysql.connect('localhost', 'tyrozty', 'Zty+19941007', 'YELP', charset='utf8')
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()
