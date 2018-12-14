import json
from tqdm import tqdm
import pickle

# loading review .......
with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_review.json', encoding='utf-8') as f:
    user_id = []
    business_id = []
    cnt = 0
    for line in f:
        if cnt == 1000:
            break
        cnt += 1
        review_text = json.loads(line)
        user_id.append(review_text['user_id'])
        business_id.append(review_text['business_id'])
print(len(user_id))

with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_tip.json', encoding='utf-8') as f:
    cnt = 0
    for line in f:
        if cnt == 1000:
            break
        cnt += 1
        review_text = json.loads(line)
        user_id.append(review_text['user_id'])
        business_id.append(review_text['business_id'])
print(len(user_id))

with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_photo.json', encoding='utf-8') as f:
    cnt = 0
    for line in f:
        if cnt == 1000:
            break
        cnt += 1
        review_text = json.loads(line)
        #user_id.append(review_text['user_id'])
        business_id.append(review_text['business_id'])
print(len(user_id))
print(len(business_id))

# loading user ......
with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_user.json', encoding='utf-8') as f:
    new_user_info = []
    for line in tqdm(f):
        user_info = json.loads(line)
        if user_info['user_id'] in user_id:
            new_user_info.append(user_info)
print(len(new_user_info))

user_to_id = {}
cnt = 1
for item in new_user_info:
    user_to_id[item['user_id']] = cnt
    cnt += 1
print(len(user_to_id))

pickle.dump(new_user_info, open('./user.pkl', 'wb'))
pickle.dump(user_to_id, open('./user2id.pkl', 'wb'))

# loading business ......
with open('../../EECS595/EECS595/yelp_dataset/yelp_academic_dataset_business.json', encoding='utf-8') as f:
    new_business_info = []
    for line in tqdm(f):
        business_info = json.loads(line)
        if business_info['business_id'] in business_id:
            new_business_info.append(business_info)
pickle.dump(new_business_info, open('./business.pkl', 'wb'))
print(len(new_business_info))

business_to_id = {}
cnt = 1
for item in new_business_info:
   business_to_id[item['business_id']] = cnt
   cnt += 1
print(len(business_to_id))
pickle.dump(business_to_id, open('./business2id.pkl', 'wb'))

location_to_id = {}
cnt = 1
for item in new_business_info:
    if item['address'] not in location_to_id:
        location_to_id[item['address']] = cnt
        cnt += 1
print(len(location_to_id))
pickle.dump(location_to_id, open('./location2id.pkl', 'wb'))




