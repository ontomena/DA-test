// Keep nav pinned directly beneath header when both are sticky
(function() {
  const header = document.querySelector('header');
  const nav = document.querySelector('nav');
  if (!header || !nav) return;

  function updateNavTop() {
    const headerHeight = header.getBoundingClientRect().height;
    nav.style.top = headerHeight + 'px';
  }

  // Set initial position
  updateNavTop();

  // Update on scroll (header may change size via .scrolled class)
  let ticking = false;
  window.addEventListener('scroll', function() {
    const scrollPosition = window.scrollY;

    if (scrollPosition > 150) {
      header.classList.add('scrolled');
      nav.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
      nav.classList.remove('scrolled');
    }

    if (!ticking) {
      requestAnimationFrame(function() {
        updateNavTop();
        ticking = false;
      });
      ticking = true;
    }
  });

  // Also update on resize
  window.addEventListener('resize', updateNavTop);
})();
