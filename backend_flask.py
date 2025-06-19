from flask import Flask, request, jsonify
from backend_mysql_work import connect_to_database, insert_review, fetch_review  # adjust import path
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

course_review_db = connect_to_database()

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.get_json()

    course_code = data.get('code')
    prof = data.get('prof')
    ease = int(data.get('ease_of_scoring_marks'))
    teaching = int(data.get('teaching_quality'))
    workload = int(data.get('workload'))

    try:
        insert_review(course_review_db, prof, course_code, ease, teaching, workload)
        return jsonify({'status': 'success'})
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)})

@app.route('/get_reviews', methods=['POST'])
def get_reviews():
    data = request.get_json()
    course_id = data.get("code")

    try:
        results = fetch_review(course_review_db, course_id)
        formatted_results = []
        for row in results:
            formatted_results.append({
                "course_id": row[0],
                "prof_name": row[1],
                "ease_of_scoring": row[2],
                "teaching_quality": row[3],
                "workload": row[4],
                "number_of_reviews": row[5]
            })
        return jsonify({"status": "success", "reviews": formatted_results})
    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)})

if __name__ == '__main__':
    app.run(debug=True)