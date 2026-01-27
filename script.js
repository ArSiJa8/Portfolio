// script.js
// DOM ready (defer + this listener = safe)
document.addEventListener('DOMContentLoaded', () => {
  // ---------- Hamburger / Nav ----------
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      const isActive = hamburger.classList.toggle('active');
      navMenu.classList.toggle('active');
      hamburger.setAttribute('aria-expanded', isActive ? 'true' : 'false');
      // Prevent scrolling when menu is open
      document.body.style.overflow = isActive ? "hidden" : "auto";
    });

    navLinks.forEach(n =>
      n.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = "auto";
      })
    );
  } else {
    console.warn('Hamburger oder nav-menu nicht gefunden.');
  }

  // ---------- Scroll Reveal ----------s
  const revealSelectors = [
    '.center-screen .card',
    'section',
    '.container-white',
    '.projects-grid > *'
  ].join(',');

  const elements = Array.from(document.querySelectorAll(revealSelectors))
    .filter(Boolean);

  if (elements.length === 0) return;

  elements.forEach((el, idx) => {
    // don't overwrite explicit inline transition-delay if present
    if (!el.style.transitionDelay && !el.dataset.delay) {
      const delayMs = (idx % 10) * 60; // 0,60,120,...,540ms
      el.style.transitionDelay = `${delayMs}ms`;
    } else if (el.dataset.delay && !el.style.transitionDelay) {
      el.style.transitionDelay = el.dataset.delay;
    }
    el.classList.add('reveal');
  });

  // IntersectionObserver options
  const ioOptions = {
    root: null,
    rootMargin: '0px 0px -8% 0px', // trigger a bit before element fully in view
    threshold: 0.12
  };

  function revealCallback(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        target.classList.add('in-view');
      
        observer.unobserve(target);
      }
    });
  }

  // Use IntersectionObserver when available
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(revealCallback, ioOptions);
    elements.forEach(el => observer.observe(el));
  } else {
    // Fallback: simple on-scroll check
    const onScroll = () => {
      const viewportHeight = window.innerHeight;
      elements.forEach(el => {
        if (el.classList.contains('in-view')) return;
        const rect = el.getBoundingClientRect();
        if (rect.top < viewportHeight * 0.92 && rect.bottom > 0) {
          el.classList.add('in-view');
        }
      });
      // if all revealed, remove listener
      if (elements.every(e => e.classList.contains('in-view'))) {
        window.removeEventListener('scroll', onScroll);
        window.removeEventListener('resize', onScroll);
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    // run once
    onScroll();
  }
});