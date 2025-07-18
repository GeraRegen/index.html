document.addEventListener('DOMContentLoaded', function() {
    // Функция для инициализации одного слайдера
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
            // Скрываем текущий слайд
            slides[currentSlide].classList.remove('active');
            dots[currentSlide].classList.remove('active');
            
            // Обновляем текущий слайд
            currentSlide = (index + slides.length) % slides.length;
            
            // Показываем новый слайд
            slides[currentSlide].classList.add('active');
            dots[currentSlide].classList.add('active');
        }
        
        // Обработчики кнопок
        prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
        nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));
        
        // Автопереключение каждые 5 секунд
        let slideInterval = setInterval(() => {
            goToSlide(currentSlide + 1);
        }, 5000);
        
        // Пауза при наведении
        sliderContainer.addEventListener('mouseenter', () => {
            clearInterval(slideInterval);
        });
        
        sliderContainer.addEventListener('mouseleave', () => {
            slideInterval = setInterval(() => {
                goToSlide(currentSlide + 1);
            }, 5000);
        });
    }
    
    // Инициализируем все слайдеры на странице
    document.querySelectorAll('.slider-container').forEach(initSlider);
    
    // Обработка кликов на карточки методов
    document.querySelectorAll('.method-card').forEach(card => {
        card.addEventListener('click', function() {
            const method = this.dataset.method;
            const section = document.getElementById(`${method}-method-content`);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});