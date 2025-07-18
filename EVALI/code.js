document.addEventListener('DOMContentLoaded', function() {
    // Функция для инициализации слайдера
    function initSlider(sliderContainer) {
        const slides = sliderContainer.querySelectorAll('.slide');
        const dotsContainer = sliderContainer.querySelector('.slider-dots');
        const prevBtn = sliderContainer.querySelector('.slider-prev');
        const nextBtn = sliderContainer.querySelector('.slider-next');
        
        let currentSlide = 0;
        
        // Создаем точки-индикаторы
        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('slider-dot');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotsContainer.appendChild(dot);
        });
        
        const dots = sliderContainer.querySelectorAll('.slider-dot');
        
        // Функция переключения слайда
        function goToSlide(index) {
            slides[currentSlide].classList.remove('active');
            dots[currentSlide].classList.remove('active');
            
            currentSlide = (index + slides.length) % slides.length;
            
            slides[currentSlide].classList.add('active');
            dots[currentSlide].classList.add('active');
        }
        
        // Обработчики кнопок
        prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
        nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));
        
        // Автопереключение
        let slideInterval = setInterval(() => goToSlide(currentSlide + 1), 5000);
        
        // Пауза при наведении
        sliderContainer.addEventListener('mouseenter', () => clearInterval(slideInterval));
        sliderContainer.addEventListener('mouseleave', () => {
            slideInterval = setInterval(() => goToSlide(currentSlide + 1), 5000);
        });
    }
    
    // Инициализация всех слайдеров
    document.querySelectorAll('.slider-container').forEach(initSlider);
    
    // Обработка раскрывающихся блоков
    document.querySelectorAll('.expandable-header').forEach(header => {
        header.addEventListener('click', function() {
            const block = this.closest('.expandable-block');
            block.classList.toggle('active');
            
            // Прокрутка к раскрытому контенту
            if (block.classList.contains('active')) {
                setTimeout(() => {
                    block.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 300);
            }
        });
    });
});