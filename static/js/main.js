// ========================================
// ОСНОВНЫЕ ПЕРЕМЕННЫЕ И НАСТРОЙКИ
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    initializeAnimations();
    initializeNavigation();
    initializeSlider();
    initializeFAQ();
    initializeMaterials();
    initializeContactForm();
    initializeScrollAnimations();
    initializeModernEffects();
    initializeParticles();
    initializeInteractiveElements();
    initializeScrollNotifications();
    
    // Добавляем класс загрузки страницы
    setTimeout(() => {
        document.body.classList.add('page-loaded');
    }, 100);
});

// ========================================
// НАВИГАЦИЯ
// ========================================

// Простая функция для кнопки контактов
function toggleContactDropdown(event) {
    event.preventDefault();
    event.stopPropagation();
    const dropdown = document.getElementById('contactDropdown');
    if (dropdown) {
        dropdown.classList.toggle('show');
    }
}

// Закрытие выпадающего блока при клике вне него
document.addEventListener('click', function(e) {
    const dropdown = document.getElementById('contactDropdown');
    if (dropdown && !e.target.closest('.contact-dropdown-container')) {
        dropdown.classList.remove('show');
    }
});

function initializeNavigation() {
    // Инициализация красивой навигации
    const navigation = document.querySelector('.navigation');
    if (navigation) {
        
        // Обработчик скролла для эффекта навигации
        let lastScrollY = window.scrollY;
        
        window.addEventListener('scroll', () => {
            const currentScrollY = window.scrollY;
            
            // Изменяем прозрачность в зависимости от скролла
            if (currentScrollY > 50) {
                navigation.style.background = 'rgba(15, 23, 42, 0.98)';
                navigation.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.15)';
            } else {
                navigation.style.background = 'rgba(15, 23, 42, 0.95)';
                navigation.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
            }
            
            lastScrollY = currentScrollY;
        });
    }
    
    // Простая навигация без выпадающих блоков
    
    // Обработчики для красивой навигации
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Добавляем ripple эффект
            createRipple(e, this);
            
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId && targetId !== 'javascript:void(0)') {
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // Простая навигация без выпадающих блоков
    
    // ВРЕМЕННО ОТКЛЮЧАЕМ ПОСТОЯННУЮ ПРОВЕРКУ
    /*
    setInterval(() => {
        const nav = document.querySelector('.site-menu');
        if (nav) {
            const computedStyle = window.getComputedStyle(nav);
            if (computedStyle.position === 'fixed' || computedStyle.position === 'sticky') {
                nav.style.setProperty('position', 'static', 'important');
                nav.style.setProperty('top', 'auto', 'important');
                nav.style.setProperty('transform', 'none', 'important');
            }
        }
    }, 50);
    */
    
    // ПРИНУДИТЕЛЬНО обновляем стили при загрузке
    window.addEventListener('load', function() {
        const nav = document.querySelector('.site-menu');
        if (nav) {
            nav.style.setProperty('position', 'static', 'important');
            nav.style.setProperty('top', 'auto', 'important');
            nav.style.setProperty('transform', 'none', 'important');
            nav.style.setProperty('left', 'auto', 'important');
            nav.style.setProperty('right', 'auto', 'important');
            nav.style.setProperty('bottom', 'auto', 'important');
        }
    });
    
    // ВРЕМЕННО ОТКЛЮЧАЕМ ПРИНУДИТЕЛЬНОЕ ОБНОВЛЕНИЕ
    /*
    window.addEventListener('scroll', function() {
        const nav = document.querySelector('.site-menu');
        if (nav) {
            nav.style.setProperty('position', 'static', 'important');
            nav.style.setProperty('top', 'auto', 'important');
            nav.style.setProperty('transform', 'none', 'important');
        }
    });
    */
    
    // Скрытие/показ навигации при скролле - ОТКЛЮЧЕНО
    // let lastScrollTop = 0;
    // window.addEventListener('scroll', function() {
    //     const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    //     
    //     if (scrollTop > lastScrollTop && scrollTop > 100) {
    //         nav.style.transform = 'translateY(-100%)';
    //     } else {
    //         nav.style.transform = 'translateY(0)';
    //     }
    //     
    //     lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    // });
}

// ========================================
// АНИМАЦИИ
// ========================================

