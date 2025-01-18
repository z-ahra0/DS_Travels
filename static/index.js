document.addEventListener('DOMContentLoaded', function() {
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');

    // Make sure the first slide is visible immediately
    slides[currentSlide].classList.add('active'); // Activate the first slide

    function showNextSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }

    // Start the slide show after a brief delay to allow the first image to load
    setInterval(showNextSlide, 3000); // Change slide every 3 seconds
});
