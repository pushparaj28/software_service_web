/* Minimal custom cursor: white dot, green ring over interactive elements. Desktop only. */
(() => {
  'use strict';

  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

  document.addEventListener('DOMContentLoaded', () => {
    const dot = document.querySelector('[data-cursor-dot]');
    const ring = document.querySelector('[data-cursor-ring]');
    if (!dot || !ring) return;

    document.documentElement.classList.add('has-cursor');
    const INTERACTIVE = 'a, button, input, select, textarea, label, [data-cursor-hover]';
    let x = 0, y = 0, rx = 0, ry = 0;

    window.addEventListener('mousemove', (e) => {
      x = e.clientX; y = e.clientY;
      dot.style.transform = `translate3d(${x}px, ${y}px, 0)`;
    }, { passive: true });

    const follow = () => {
      rx += (x - rx) * 0.18;
      ry += (y - ry) * 0.18;
      ring.style.transform = `translate3d(${rx}px, ${ry}px, 0)`;
      requestAnimationFrame(follow);
    };
    follow();

    document.addEventListener('mouseover', (e) => { if (e.target.closest(INTERACTIVE)) ring.classList.add('is-active'); });
    document.addEventListener('mouseout', (e) => { if (e.target.closest(INTERACTIVE)) ring.classList.remove('is-active'); });
  });
})();
