import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="data.env")

def connect_to_database():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn

def insert_review(conn:mysql.connector.MySQLConnection, prof_name:str, course_id:str,ease_of_scoring:int, teaching_quality:int, workload:int):
    query = "SELECT * FROM COURSE_REVIEW WHERE prof_name = %s AND course_id = %s"
    values = (prof_name, course_id)
    cursor = conn.cursor()
    cursor.execute(query, values)
    prev_results = cursor.fetchone()
    if(prev_results == None):
        query = "INSERT INTO COURSE_REVIEW VALUES (%s, %s, %s, %s, %s, %s)"
        values = ( course_id, prof_name, ease_of_scoring, teaching_quality, workload, 1)
        pass
    else:
        ease_of_scoring = (prev_results[2]*prev_results[5] + ease_of_scoring)/(prev_results[5]+1)
        teaching_quality = (prev_results[3]*prev_results[5] + teaching_quality)/(prev_results[5]+1)
        workload = (prev_results[4]*prev_results[5] + workload)/(prev_results[5]+1)
        query = "UPDATE COURSE_REVIEW SET ease_of_scoring = %s, teaching_quality = %s, workload = %s, number_of_reviews = %s" \
                " WHERE course_id = %s AND prof_name = %s"
        values = ( ease_of_scoring, teaching_quality, workload, prev_results[5]+1,course_id, prof_name)
    cursor.execute(query, values)
    conn.commit()

def fetch_review(conn:mysql.connector.MySQLConnection, course_id:str):
    query = "SELECT * FROM COURSE_REVIEW WHERE course_id = %s"
    values = (course_id,)
    cursor = conn.cursor()
    cursor.execute(query, values)
    prev_results = cursor.fetchall()
    return prev_results
    

""" course_review_db = connect_to_database()
cursor = course_review_db.cursor()
insert_review(course_review_db, "Some guy", "CS2030",5,2,5)
reviews = fetch_review(course_review_db, "CS2030")
print(reviews) """

#cursor.execute("DROP TABLE COURSE_REVIEWS")

