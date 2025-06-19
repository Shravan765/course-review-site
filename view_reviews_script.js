document.body.style.backgroundColor = "DarkTurquoise";

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('take_review');
    const resultDiv = document.getElementById('Present_reviews');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent page reload

        const code = document.getElementById('code').value;

        if (!code) {
            alert("Please enter a course code.");
            return;
        }

        fetch('http://localhost:5000/get_reviews', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code: code })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = ''; // Clear previous results

            if (data.status === 'success' && data.reviews.length > 0) {
                data.reviews.forEach(review => {
                    const reviewHTML = `
                        <div style="border:1px solid #000; padding:10px; margin:10px;">
                            <strong>Professor:</strong> ${review.prof_name} <br>
                            <strong>Ease of Scoring:</strong> ${review.ease_of_scoring.toFixed(2)} <br>
                            <strong>Teaching Quality:</strong> ${review.teaching_quality.toFixed(2)} <br>
                            <strong>Workload:</strong> ${review.workload.toFixed(2)} <br>
                            <strong>Number of Reviews:</strong> ${review.number_of_reviews}
                        </div>
                    `;
                    resultDiv.innerHTML += reviewHTML;
                });
            } else if (data.status === 'success') {
                resultDiv.innerHTML = 'No reviews found for this course.';
            } else {
                resultDiv.innerHTML = 'Error: ' + data.message;
            }
        })
        .catch(err => {
            console.error(err);
            resultDiv.innerHTML = 'An error occurred while fetching reviews.';
        });
    });
});
