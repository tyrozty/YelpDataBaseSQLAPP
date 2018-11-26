import json
import pymysql

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS business")
    sql = """CREATE TABLE business (
             business_id VARCHAR(256),
             business_name VARCHAR(256),
             business_neighbor VARCHAR(256),
             location VARCHAR(256),
             stars FLOAT
             review_count INT)"""
    cursor.execute(sql)

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
                result.append((review_text['business_id'], review_text['name'],review_text['neighborhood'],review_text['address'],review_text['stars'],review_text['reveiw_count']))
                inesrt_re = "insert into business(business_id, business_name, business_neighbor, location, stars, review_count) values (%s, %s, %s, %s, %f, %d)"
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