function initializeAnimations() {
    // Анимация логотипа
    const mainLogo = document.querySelector('.main-logo');
    if (mainLogo) {
        setTimeout(() => {
            mainLogo.classList.add('animated-entrance');
        }, 500);
    }
    
    // Анимация карточек при наведении
    const cards = document.querySelectorAll('.tech-card, .info-card, .advantage-card, .workflow-step, .stat-item');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Эффект параллакса для принтера
    const floatingPrinter = document.querySelector('.floating-printer');
    if (floatingPrinter) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            floatingPrinter.style.transform = `translateY(calc(-50% + ${rate}px))`;
        });
    }
}

// ========================================
// СКРОЛЛ АНИМАЦИИ
// ========================================

function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                
                // Анимация счетчиков
                if (entry.target.classList.contains('stat-number')) {
                    animateCounter(entry.target);
                }
            }
        });
    }, observerOptions);
    
    // Добавляем элементы для наблюдения
    const animatedElements = document.querySelectorAll('.tech-card, .info-card, .advantage-card, .workflow-step, .stat-item, .faq-item');
    animatedElements.forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
    
    // Анимация счетчиков
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => observer.observe(stat));
}

function animateCounter(element) {
    const target = element.textContent.replace(/[^0-9]/g, '');
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;
    
    const timer = setInterval(() => {
        current += step;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        
        const prefix = element.textContent.includes('>') ? '>' : '';
        element.textContent = prefix + Math.floor(current);
    }, 16);
}

// ========================================
// СЛАЙДЕР ПОРТФОЛИО
// ========================================

// Глобальные переменные для слайдера
let currentSlideIndex = 0;
let totalSlides = 0;

function initializeSlider() {
    
    const track = document.querySelector('.portfolio-track');
    const items = document.querySelectorAll('.portfolio-item');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const dots = document.querySelectorAll('.dot');
    
    
    if (!track || !items.length) {
        return;
    }
    
    totalSlides = items.length;
    currentSlideIndex = 0;
    
    // Инициализация
    updateSliderManual();
    
    
    // Принудительно обновляем слайдер через 500ms для загрузки контента
    setTimeout(() => {
        const newItems = document.querySelectorAll('.portfolio-item');
        if (newItems.length !== totalSlides) {
            totalSlides = newItems.length;
            updateSliderManual();
        }
    }, 500);
    
    // Поддержка свайпов на мобильных
    let startX = 0;
    let endX = 0;
    
    if (track) {
        track.addEventListener('touchstart', e => {
            startX = e.touches[0].clientX;
        }, { passive: true });
        
        track.addEventListener('touchend', e => {
            endX = e.changedTouches[0].clientX;
            handleSwipe();
        }, { passive: true });
    }
    
    function handleSwipe() {
        const threshold = 50;
        const diff = startX - endX;
        
        if (Math.abs(diff) > threshold) {
            if (diff > 0) {
                nextSlideManual();
            } else {
                prevSlideManual();
            }
        }
    }
}

// ========================================
// FAQ АККОРДЕОН
// ========================================

function initializeFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        const icon = item.querySelector('.faq-icon');
        
        if (question && answer) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                
                // Закрываем все другие элементы
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                        const otherAnswer = otherItem.querySelector('.faq-answer');
                        if (otherAnswer) {
                            otherAnswer.style.maxHeight = '0';
                        }
                    }
                });
                
                // Переключаем текущий элемент
                if (isActive) {
                    item.classList.remove('active');
                    answer.style.maxHeight = '0';
                } else {
                    item.classList.add('active');
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                }
            });
        }
    });
}

// ========================================
// МАТЕРИАЛЫ ТЕХНОЛОГИЙ
// ========================================

