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
             description VARCHAR(1024),
             PRIMARY KEY (business_id),
             CONSTRAINT `business_ibfk_1` FOREIGN KEY (location_id) REFERENCES location(location_id) ON DELETE CASCADE ON UPDATE CASCADE
             )"""
    cursor.execute(sql)

def reviewdata_insert(db):
    with open('./../../location2id.pkl', 'rb') as d:
        location2id = pickle.load(d)

    with open('./../../business.pkl', 'rb') as f:
        business_info = pickle.load(f)
        for item in business_info:
            result = []
            if item['categories']:
                result.append((item['business_id'],item['name'],location2id[item['address']],item['stars'],item['review_count'], ' '.join(item['categories'].split(' '))))
                inesrt_re = "insert into business(business_identifier, business_name, location_id, stars, review_count, description) values (%s, %s, %s, %s, %s, %s)"
            else:
                result.append((item['business_id'],item['name'],location2id[item['address']],item['stars'],item['review_count'], None))
                inesrt_re = "insert into business(business_identifier, business_name, location_id, stars, review_count, description) values (%s, %s, %s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.executemany(inesrt_re, result)
            db.commit()

if __name__ == "__main__":  
    db = pymysql.connect('localhost', 'tyrozty', 'Zty+19941007', 'yelptest', charset='utf8')
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()
