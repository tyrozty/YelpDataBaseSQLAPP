import json
import pymysql
import pickle

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS photo")
    sql = """CREATE TABLE photo (
             photo_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
             photo_identifier  VARCHAR(100),
             business_id INT,
             caption VARCHAR(1024) NOT NULL,
             label VARCHAR(100),
             PRIMARY KEY (photo_id),
             FOREIGN KEY (business_id) REFERENCES business(business_id)
             ON DELETE RESTRICT ON UPDATE CASCADE
             )"""
    cursor.execute(sql)

def reviewdata_insert(db):
    with open('./business.pkl', 'rb') as f:
        business_info = pickle.load(f)
    
    with open('./business2id.pkl', 'rb') as b:
        business_to_id = pickle.load(b)

    with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_photo.json', encoding='utf-8') as f:
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
                if review_text['business_id'] in business_to_id:
                    result.append((review_text['photo_id'], business_to_id[review_text['business_id']],review_text['caption'],review_text['label']))
                    inesrt_re = "insert into photo(photo_identifier, business_id, caption, label) values (%s, %s, %s, %s)"
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