function initializeMaterials() {
    const materialsBtns = document.querySelectorAll('.materials-btn');
    
    // Предустановленные материалы для каждой технологии
    const materialsData = {
        'FDM': [
            'PLA - биоразлагаемый пластик',
            'ABS - прочный инженерный пластик',
            'PETG - химически стойкий материал',
            'TPU - гибкий эластичный материал',
            'Wood Fill - пластик с древесными волокнами',
            'Carbon Fiber - углеволоконный композит',
            'Metal Fill - пластик с металлическими частицами'
        ],
        'SLA': [
            'Standard Resin - базовая фотополимерная смола',
            'Tough Resin - прочная инженерная смола',
            'Flexible Resin - гибкая эластичная смола',
            'Castable Resin - выжигаемая смола для литья',
            'Dental Resin - биосовместимая смола',
            'Clear Resin - прозрачная оптическая смола',
            'High Temp Resin - термостойкая смола'
        ],
        'SLM': [
            'Stainless Steel 316L - нержавеющая сталь',
            'Titanium Ti6Al4V - титановый сплав',
            'Aluminum AlSi10Mg - алюминиевый сплав',
            'Inconel 718 - жаропрочный сплав',
            'Maraging Steel - мартенситно-стареющая сталь',
            'Cobalt Chrome - кобальт-хромовый сплав',
            'Tool Steel - инструментальная сталь'
        ],
        // Добавляем материалы для всех возможных вариантов
        '1': [
            'PLA - биоразлагаемый пластик',
            'ABS - прочный инженерный пластик',
            'PETG - химически стойкий материал'
        ],
        '2': [
            'Standard Resin - базовая фотополимерная смола',
            'Tough Resin - прочная инженерная смола',
            'Clear Resin - прозрачная оптическая смола'
        ],
        '3': [
            'Stainless Steel 316L - нержавеющая сталь',
            'Titanium Ti6Al4V - титановый сплав',
            'Aluminum AlSi10Mg - алюминиевый сплав'
        ]
    };
    
    materialsBtns.forEach(btn => {
        // Заранее создаем tooltip для материалов
        const tech = btn.dataset.tech;
        if (tech && materialsData[tech]) {
            const tooltip = document.createElement('div');
            tooltip.className = 'materials-tooltip';
            tooltip.innerHTML = `
                <div class="tooltip-header">Материалы ${tech}</div>
                <div class="tooltip-content">
                    ${materialsData[tech].map(material => 
                        `<div class="tooltip-item">${material}</div>`
                    ).join('')}
                </div>
            `;
            
            btn.parentNode.style.position = 'relative';
            btn.parentNode.appendChild(tooltip);
            
            // События наведения
            btn.addEventListener('mouseenter', () => {
                tooltip.classList.add('show');
            });
            
            btn.addEventListener('mouseleave', () => {
                setTimeout(() => {
                    if (!tooltip.matches(':hover')) {
                        tooltip.classList.remove('show');
                    }
                }, 100);
            });
            
            tooltip.addEventListener('mouseleave', () => {
                tooltip.classList.remove('show');
            });
        }
        
        // Клик события (оставляем для мобильных)
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const tooltip = this.parentNode.querySelector('.materials-tooltip');
            if (tooltip) {
                tooltip.classList.toggle('show');
            }
        });
    });
    
    // Закрытие тултипов при клике вне них
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.materials-btn') && !e.target.closest('.materials-tooltip')) {
            document.querySelectorAll('.materials-tooltip').forEach(tooltip => {
                tooltip.classList.remove('show');
            });
        }
    });
}

// ========================================
// ФОРМА ЗАЯВКИ
// ========================================

function initializeContactForm() {
    const form = document.getElementById('orderForm');
    const fileInput = document.getElementById('fileInput');
    const fileLabel = document.querySelector('.file-label span');
    
    
    // Обработка выбора файла
    if (fileInput && fileLabel) {
        fileInput.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                const fileName = this.files[0].name;
                fileLabel.textContent = `Выбран: ${fileName}`;
                fileLabel.style.color = '#0ea5e9';
            } else {
                fileLabel.textContent = 'Прикрепить файл';
                fileLabel.style.color = '';
            }
        });
    }
    
    // Обработка отправки формы
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const formData = new FormData(this);
            const submitBtn = this.querySelector('.submit-btn');
            const originalText = submitBtn.innerHTML;
            
            // Показываем состояние загрузки
            submitBtn.innerHTML = '<i class=\"fas fa-spinner fa-spin\"></i> ОТПРАВКА...';
            submitBtn.disabled = true;
            
            // Получаем CSRF токен
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
            
            // Отправляем данные
            fetch('/submit-order/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken ? csrfToken.value : ''
                }
            })
            .then(response => {
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    showNotification('Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.', 'success');
                    form.reset();
                    if (fileLabel) {
                        fileLabel.textContent = 'Прикрепить файл';
                        fileLabel.style.color = '';
                    }
                } else {
                    showNotification(data.error || 'Произошла ошибка при отправке заявки', 'error');
                }
            })
            .catch(error => {
                console.error('Ошибка при отправке:', error);
                showNotification('Произошла ошибка при отправке заявки', 'error');
            })
            .finally(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }
}

