// Gentle animations (GSAP + ScrollTrigger, stored in js/vendor/).
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

  // Wrap each word of a heading in a span so the words can appear one after another.
  // The words stay real text, so search engines and screen readers read the heading as normal.
  function splitWords(el) {
    var words = [];
    Array.prototype.slice.call(el.childNodes).forEach(function (node) {
      if (node.nodeType !== 3) return;
      var frag = document.createDocumentFragment();
      node.textContent.split(/(\s+)/).forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
        var w = document.createElement('span');
        w.className = 'w';
        w.textContent = part;
        frag.appendChild(w);
        words.push(w);
      });
      el.replaceChild(frag, node);
    });
    return words;
  }

  // 1. Hero: the eyebrow appears, the heading comes into focus word by word,
  //    then the text and buttons rise in, and the gold line along the bottom draws across.
  var hero = document.querySelector('.hero .wrap');
  if (hero) {
    var eyebrow = hero.querySelector('.eyebrow');
    var h1 = hero.querySelector('h1');
    var rest = hero.querySelectorAll('.lead, .hero-actions');
    var words = h1 ? splitWords(h1) : [];
    var tl = gsap.timeline({ delay: 0.1 });
    if (eyebrow) tl.fromTo(eyebrow, { autoAlpha: 0, y: 12 }, { autoAlpha: 1, y: 0, duration: 0.6 });
    if (h1) {
      gsap.set(h1, { autoAlpha: 1 });
      tl.fromTo(words, { opacity: 0, y: 14, filter: 'blur(8px)' },
        { opacity: 1, y: 0, filter: 'blur(0px)', duration: 0.7, stagger: 0.07,
          onComplete: function () { gsap.set(words, { clearProps: 'all' }); } }, '-=0.25');
    }
    if (rest.length) tl.fromTo(rest, { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, stagger: 0.12, duration: 0.8,
      onComplete: function () { gsap.set(rest, { clearProps: 'all' }); } }, '-=0.35');
    tl.add(function () { root.classList.add('hero-line-in'); }, 0.4);
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
    '.values > div', '.split > div', '.aside > *', '.contact-card', '.checks li',
    '.cta-inner > *', '.footer-grid > div'
  ].join(',');
  var onScreen = function (el) { return el.getBoundingClientRect().top < window.innerHeight * 0.92; };
  var all = gsap.utils.toArray(selectors);
  var items = all.filter(function (el) {
    // Skip anything already on screen when the page opens (so nothing flickers),
    // and anything inside a block that already fades in as a whole (so nothing animates twice).
    if (onScreen(el)) return false;
    for (var p = el.parentElement; p; p = p.parentElement) { if (all.indexOf(p) !== -1) return false; }
    return true;
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

  // 4. Gold lines above "Our mission / vision / values" draw across when they come into view.
  gsap.utils.toArray('.values > div').forEach(function (el) {
    if (onScreen(el)) { el.classList.add('is-drawn'); return; }
    ScrollTrigger.create({ trigger: el, start: 'top 88%', once: true,
      onEnter: function () { el.classList.add('is-drawn'); } });
  });

  // 5. Lawyer's portrait: soft reveal from a slight zoom; its gold frame settles in behind it.
  gsap.utils.toArray('.portrait').forEach(function (img) {
    if (onScreen(img)) { img.classList.add('is-framed'); return; }
    gsap.fromTo(img, { opacity: 0, scale: 1.04 }, {
      opacity: 1, scale: 1, duration: 1.2,
      scrollTrigger: { trigger: img, start: 'top 85%', once: true },
      onStart: function () { img.classList.add('is-framed'); },
      onComplete: function () { gsap.set(img, { clearProps: 'transform,opacity' }); }
    });
  });

  // Images and fonts can shift the layout after load; re-measure trigger points.
  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
