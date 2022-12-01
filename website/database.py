import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas",
        database="unes"
    )
    return db

def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas",
    )

    cursor = db.cursor()
    sql = "CREATE DATABASE unes; USE unes"
    cursor.execute(sql)
    db.commit()


def create_contato_table():
    db = connect_db()
    cursor = db.cursor()
    sql = "CREATE TABLE contato (email varchar(255), assunto varchar(255), descricao varchar(255));"
    cursor.execute(sql)
    db.commit()

def insert_data(email, assunto, desc):
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO contato (email, assunto, descricao) VALUES (%s, %s, %s);"
    values = [email, assunto, desc]
    cursor.execute(sql, values)
    db.commit()

def find_data():
    db = connect_db()
    cur = db.cursor()
    cur.execute("SELECT *  FROM contato;")
    info = cur.fetchall()
    return info
    
    