// ========================================
// УВЕДОМЛЕНИЯ
// ========================================

function showNotification(message, type = 'info') {
    // Создаем элемент уведомления
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class=\"notification-content\">
            <i class=\"fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}\"></i>
            <span>${message}</span>
        </div>
        <button class=\"notification-close\">&times;</button>
    `;
    
    // Добавляем стили если их еще нет
    if (!document.querySelector('#notification-styles')) {
        const styles = document.createElement('style');
        styles.id = 'notification-styles';
        styles.textContent = `
            .notification {
                position: fixed;
                top: 100px;
                right: 20px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                padding: 20px;
                max-width: 400px;
                z-index: 10001;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 16px;
                transform: translateX(100%);
                transition: transform 0.3s ease-out;
            }
            .notification-success { border-left: 4px solid #10b981; }
            .notification-error { border-left: 4px solid #ef4444; }
            .notification-content {
                display: flex;
                align-items: center;
                gap: 12px;
                flex: 1;
            }
            .notification-success .fa-check-circle { color: #10b981; }
            .notification-error .fa-exclamation-circle { color: #ef4444; }
            .notification-close {
                background: none;
                border: none;
                font-size: 20px;
                cursor: pointer;
                color: #9ca3af;
                padding: 0;
                width: 24px;
                height: 24px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .notification-close:hover { color: #374151; }
        `;
        document.head.appendChild(styles);
    }
    
    // Добавляем в DOM
    document.body.appendChild(notification);
    
    // Анимация появления
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Обработчик закрытия
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    });
    
    // Автоматическое удаление через 5 секунд
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
}

// ========================================
// УТИЛИТЫ
// ========================================

function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Debounce функция для оптимизации событий
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Оптимизированный обработчик скролла
const optimizedScrollHandler = debounce(() => {
    // Здесь можно добавить дополнительные обработчики скролла
}, 16);

window.addEventListener('scroll', optimizedScrollHandler);

// ========================================
// МОБИЛЬНОЕ МЕНЮ
// ========================================

function initializeMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const menu = document.querySelector('.nav-menu');
    
    if (toggle && menu) {
        toggle.addEventListener('click', () => {
            menu.classList.toggle('active');
            toggle.classList.toggle('active');
        });
    }
}

// Инициализация мобильного меню
document.addEventListener('DOMContentLoaded', initializeMobileMenu);

// ========================================
// ПРОИЗВОДИТЕЛЬНОСТЬ
// ========================================

// Preload критически важных изображений
function preloadImages() {
    const criticalImages = [
        '/media/services/printer.jpg',
        '/media/services/printer.jpg',
        '/media/services/3d_printing.jpg',
        '/media/services/3d_printing.jpg',
        '/media/services/3d_printing.jpg'
    ];
    
    criticalImages.forEach(src => {
        const img = new Image();
        img.src = src;
    });
}

// Запускаем preload после загрузки страницы
window.addEventListener('load', preloadImages);

// ========================================
// СОВРЕМЕННЫЕ ИНТЕРАКТИВНЫЕ ЭФФЕКТЫ
// ========================================

function initializeModernEffects() {
    // Эффект параллакса для фона
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.parallax-bg');
        
        parallaxElements.forEach(element => {
            const speed = element.dataset.speed || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });
    
    // Интерактивные карточки с 3D эффектом
    const cards = document.querySelectorAll('.advantage-card, .tech-card, .workflow-step');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', handleCardMouseMove);
        card.addEventListener('mouseleave', handleCardMouseLeave);
    });
}

function handleCardMouseMove(e) {
    const card = e.currentTarget;
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    const rotateX = (y - centerY) / 10;
    const rotateY = (centerX - x) / 10;
    
    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
    card.style.boxShadow = '0 20px 40px rgba(0,0,0,0.2)';
}

function handleCardMouseLeave(e) {
    const card = e.currentTarget;
    card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
    card.style.boxShadow = '';
}

// Частицы на фоне
function initializeParticles() {
    const heroSection = document.querySelector('.hero-section');
    if (!heroSection) return;
    
    const particlesContainer = document.createElement('div');
    particlesContainer.className = 'particles-container';
    heroSection.appendChild(particlesContainer);
    
    // Создаем частицы
    for (let i = 0; i < 50; i++) {
        createParticle(particlesContainer);
    }
}

function createParticle(container) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    
    // Случайные параметры
    const size = Math.random() * 4 + 2;
    const x = Math.random() * 100;
    const animationDuration = Math.random() * 20 + 10;
    const opacity = Math.random() * 0.5 + 0.1;
    
    particle.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        background: linear-gradient(45deg, #7dd3fc, #0ea5e9);
        border-radius: 50%;
        left: ${x}%;
        opacity: ${opacity};
        animation: floatUp ${animationDuration}s infinite linear;
        pointer-events: none;
    `;
    
    container.appendChild(particle);
    
    // Удаляем частицу после анимации
    setTimeout(() => {
        if (particle.parentNode) {
            particle.parentNode.removeChild(particle);
        }
    }, animationDuration * 1000);
}

// Интерактивные элементы
function initializeInteractiveElements() {
    // Магнитный эффект для кнопок
    const buttons = document.querySelectorAll('.cta-button, .submit-btn');
    
    buttons.forEach(button => {
        button.addEventListener('mousemove', (e) => {
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            button.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px) scale(1.05)`;
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.transform = 'translate(0px, 0px) scale(1)';
        });
    });
    
    // Волновой эффект при клике
    buttons.forEach(button => {
        button.addEventListener('click', createRippleEffect);
    });
}

function createRippleEffect(e) {
    const button = e.currentTarget;
    const rect = button.getBoundingClientRect();
    const ripple = document.createElement('span');
    const size = Math.max(rect.width, rect.height);
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;
    
    ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        left: ${x}px;
        top: ${y}px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 50%;
        transform: scale(0);
        animation: ripple 0.6s ease-out;
        pointer-events: none;
    `;
    
    button.style.position = 'relative';
    button.style.overflow = 'hidden';
    button.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
}

// Плавное появление элементов при скролле
function initializeScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal-on-scroll');
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    revealElements.forEach(element => {
        revealObserver.observe(element);
    });
}

// Добавляем CSS для новых эффектов
function addModernCSS() {
    const style = document.createElement('style');
    style.textContent = `
        .particles-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            pointer-events: none;
            z-index: 1;
        }
        
        @keyframes floatUp {
            0% {
                transform: translateY(100vh) rotate(0deg);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100px) rotate(360deg);
                opacity: 0;
            }
        }
        
        @keyframes ripple {
            to {
                transform: scale(2);
                opacity: 0;
            }
        }
        
        .reveal-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .reveal-on-scroll.revealed {
            opacity: 1;
            transform: translateY(0);
        }
        
        .advantage-card,
        .tech-card,
        .workflow-step {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .floating-printer {
            filter: drop-shadow(0 10px 20px rgba(0,0,0,0.3));
        }
        
        @media (prefers-reduced-motion: reduce) {
            .particles-container {
                display: none;
            }
            
            .advantage-card,
            .tech-card,
            .workflow-step {
                transform: none !important;
            }
        }
    `;
    
    document.head.appendChild(style);
}

// Инициализируем современные эффекты
document.addEventListener('DOMContentLoaded', () => {
    addModernCSS();
    initializeScrollReveal();
});

// ========================================
// ACCESSIBILITY
// ========================================

// Улучшение доступности клавиатуры
document.addEventListener('keydown', function(e) {
    // ESC для закрытия модальных окон
    if (e.key === 'Escape') {
        const modal = document.getElementById('contactModal');
        if (modal && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
        
        // Закрытие всех дропдаунов
        document.querySelectorAll('.materials-dropdown.active').forEach(dd => {
            dd.classList.remove('active');
        });
        document.querySelectorAll('.materials-btn.active').forEach(btn => {
            btn.classList.remove('active');
        });
    }
});

// Focus trap для модального окна
function trapFocus(element) {
    const focusableElements = element.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex=\"-1\"])'
    );
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    element.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            if (e.shiftKey) {
                if (document.activeElement === firstElement) {
                    lastElement.focus();
                    e.preventDefault();
                }
            } else {
                if (document.activeElement === lastElement) {
                    firstElement.focus();
                    e.preventDefault();
                }
            }
        }
    });
}

// Применяем focus trap к модальному окну
const modal = document.getElementById('contactModal');
if (modal) {
    trapFocus(modal);
}

// ========================================
// УВЕДОМЛЕНИЯ О СКРОЛЛЕ
// ========================================

function initializeScrollNotifications() {
    const notification = document.getElementById('scrollNotification');
    const closeBtn = notification?.querySelector('.close-notification');
    let hasShown = false;
    let scrollTimeout;
    
    // Показываем уведомление после небольшой задержки
    setTimeout(() => {
        if (!hasShown && window.pageYOffset < 100) {
            showScrollNotification();
        }
    }, 3000);
    
    function showScrollNotification() {
        if (notification && !hasShown) {
            notification.classList.add('show');
            hasShown = true;
            
            // Автоматически скрываем через 5 секунд
            setTimeout(hideScrollNotification, 5000);
        }
    }
    
    function hideScrollNotification() {
        if (notification) {
            notification.classList.remove('show');
        }
    }
    
    // Закрытие по кнопке
    if (closeBtn) {
        closeBtn.addEventListener('click', hideScrollNotification);
    }
    
    // Скрываем при скролле
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 200) {
            hideScrollNotification();
        }
    });
    
    // Показываем другие уведомления при достижении определенных секций
    const sections = document.querySelectorAll('section');
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Можно добавить специфические уведомления для каждой секции
                triggerSectionNotification(entry.target);
            }
        });
    }, {
        threshold: 0.3
    });
    
    sections.forEach(section => {
        sectionObserver.observe(section);
    });
}

