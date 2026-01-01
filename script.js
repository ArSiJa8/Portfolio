const Hamburger = document.querySelector('.hamburger');
const NavMenu = document.querySelector('.nav-menu');

Hamburger.addEventListener('click', () => {
    Hamburger.classList.toggle('active');
    NavMenu.classList.toggle('active');
});

document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    Hamburger.classList.remove('active');
    NavMenu.classList.remove('active');
}