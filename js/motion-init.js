// Runs before the page shows. Marks the page as "motion on" so the hero text can
// start hidden and fade in. Skipped for visitors who ask their device for less motion.
(function () {
  try {
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.documentElement.classList.add('motion');
    }
  } catch (e) {}
})();