function triggerSectionNotification(section) {
    // Здесь можно добавить специфические уведомления для разных секций
    const sectionId = section.id;
    
    if (sectionId === 'technologies' && !localStorage.getItem('techNotificationShown')) {
        showCustomNotification('Нажмите на "Материал" чтобы посмотреть доступные материалы!', 'info');
        localStorage.setItem('techNotificationShown', 'true');
    }
}

function showCustomNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `custom-notification ${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-${type === 'info' ? 'info-circle' : 'check-circle'}"></i>
            <span>${message}</span>
        </div>
        <button class="close-notification">&times;</button>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    // Закрытие
    const closeBtn = notification.querySelector('.close-notification');
    closeBtn.addEventListener('click', () => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    });
    
    // Автоматическое удаление
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.classList.remove('show');
            setTimeout(() => {
                notification.remove();
            }, 300);
        }
    }, 4000);
}

// ========================================
// ПРОИЗВОДИТЕЛЬНОСТЬ И ОПТИМИЗАЦИЯ
// ========================================

// Ленивая загрузка изображений
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Отложенная загрузка некритичных ресурсов
function loadNonCriticalResources() {
    // Загружаем шрифты асинхронно
    if ('fonts' in document) {
        document.fonts.load('400 16px Inter').then(() => {
            document.body.classList.add('fonts-loaded');
        });
    }
}

// Оптимизация скролла
let ticking = false;

function optimizedScrollHandler() {
    if (!ticking) {
        requestAnimationFrame(() => {
            updateParallaxElements();
            ticking = false;
        });
        ticking = true;
    }
}

function updateParallaxElements() {
    const scrolled = window.pageYOffset;
    const floatingPrinter = document.querySelector('.floating-printer');
    
    if (floatingPrinter && window.innerWidth > 768) {
        const rate = scrolled * -0.3;
        floatingPrinter.style.transform = `translateY(calc(-50% + ${rate}px))`;
    }
}

// Запуск оптимизаций
window.addEventListener('load', () => {
    initializeLazyLoading();
    loadNonCriticalResources();
});

window.addEventListener('scroll', optimizedScrollHandler, { passive: true });

// Обработка размера окна
window.addEventListener('resize', debounce(() => {
    updateParallaxElements();
}, 250));

// ========================================
// RIPPLE ЭФФЕКТ ДЛЯ КНОПОК НАВИГАЦИИ
// ========================================

// Функция для создания ripple эффекта
function createRipple(event, element) {
    const circle = document.createElement('span');
    const diameter = Math.max(element.clientWidth, element.clientHeight);
    const radius = diameter / 2;
    
    const rect = element.getBoundingClientRect();
    circle.style.width = circle.style.height = `${diameter}px`;
    circle.style.left = `${event.clientX - rect.left - radius}px`;
    circle.style.top = `${event.clientY - rect.top - radius}px`;
    circle.classList.add('nav-ripple');
    
    const ripple = element.querySelector('.nav-ripple');
    if (ripple) {
        ripple.remove();
    }
    
    element.appendChild(circle);
    
    // Удаляем элемент после анимации
    setTimeout(() => {
        circle.remove();
    }, 600);
}

// ========================================
// ДОПОЛНИТЕЛЬНЫЕ АНИМАЦИИ ИЗ РЕЗЕРВНОЙ КОПИИ
// ========================================

function addBackgroundAnimations() {
    const body = document.body;
    
    // Анимация фонового градиента
    if (!body.classList.contains('bg-animated')) {
        body.classList.add('bg-animated');
    }
    
    // Добавляем плавающие частицы
    createFloatingParticles();
}

function activateHoverEffects() {
    // Эффекты для кнопок
    const buttons = document.querySelectorAll('.nav-link, .cta-button, .btn');
    buttons.forEach(button => {
        if (!button.classList.contains('hover-enhanced')) {
            button.classList.add('hover-enhanced');
            
            button.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px) scale(1.05)';
                this.style.boxShadow = '0 10px 30px rgba(65, 105, 225, 0.4)';
            });
            
            button.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
                this.style.boxShadow = '0 2px 8px rgba(65, 105, 225, 0.2)';
            });
        }
    });
    
}

function startParticleSystem() {
    // Создаем систему частиц для hero секции
    const heroSection = document.querySelector('.hero');
    if (heroSection && !heroSection.querySelector('.particle-system')) {
        const particleContainer = document.createElement('div');
        particleContainer.className = 'particle-system';
        particleContainer.style.cssText = `
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        `;
        
        // Создаем 20 частиц
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.cssText = `
                position: absolute;
                width: 4px;
                height: 4px;
                background: rgba(65, 105, 225, 0.6);
                border-radius: 50%;
                animation: float-particle ${5 + Math.random() * 10}s infinite linear;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                opacity: ${0.3 + Math.random() * 0.7};
            `;
            particleContainer.appendChild(particle);
        }
        
        heroSection.appendChild(particleContainer);
    }
}

function createFloatingParticles() {
    // Создаем CSS для анимации частиц, если его еще нет
    if (!document.querySelector('#particle-animations')) {
        const style = document.createElement('style');
        style.id = 'particle-animations';
        style.textContent = `
            @keyframes float-particle {
                0% {
                    transform: translateY(100vh) rotate(0deg);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                90% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(-100px) rotate(360deg);
                    opacity: 0;
                }
            }
            
            .bg-animated {
                background: linear-gradient(-45deg, #1a1a1a, #2d2d2d, #1a1a1a, #333) !important;
                background-size: 400% 400% !important;
                animation: gradient-shift 15s ease infinite !important;
            }
            
            @keyframes gradient-shift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            .hover-enhanced {
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
        `;
        document.head.appendChild(style);
    }
}

// ========================================
// ГЛОБАЛЬНЫЕ ФУНКЦИИ ДЛЯ СЛАЙДЕРА
// ========================================

// Функции, которые вызываются из HTML
function nextSlideManual() {
    if (totalSlides === 0) return;
    
    currentSlideIndex = (currentSlideIndex + 1) % totalSlides;
    updateSliderManual();
}

function prevSlideManual() {
    if (totalSlides === 0) return;
    
    currentSlideIndex = currentSlideIndex === 0 ? totalSlides - 1 : currentSlideIndex - 1;
    updateSliderManual();
}

function goToSlide(index) {
    if (totalSlides === 0) return;
    
    currentSlideIndex = index;
    updateSliderManual();
}

function updateSliderManual() {
    const track = document.querySelector('.portfolio-track');
    const items = document.querySelectorAll('.portfolio-item');
    const dots = document.querySelectorAll('.dot');
    
    if (!track || !items.length) return;
    
    // Обновляем позицию слайдера
    const translateX = -currentSlideIndex * 100;
    track.style.transform = `translateX(${translateX}%)`;
    
    // Обновляем точки
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentSlideIndex);
    });
    
    // Обновляем видимость кнопок
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if (prevBtn) {
        prevBtn.style.opacity = currentSlideIndex === 0 ? '0.5' : '1';
    }
    if (nextBtn) {
        nextBtn.style.opacity = currentSlideIndex === totalSlides - 1 ? '0.5' : '1';
    }
}

// ========================================
// ОТКЛЮЧЕНЫ HOVER СТИЛИ ДЛЯ СОЦИАЛЬНЫХ ИКОНОК
// ========================================

// ОТКЛЮЧЕНО: Принудительное применение hover стилей для социальных иконок в футере
/*
document.addEventListener('DOMContentLoaded', function() {
    
    const socialLinks = document.querySelectorAll('.footer .social-icons-row .social-link');
    
    socialLinks.forEach((link, index) => {
        
        // Добавляем обработчики событий для принудительного изменения стилей
        link.addEventListener('mouseenter', function() {
            
            // Проверяем оба варианта классов: с -link и без
            const platform = this.classList.contains('vk-link') || this.classList.contains('vk') ? 'vk' : 
                           this.classList.contains('youtube-link') || this.classList.contains('youtube') ? 'youtube' :
                           this.classList.contains('telegram-link') || this.classList.contains('telegram') ? 'telegram' :
                           this.classList.contains('whatsapp-link') || this.classList.contains('whatsapp') ? 'whatsapp' : '';
            
            let color = '';
            switch(platform) {
                case 'vk':
                    color = '#4680c2';
                    break;
                case 'youtube':
                    color = '#ff0000';
                    break;
                case 'telegram':
                    color = '#0088cc';
                    break;
                case 'whatsapp':
                    color = '#25d366';
                    break;
            }
            
            if (color) {
                this.style.setProperty('background-color', color, 'important');
                this.style.setProperty('border-color', color, 'important');
                this.style.setProperty('transform', 'translateY(-4px)', 'important');
                this.style.setProperty('box-shadow', '0 8px 25px rgba(0,0,0,0.15)', 'important');
            }
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.removeProperty('background-color');
            this.style.removeProperty('border-color');
            this.style.removeProperty('transform');
            this.style.removeProperty('box-shadow');
        });
    });
    
    // Дополнительная проверка через 1 секунду для динамически загруженного контента
    setTimeout(() => {
        const newSocialLinks = document.querySelectorAll('.footer .social-icons-row .social-link');
        if (newSocialLinks.length > socialLinks.length) {
            newSocialLinks.forEach(link => {
                if (!link.dataset.hoverInitialized) {
                    link.dataset.hoverInitialized = 'true';
                    
                    link.addEventListener('mouseenter', function() {
                        // Проверяем оба варианта классов: с -link и без
                        const platform = this.classList.contains('vk-link') || this.classList.contains('vk') ? 'vk' : 
                                       this.classList.contains('youtube-link') || this.classList.contains('youtube') ? 'youtube' :
                                       this.classList.contains('telegram-link') || this.classList.contains('telegram') ? 'telegram' :
                                       this.classList.contains('whatsapp-link') || this.classList.contains('whatsapp') ? 'whatsapp' : '';
                        
                        let color = '';
                        switch(platform) {
                            case 'vk': color = '#4680c2'; break;
                            case 'youtube': color = '#ff0000'; break;
                            case 'telegram': color = '#0088cc'; break;
                            case 'whatsapp': color = '#25d366'; break;
                        }
                        
                        if (color) {
                            this.style.setProperty('background-color', color, 'important');
                            this.style.setProperty('border-color', color, 'important');
                            this.style.setProperty('transform', 'translateY(-4px)', 'important');
                            this.style.setProperty('box-shadow', '0 8px 25px rgba(0,0,0,0.15)', 'important');
                        }
                    });
                    
                    link.addEventListener('mouseleave', function() {
                        this.style.removeProperty('background-color');
                        this.style.removeProperty('border-color');
                        this.style.removeProperty('transform');
                        this.style.removeProperty('box-shadow');
                    });
                }
            });
        }
    }, 1000);
});
*/
