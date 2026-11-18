// Gentle scroll animations (GSAP + ScrollTrigger, stored in js/vendor/).
// Calm and professional on purpose: short fades and small lifts, nothing that spins or bounces.
// Visitors who ask their device for less motion see the page with no animation.
(function () {
  var root = document.documentElement;
  if (!window.gsap || !window.ScrollTrigger || !root.classList.contains('motion')) {
    root.classList.remove('motion');
    return;
  }
  gsap.registerPlugin(ScrollTrigger);
  gsap.defaults({ ease: 'power2.out', duration: 0.8 });

  // 1. Hero: eyebrow, heading, text and buttons rise in one after another.
  var hero = document.querySelector('.hero .wrap');
  if (hero) {
    var parts = hero.querySelectorAll('.eyebrow, h1, .lead, .hero-actions');
    gsap.timeline({ onComplete: function () { gsap.set(parts, { clearProps: 'all' }); } })
      .fromTo(parts, { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, stagger: 0.14, duration: 0.9 });
    root.classList.add('motion-ready');
  }

  // 2. Background video drifts slightly slower than the page as you scroll (depth effect).
  var video = document.querySelector('.hero-video');
  if (video) {
    gsap.to(video, {
      yPercent: 12, ease: 'none',
      scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
    });
  }

  // 3. Content fades up as it scrolls into view, a few items at a time.
  var selectors = [
    '.section .eyebrow', '.section h2', '.section .prose > *', '.cards .card',
    '.values > div', '.split > div', '.aside-box', '.contact-card', '.checks li',
    '.cta-inner > *', '.footer-grid > div'
  ].join(',');
  var items = gsap.utils.toArray(selectors).filter(function (el) {
    // Skip anything already on screen when the page opens, so nothing flickers.
    return el.getBoundingClientRect().top > window.innerHeight * 0.92;
  });
  gsap.set(items, { opacity: 0, y: 28 });
  ScrollTrigger.batch(items, {
    start: 'top 90%',
    once: true,
    onEnter: function (batch) {
      batch.forEach(function (el) { el.classList.add('is-revealing'); });
      gsap.to(batch, {
        opacity: 1, y: 0, stagger: 0.1, overwrite: true,
        onComplete: function () {
          batch.forEach(function (el) { el.classList.remove('is-revealing'); });
          gsap.set(batch, { clearProps: 'transform,opacity' });
        }
      });
    }
  });

  // 4. Lawyer's portrait: soft reveal from a slight zoom.
  gsap.utils.toArray('.portrait').forEach(function (img) {
    if (img.getBoundingClientRect().top < window.innerHeight * 0.92) return;
    gsap.fromTo(img, { opacity: 0, scale: 1.06 }, {
      opacity: 1, scale: 1, duration: 1.2,
      scrollTrigger: { trigger: img, start: 'top 85%', once: true }
    });
  });

  // 5. Header gets a soft shadow once you scroll down.
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Images and fonts can shift the layout after load; re-measure trigger points.
  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
