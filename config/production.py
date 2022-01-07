from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='Eid#Vp0+8%)#;[EBSp|8!3w{2gSbsyNL',
    url='ls-f6db227e82f48c59fb7824ace81c4a75963842d8.cnkuzc0ouhty.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b's\xf9Be\xe8\x8c\xa6^\xef"\x80Y\xf5(\x7f3'
