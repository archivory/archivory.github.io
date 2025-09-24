// Homepage carousel JS with visible previous and next images
let currentSlide = 0;
const slides = document.querySelectorAll('.homepage-carousel-slide');
const totalSlides = slides.length;

function showSlide(index) {
  slides.forEach((slide, i) => {
    if (i === index) {
      slide.style.display = 'block';
      slide.style.opacity = '1';
      slide.style.transform = 'scale(1)';
      slide.style.zIndex = '2';
    } else if (i === (index - 1 + totalSlides) % totalSlides) {
      slide.style.display = 'block';
      slide.style.opacity = '0.5';
      slide.style.transform = 'scale(0.8) translateX(-120%)'; // space left
      slide.style.zIndex = '1';
    } else if (i === (index + 1) % totalSlides) {
      slide.style.display = 'block';
      slide.style.opacity = '0.5';
      slide.style.transform = 'scale(0.8) translateX(120%)'; // space right
      slide.style.zIndex = '1';
    } else {
      slide.style.display = 'none';
      slide.style.opacity = '0';
      slide.style.transform = 'scale(0.8)';
      slide.style.zIndex = '0';
    }
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  showSlide(currentSlide);
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  showSlide(currentSlide);
}

document.addEventListener('DOMContentLoaded', () => {
  showSlide(currentSlide);
  document.getElementById('homepage-carousel-next').onclick = nextSlide;
  document.getElementById('homepage-carousel-prev').onclick = prevSlide;
});
