// ДИНАМИЧЕСКАЯ АДАПТИВНОСТЬ ТОЛЬКО ДЛЯ HERO-SECTION
// Этот скрипт обеспечивает адаптивность элементов только в первом блоке

(function() {
    'use strict';
    
    // Функция для обновления позиционирования социальных иконок в hero-section
    function updateHeroSocialLinks() {
        const heroSection = document.querySelector('.hero-section');
        if (!heroSection) return;
        
        const socialLinks = heroSection.querySelectorAll('.social-links');
        const screenWidth = window.innerWidth;
        
        socialLinks.forEach(links => {
            if (screenWidth <= 768) {
                // Мобильные устройства - центрируем
                links.style.position = 'static';
                links.style.left = 'auto';
                links.style.right = 'auto';
                links.style.top = 'auto';
                links.style.margin = '20px auto';
                links.style.justifyContent = 'center';
                links.style.width = '100%';
            } else if (screenWidth <= 1000) {
                // Планшеты - позиционируем справа
                links.style.position = 'absolute';
                links.style.right = '10px';
                links.style.top = '10px';
                links.style.left = 'auto';
                links.style.margin = '0';
                links.style.justifyContent = 'flex-start';
                links.style.width = 'auto';
            } else if (screenWidth <= 1200) {
                // Средние экраны
                links.style.position = 'absolute';
                links.style.right = '15px';
                links.style.top = '15px';
                links.style.left = 'auto';
                links.style.margin = '0';
                links.style.justifyContent = 'flex-start';
                links.style.width = 'auto';
            } else {
                // Большие экраны
                links.style.position = 'absolute';
                links.style.right = '20px';
                links.style.top = '20px';
                links.style.left = 'auto';
                links.style.margin = '0';
                links.style.justifyContent = 'flex-start';
                links.style.width = 'auto';
            }
        });
    }
    
    // Функция для обновления размеров изображения pervblok в hero-section
    function updateHeroPervblokImage() {
        const heroSection = document.querySelector('.hero-section');
        if (!heroSection) return;
        
        const pervblokImages = heroSection.querySelectorAll('img[src*="pervblok"]');
        const screenWidth = window.innerWidth;
        const screenHeight = window.innerHeight;
        
        let maxHeight;
        
        if (screenWidth <= 480) {
            maxHeight = screenHeight * 0.2; // 20% от высоты экрана
        } else if (screenWidth <= 600) {
            maxHeight = screenHeight * 0.25; // 25% от высоты экрана
        } else if (screenWidth <= 800) {
            maxHeight = screenHeight * 0.3; // 30% от высоты экрана
        } else if (screenWidth <= 1000) {
            maxHeight = screenHeight * 0.35; // 35% от высоты экрана
        } else if (screenWidth <= 1200) {
            maxHeight = screenHeight * 0.4; // 40% от высоты экрана
        } else if (screenWidth <= 1400) {
            maxHeight = screenHeight * 0.45; // 45% от высоты экрана
        } else {
            maxHeight = screenHeight * 0.5; // 50% от высоты экрана
        }
        
        pervblokImages.forEach(img => {
            img.style.width = '100%';
            img.style.height = 'auto';
            img.style.maxWidth = '100%';
            img.style.maxHeight = maxHeight + 'px';
            img.style.objectFit = 'contain';
        });
    }
    
    // Функция для обновления размеров кнопок социальных сетей в hero-section
    function updateHeroSocialButtons() {
        const heroSection = document.querySelector('.hero-section');
        if (!heroSection) return;
        
        const socialButtons = heroSection.querySelectorAll('.social-links .social-btn');
        const screenWidth = window.innerWidth;
        
        let buttonSize;
        
        if (screenWidth <= 480) {
            buttonSize = '40px';
        } else if (screenWidth <= 768) {
            buttonSize = '45px';
        } else {
            buttonSize = '50px';
        }
        
        socialButtons.forEach(btn => {
            btn.style.width = buttonSize;
            btn.style.height = buttonSize;
            btn.style.borderRadius = '50%';
            btn.style.display = 'flex';
            btn.style.alignItems = 'center';
            btn.style.justifyContent = 'center';
        });
    }
    
    // Основная функция обновления для hero-section
    function updateHeroResponsiveElements() {
        updateHeroSocialLinks();
        updateHeroPervblokImage();
        updateHeroSocialButtons();
    }
    
    // Запуск при загрузке страницы
    document.addEventListener('DOMContentLoaded', function() {
        updateHeroResponsiveElements();
    });
    
    // Обновление при изменении размера окна
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(updateHeroResponsiveElements, 100);
    });
    
    // Дополнительная проверка каждые 500ms для надежности (только для hero-section)
    setInterval(function() {
        const heroSection = document.querySelector('.hero-section');
        if (heroSection) {
            updateHeroResponsiveElements();
        }
    }, 500);
    
})();




