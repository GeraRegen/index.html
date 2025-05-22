document.addEventListener('DOMContentLoaded', function() {
    // Инициализация всех слайдеров на странице
    const sliders = document.querySelectorAll('.fullscreen-slider');
    sliders.forEach((slider, sliderIndex) => {
        // Для каждого слайдера свой индекс текущего слайда
        slider.currentSlideIndex = 1;
        
        // Инициализация первого слайда
        showSlides(slider.currentSlideIndex, slider);
        
        // Запуск автосмены для каждого слайдера
        slider.interval = setInterval(() => {
            plusSlides(1, slider);
        }, 5000);
        
        // Назначение обработчиков для стрелок и точек
        const arrows = slider.querySelectorAll('.slider-arrow');
        arrows.forEach(arrow => {
            arrow.addEventListener('click', function() {
                const direction = this.classList.contains('prev') ? -1 : 1;
                plusSlides(direction, slider);
            });
        });
        
        const dots = slider.querySelectorAll('.slider-dot');
        dots.forEach((dot, dotIndex) => {
            dot.addEventListener('click', function() {
                currentSlide(dotIndex + 1, slider);
            });
        });
    });
});

function plusSlides(n, slider) {
    showSlides(slider.currentSlideIndex += n, slider);
    resetTimer(slider);
}

function currentSlide(n, slider) {
    showSlides(slider.currentSlideIndex = n, slider);
    resetTimer(slider);
}

function showSlides(n, slider) {
    const slides = slider.querySelectorAll('.slide');
    const dots = slider.querySelectorAll('.slider-dot');
    
    if (n > slides.length) { slider.currentSlideIndex = 1; }
    if (n < 1) { slider.currentSlideIndex = slides.length; }
    
    // Скрыть все слайды
    slides.forEach(slide => {
        slide.classList.remove('active');
    });
    
    // Деактивировать все точки
    dots.forEach(dot => {
        dot.classList.remove('active');
    });
    
    // Показать текущий слайд
    slides[slider.currentSlideIndex - 1].classList.add('active');
    
    // Активировать соответствующую точку
    if (dots.length > 0) {
        dots[slider.currentSlideIndex - 1].classList.add('active');
    }
}

function resetTimer(slider) {
    clearInterval(slider.interval);
    slider.interval = setInterval(() => {
        plusSlides(1, slider);
    }, 5000);
}

