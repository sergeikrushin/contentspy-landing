// ============================================
// ContentSpy Landing — Interactions
// ============================================

// Scroll animations (IntersectionObserver)
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));

    // Nav scroll effect
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => {
        nav.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });

    // FAQ accordion
    document.querySelectorAll('.faq-item').forEach(item => {
        item.querySelector('.faq-q').addEventListener('click', () => {
            const wasActive = item.classList.contains('active');
            // Close all
            document.querySelectorAll('.faq-item.active').forEach(i => i.classList.remove('active'));
            // Toggle current
            if (!wasActive) item.classList.add('active');
        });
    });

    // Hamburger menu
    const hamburger = document.getElementById('navHamburger');
    const mobileNav = document.getElementById('navMobile');
    if (hamburger && mobileNav) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            mobileNav.classList.toggle('active');
        });
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                mobileNav.classList.remove('active');
            });
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Parallax on hero screenshot (subtle tilt on mouse move)
    const heroVisual = document.querySelector('.hero-visual');
    if (heroVisual) {
        const wrap = heroVisual.querySelector('.hero-screenshot-wrap');
        document.addEventListener('mousemove', (e) => {
            if (!wrap) return;
            const rect = heroVisual.getBoundingClientRect();
            if (rect.bottom < 0 || rect.top > window.innerHeight) return;
            const cx = (e.clientX / window.innerWidth - 0.5) * 2;
            const cy = (e.clientY / window.innerHeight - 0.5) * 2;
            wrap.style.transform = `rotateX(${2 - cy * 3}deg) rotateY(${cx * 3}deg)`;
        }, { passive: true });
    }

    // Parallax floating screenshots on scroll
    const floaters = document.querySelectorAll('.floater');
    if (floaters.length) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            floaters.forEach((f, i) => {
                const speed = i === 0 ? 0.06 : -0.04;
                f.style.transform = `translateY(${scrollY * speed}px)`;
            });
        }, { passive: true });
    }

    // Feature screenshots — tilt on hover
    document.querySelectorAll('.feature-screenshot-wrap').forEach(wrap => {
        wrap.addEventListener('mousemove', (e) => {
            const rect = wrap.getBoundingClientRect();
            const cx = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
            const cy = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
            wrap.style.transform = `translateY(-6px) scale(1.01) rotateY(${cx * 4}deg) rotateX(${-cy * 4}deg)`;
        }, { passive: true });
        wrap.addEventListener('mouseleave', () => {
            wrap.style.transform = '';
        });
    });
});

// === COUNTDOWN TIMER ===
function updateCountdown() {
    const deadline = new Date('2026-03-27T23:59:59');
    const now = new Date();
    const diff = deadline - now;
    if (diff <= 0) {
        const el = document.getElementById('pricingCountdown');
        if (el) el.textContent = 'Offer expired';
        return;
    }
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const el = document.getElementById('pricingCountdown');
    if (el) el.textContent = `${days}d ${String(hours).padStart(2,'0')}h ${String(mins).padStart(2,'0')}m`;
}
updateCountdown();
setInterval(updateCountdown, 30000);

// === STICKY MOBILE CTA ===
const stickyBar = document.getElementById('stickyMobileCta');
if (stickyBar) {
    let shown = false;
    window.addEventListener('scroll', () => {
        if (window.scrollY > 400 && !shown) {
            stickyBar.classList.add('visible');
            shown = true;
        }
    }, { passive: true });
}

// === WINDOWS WAITLIST FORM ===
const waitlistForm = document.getElementById('windowsWaitlist');
if (waitlistForm) {
    waitlistForm.addEventListener('submit', function(e) {
        e.preventDefault();
        waitlistForm.style.display = 'none';
        const success = document.getElementById('waitlistSuccess');
        if (success) success.style.display = 'block';
    });
}
