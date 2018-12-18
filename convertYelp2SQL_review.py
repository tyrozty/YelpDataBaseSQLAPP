import json
import pymysql
import pickle

def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) 
    cursor.execute("DROP TABLE IF EXISTS review")
    sql = """CREATE TABLE review (
             review_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
             review_identifier  VARCHAR(100),
             user_id INT,
             business_id INT,
             stars INT,
             text VARCHAR(10000) NOT NULL,
             useful INT,
             funny INT,
             cool INT,
             PRIMARY KEY (review_id),
             CONSTRAINT `review_ibfk_1` FOREIGN KEY(user_id) REFERENCES user(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
             CONSTRAINT `review_ibfk_2` FOREIGN KEY(business_id) REFERENCES business(business_id) ON DELETE CASCADE ON UPDATE CASCADE
             )"""
    cursor.execute(sql)

def reviewdata_insert(db):
    with open('./../../user2id.pkl', 'rb') as u:
        user_to_id = pickle.load(u)

    with open('./../../business2id.pkl', 'rb') as b:
        business_to_id = pickle.load(b)

    with open('./../../review.pkl', 'rb') as f:
        review = pickle.load(f)
        i = 0
        for review_text in review:
            i += 1
            # print('processing line %d' %i + '......')
            try:
                if i == 1001:
                    break
                result = []
                if review_text['user_id'] in user_to_id and review_text['business_id'] in business_to_id:
                    result.append((review_text['review_id'], user_to_id[review_text['user_id']],business_to_id[review_text['business_id']],review_text['stars'], review_text['text'], review_text['useful'],review_text['funny'], review_text['cool']))
                    inesrt_re = "insert into review (review_identifier, user_id, business_id, stars, text, useful,funny, cool) values (%s, %s, %s, %s,%s, %s,%s, %s)"
                cursor = db.cursor()
                cursor.executemany(inesrt_re, result)
                db.commit()
            
            except Exception as e:
                db.rollback()
                print(str(e))
                break

if __name__ == "__main__":  
    db = pymysql.connect('localhost', 'tyrozty', 'Zty+19941007', 'yelptest', charset='utf8')
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()
