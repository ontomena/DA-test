// Add 'scrolled' class to header and nav when user scrolls past piano strip
window.addEventListener('scroll', function() {
  const header = document.querySelector('header');
  const nav = document.querySelector('nav');
  const scrollPosition = window.scrollY;
  
  // Add class when scrolled past 150px (piano strip height)
  if (scrollPosition > 150) {
    header.classList.add('scrolled');
    nav.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
    nav.classList.remove('scrolled');
  }
});
