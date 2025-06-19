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

.
├── backend_flask.py # Main Flask server
├── backend_mysql_work.py # Database logic
├── review_submission.html # Form to submit reviews
├── view_reviews.html # Form to view reviews
├── review_submission_script.js # JS for submission page
├── view_reviews_script.js # JS for viewing reviews
├── requirements.txt # Python dependencies
├── .env # (not included) Database credentials
├── mysql_table.txt (To show what kind of a table does the server need to have)
└── README.md


## 📁 Environment Variables

Create a `.env` file in the root directory with the following content:

```env
DB_HOST=your-database-host
DB_USER=your-username
DB_PASSWORD=your-password
DB_NAME=your-database-name
