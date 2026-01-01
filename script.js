// script.js
// Sicherstellen, dass DOM vorhanden ist (zusätzlich zu defer)
document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');

  if (!hamburger || !navMenu) {
    console.warn('Hamburger oder nav-menu wurde nicht gefunden. Elemente fehlen im DOM.');
    return;
  }

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
  });

  document.querySelectorAll('.nav-link').forEach(n =>
    n.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
    })
  );
});