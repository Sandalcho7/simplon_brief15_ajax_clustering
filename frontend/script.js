const API_PATH = "http://localhost:8000"

document.addEventListener("DOMContentLoaded", function() {
    const runButton = document.getElementById("run-button");
    const dropdown = document.getElementById("endpoint-dropdown");
    const resultDisplay = document.querySelector(".result-display .big-number");

    runButton.addEventListener("click", function() {
        const selectedEndpoint = API_PATH + dropdown.value + "/score";
        if (selectedEndpoint) {
            fetch(selectedEndpoint)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const roundedResult = data.result.toFixed(3);
                    resultDisplay.textContent = roundedResult;
                })
                .catch(error => console.error('Error:', error));
        }
    });
});