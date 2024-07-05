let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("mySlides");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 2000); // Change image every 2 seconds
}

function loadPredictions() {
    fetch('/predictions')
        .then(response => response.json())
        .then(data => {
            let predictionsDiv = document.getElementById('predictions');
            predictionsDiv.innerHTML = '<h2>Today\'s Predictions:</h2>';
            data.forEach(prediction => {
                predictionsDiv.innerHTML += `<p>${prediction.fixture}: ${prediction.prediction}</p>`;
            });
        });
}
