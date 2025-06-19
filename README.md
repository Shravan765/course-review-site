# course-review-site
A simple Flask + MySQL web app to submit and view reviews for course–professor pairs.

This project is a simple Flask + MySQL-powered web application to collect and view course reviews based on:
- Ease of scoring
- Teaching quality
- Workload

## 🔧 Technologies Used

- **Frontend**: HTML, JavaScript
- **Backend**: Python with Flask
- **Database**: MySQL
- **Others**: python-dotenv, flask-cors

---

## 🚀 Features

- Submit course reviews via a form.
- View aggregated course reviews.
- Ratings are averaged across all submissions.
- Data is stored in a MySQL database.

---

## 📦 Project Structure

```plaintext
.
├── backend_flask.py             # Main Flask server
├── backend_mysql_work.py        # Database logic
├── review_submission.html       # Form to submit reviews
├── view_reviews.html            # Form to view reviews
├── review_submission_script.js  # JS for submission page
├── view_reviews_script.js       # JS for viewing reviews
├── requirements.txt             # Python dependencies
├── .env                         # (not included) Database credentials
├── mysql_table.txt              # SQL schema for the required table
└── README.md
```


## 📁 Environment Variables

Create a `.env` file in the root directory with the following content:

env
DB_HOST=your-database-host
DB_USER=your-username
DB_PASSWORD=your-password
DB_NAME=your-database-name


## 🛠️ Setup Instructions
1- Clone the repository:
git clone https://github.com/your-username/course-review-site.git
cd course-review-site

2- Install Python dependencies (ensure Python ≥ 3.7 and pip are installed):
pip install -r requirements.txt

3- Set up the MySQL database:

Create a database (course_reviews) in MySQL.
Use the table schema from mysql_table.txt

4- Create a .env file in the root directory with your actual MySQL credentials:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=course_reviews

5- Run the Flask server:
python backend_flask.py

If successful, you’ll see:
* Running on http://127.0.0.1:5000
