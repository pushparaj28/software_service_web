/* Our Work: category filters + live search + "load more" – all client side. */
(() => {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const grid = document.querySelector('[data-project-grid]');
    if (!grid) return;

    const cards = [...grid.querySelectorAll('[data-project]')];
    const chips = [...document.querySelectorAll('[data-filter]')];
    const search = document.querySelector('[data-project-search]');
    const loadMore = document.querySelector('[data-load-more]');
    const empty = document.querySelector('[data-empty]');
    const count = document.querySelector('[data-count]');
    const PAGE_SIZE = 6;
    const state = { filter: 'all', query: '', limit: PAGE_SIZE };

    const matches = (card) =>
      (state.filter === 'all' || card.dataset.tags.split(' ').includes(state.filter)) &&
      card.dataset.title.includes(state.query);

    function render() {
      const found = cards.filter(matches);
      cards.forEach((card) => { card.hidden = true; });
      found.slice(0, state.limit).forEach((card) => { card.hidden = false; card.classList.add('is-visible'); });
      if (count) count.textContent = found.length;
      if (empty) empty.hidden = found.length > 0;
      if (loadMore) loadMore.hidden = found.length <= state.limit;
    }

    chips.forEach((chip) => chip.addEventListener('click', () => {
      state.filter = chip.dataset.filter;
      state.limit = PAGE_SIZE;
      chips.forEach((c) => c.classList.toggle('is-active', c === chip));
      render();
    }));

    search?.addEventListener('input', () => {
      state.query = search.value.trim().toLowerCase();
      state.limit = PAGE_SIZE;
      render();
    });

    loadMore?.addEventListener('click', () => { state.limit += PAGE_SIZE; render(); });
    render();
  });
})();
