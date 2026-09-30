/* Lightweight animated neural network drawn on a 2D canvas (AI & Data page). */
(() => {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.querySelector('[data-neural-canvas]');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let width = 0, height = 0, nodes = [], edges = [], pulses = [], running = true;

    function build() {
      const rect = canvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = rect.width; height = rect.height;
      canvas.width = width * dpr; canvas.height = height * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      const layers = width < 500 ? [3, 4, 4, 2] : [4, 6, 6, 3];
      nodes = []; edges = [];
      layers.forEach((count, layer) => {
        for (let i = 0; i < count; i++) {
          nodes.push({ layer, x: width * (0.1 + 0.8 * layer / (layers.length - 1)), y: height * (i + 1) / (count + 1) });
        }
      });
      nodes.forEach((a, i) => nodes.forEach((b, j) => { if (b.layer === a.layer + 1) edges.push([i, j]); }));
      pulses = Array.from({ length: width < 500 ? 6 : 12 }, () => ({ edge: Math.floor(Math.random() * edges.length), t: Math.random() }));
    }

    function draw() {
      ctx.clearRect(0, 0, width, height);
      ctx.lineWidth = 1;
      ctx.strokeStyle = 'rgba(0,255,136,.13)';
      edges.forEach(([a, b]) => { ctx.beginPath(); ctx.moveTo(nodes[a].x, nodes[a].y); ctx.lineTo(nodes[b].x, nodes[b].y); ctx.stroke(); });

      pulses.forEach((p) => {
        const [a, b] = edges[p.edge];
        const x = nodes[a].x + (nodes[b].x - nodes[a].x) * p.t;
        const y = nodes[a].y + (nodes[b].y - nodes[a].y) * p.t;
        ctx.fillStyle = '#00FF88'; ctx.shadowColor = '#00FF88'; ctx.shadowBlur = 10;
        ctx.beginPath(); ctx.arc(x, y, 2.4, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
        if (!reduceMotion) {
          p.t += 0.008;
          if (p.t >= 1) { p.t = 0; p.edge = Math.floor(Math.random() * edges.length); }
        }
      });

      nodes.forEach((n) => {
        ctx.fillStyle = '#0B0F0D'; ctx.strokeStyle = 'rgba(0,255,136,.7)';
        ctx.beginPath(); ctx.arc(n.x, n.y, 6, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
      });
    }

    function loop() {
      if (running) draw();
      if (!reduceMotion) requestAnimationFrame(loop);
    }

    build();
    draw();
    if (!reduceMotion) loop();
    window.addEventListener('resize', () => { build(); draw(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([entry]) => { running = entry.isIntersecting; }).observe(canvas);
    }
  });
})();
