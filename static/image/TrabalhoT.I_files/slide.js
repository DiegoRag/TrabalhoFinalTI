document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.getElementById('carousel');
    const carouselInner = document.querySelector('.carousel-inner');
    const totalItems = document.querySelectorAll('.carousel-item').length;
    let currentIndex = 0;

    // Selecione os botões dentro da div com a classe "containerBotao"
    const prevButton = document.querySelector('.containerBotao .prev');
    const nextButton = document.querySelector('.containerBotao .next');

    // Adicione ouvintes de evento para os botões
    prevButton.addEventListener('click', prevImage);
    nextButton.addEventListener('click', nextImage);

    // Função para exibir a próxima imagem no carrossel
    function nextImage() {
        if (currentIndex < totalItems - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        updateCarousel();
    }

    // Função para exibir a imagem anterior no carrossel
    function prevImage() {
        if (currentIndex > 0) {
            currentIndex--;
        } else {
            currentIndex = totalItems - 1;
        }
        updateCarousel();
    }

    // Atualiza a exibição do carrossel com base no índice atual
    function updateCarousel() {
        const newTransformValue = -currentIndex * 100 + '%';
        carouselInner.style.transform = 'translateX(' + newTransformValue + ')';
    }
});