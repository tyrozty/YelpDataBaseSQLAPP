import json
import pymysql

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS location")
    sql = """CREATE TABLE loaction (
             location_id VARCHAR(256),
             city VARCHAR(256),
             state VARCHAR(256),
             postal_code VARCHAR(256),
             latitude FLOAT, 
             longitude FLOAT)"""
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
                result.append((review_text['address'], review_text['city'],review_text['state'],review_text['postal code'], review_text['latitude'],review_text['longitude']))
                inesrt_re = "insert into location(location_id, city, state, postal_code, latitude, longitude) values (%s, %s, %s, %s,%f, %f)"
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
