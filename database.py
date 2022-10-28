import sqlite3
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    username = "admin",
    password = "admin",
)

print(db)