async function predict() {
    const input = document.getElementById('imageInput');
    const result = document.getElementById('result');

    if (!input.files[0]) {
        result.textContent = "Please upload an image first.";
        return;
    }

    const formData = new FormData();
    formData.append('file', input.files[0]);

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            result.textContent = `Predicted Class: ${data.prediction}`;
        } else {
            result.textContent = `Error: ${data.error}`;
        }
    } catch (err) {
        result.textContent = 'An error occurred: ' + err;
    }
}
