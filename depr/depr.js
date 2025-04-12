document.addEventListener('DOMContentLoaded', function() {
    const blocks = document.querySelectorAll('.antidepressant-block');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');
    let currentIndex = 0;

    // Показываем первый блок
    showBlock(currentIndex);

    // Обработчики для кнопок
    prevButton.addEventListener('click', function() {
        currentIndex = (currentIndex - 1 + blocks.length) % blocks.length;
        showBlock(currentIndex);
    });

    nextButton.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % blocks.length;
        showBlock(currentIndex);
    });

    // Функция для показа блока
    function showBlock(index) {
        blocks.forEach(block => block.classList.remove('active'));
        blocks[index].classList.add('active');
    }
});