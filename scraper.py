from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from piazza_api import Piazza
from utils import *
import argparse
import nltk

piazza = Piazza()
piazza.user_login(email=Config.username, password=Config.password)
course = piazza.network(Config.courseid)
engine = create_engine('sqlite:///test.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


for i in range(270, 275):
  post = course.get_post(i)
  title = remove_tags(post['history'][0]['subject'])
  body = remove_tags(post['history'][0]['content'])
  f = open("test.txt", "a")
  for line in body:
    f.write(line)
  f.write("\n")


f.close()


