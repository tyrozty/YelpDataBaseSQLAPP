#!/bin/bash
clear
echo 'begin building database'

python3 ./../../convertYelp2SQL_user.py
echo 'user table complete !!!'

python ./../../convertYelp2SQL_location.py
echo 'location table complete !!!'

python3 ./../../convertYelp2SQL_business.py
echo 'business table complete !!!'

python ./../../convertYelp2SQL_review.py
echo 'review table complete !!!'

python ./../../convertYelp2SQL_tip.py
echo 'tip table complete !!!'

python ./../../convertYelp2SQL_photo.py
echo 'photo table complete !!!'
