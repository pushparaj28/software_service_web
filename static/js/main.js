/* Site-wide behaviour: loader, scroll reveal, flash messages, tech cards, form state. */
(() => {
  'use strict';

  const ready = (fn) => (document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fn) : fn());
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function hideLoader() {
    const loader = document.querySelector('[data-loader]');
    if (!loader) return;
    const done = () => loader.classList.add('is-done');
    window.addEventListener('load', done, { once: true });
    setTimeout(done, 2500); // failsafe
  }

  function initReveal() {
    const items = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window) || reduceMotion) {
      items.forEach((el) => el.classList.add('is-visible'));
      return;
    }
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach((el) => observer.observe(el));
  }

  function initMessages() {
    document.querySelectorAll('[data-flash]').forEach((el) => {
      el.querySelector('[data-flash-close]')?.addEventListener('click', () => el.remove());
      setTimeout(() => el.remove(), 8000);
    });
  }

  // Touch devices have no hover, so tapping a technology card toggles its description.
  function initTechCards() {
    document.addEventListener('click', (event) => {
      const card = event.target.closest('[data-tech-card]');
      if (card) card.classList.toggle('is-open');
    });
  }

  function initForms() {
    document.querySelectorAll('form[data-submit-lock]').forEach((form) => {
      form.addEventListener('submit', () => {
        const button = form.querySelector('button[type="submit"]');
        if (button) { button.disabled = true; button.textContent = 'SENDING…'; }
      });
    });
  }

  ready(() => {
    const year = document.querySelector('[data-year]');
    if (year) year.textContent = new Date().getFullYear();
    hideLoader();
    initReveal();
    initMessages();
    initTechCards();
    initForms();
  });
})();
