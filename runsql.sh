#!/bin/bash
clear
python convertYelp2SQL_review.py
echo 'review table complete !!!'
python convertYelp2SQL_user.py
echo 'user table complete !!!'
python convertYelp2SQL_business.py
echo 'business table complete !!!'
python convertYelp2SQL_loaction.py
echo 'location table complete !!!'