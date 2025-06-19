document.body.style.backgroundColor = "DarkCyan";

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submit

        const data = {
            code: document.getElementById('code').value,
            prof: document.getElementById('prof').value,
            ease_of_scoring_marks: document.querySelector('input[name="ease_of_scoring_marks"]:checked')?.value,
            teaching_quality: document.querySelector('input[name="teaching_quality"]:checked')?.value,
            workload: document.querySelector('input[name="workload"]:checked')?.value
        };

        // Ensure no field is empty
        if (!data.code || !data.prof || !data.ease_of_scoring_marks || !data.teaching_quality || !data.workload) {
            alert("Please fill all fields!");
            return;
        }

        fetch('http://localhost:5000/submit_review', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.status === 'success') {
                alert('Review submitted successfully!');
                form.reset();
            } else {
                alert('Error: ' + result.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error submitting review.');
        });
    });
});