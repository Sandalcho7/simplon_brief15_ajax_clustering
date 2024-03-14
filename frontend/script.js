document.addEventListener("DOMContentLoaded", function() {
    const runButton = document.getElementById("run-button");
    const dropdown = document.getElementById("endpoint-dropdown");
    const resultDisplay = document.querySelector(".result-display .big-number");

    runButton.addEventListener("click", function() {
        const selectedEndpoint = dropdown.value;
        if (selectedEndpoint) {
            fetch(selectedEndpoint)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const roundedInertia = Math.round(data.inertia);
                    resultDisplay.textContent = roundedInertia;
                })
                .catch(error => console.error('Error:', error));
        }
    });
});