document.getElementById('check-button').addEventListener('click', async () => {
    const inputText = document.getElementById('input-text').value;
    const resultElement = document.getElementById('result');

    try {
        const response = await fetch('http://localhost:5000/detect-xss', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: inputText }),
        });

        const data = await response.json();
        resultElement.textContent = data.message;
        resultElement.style.color = data.status === 'malicious' ? 'red' : 'green';
    } catch (error) {
        resultElement.textContent = 'Error checking for XSS.';
        resultElement.style.color = 'red';
    }
});