import mysql.connector

def create_database():
    import mysql.connector

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas", #"MUL1NH4S"
    )
    cur = db.cursor()

    sql = "CREATE DATABASE unes; USE unes"
    cur.execute(sql)
    db.commit()

def connect_db():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas", #"MUL1NH4S"
        database="unes"
    )
    return db