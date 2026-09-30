/* Hero "digital matrix": a 3D lattice that tilts with the mouse.
   Uses Three.js when available and falls back to a 2D canvas projection. */
(() => {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.querySelector('[data-hero-canvas]');
    if (!canvas) return;

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const small = window.innerWidth < 768;
    const N = small ? 3 : 5;      // lattice size (fewer points on mobile)
    const GAP = 0.7;
    const mouse = { x: 0, y: 0 };
    let visible = true;

    window.addEventListener('pointermove', (e) => {
      mouse.x = (e.clientX / window.innerWidth - 0.5) * 2;
      mouse.y = (e.clientY / window.innerHeight - 0.5) * 2;
    }, { passive: true });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; }).observe(canvas);
    }

    // Lattice points and the links between neighbours.
    const points = [];
    for (let x = 0; x < N; x++) for (let y = 0; y < N; y++) for (let z = 0; z < N; z++) {
      points.push([(x - (N - 1) / 2) * GAP, (y - (N - 1) / 2) * GAP, (z - (N - 1) / 2) * GAP]);
    }
    const at = (x, y, z) => (x * N + y) * N + z;
    const links = [];
    for (let x = 0; x < N; x++) for (let y = 0; y < N; y++) for (let z = 0; z < N; z++) {
      if (x < N - 1) links.push([at(x, y, z), at(x + 1, y, z)]);
      if (y < N - 1) links.push([at(x, y, z), at(x, y + 1, z)]);
      if (z < N - 1) links.push([at(x, y, z), at(x, y, z + 1)]);
    }

    window.THREE ? runThree() : runFallback();

    function runThree() {
      const renderer = new THREE.WebGLRenderer({ canvas, antialias: !small, alpha: true });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, small ? 1.5 : 2));
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
      camera.position.z = 9;
      const group = new THREE.Group();
      scene.add(group);

      const flat = new Float32Array(points.flat());
      const pointGeo = new THREE.BufferGeometry();
      pointGeo.setAttribute('position', new THREE.BufferAttribute(flat, 3));
      group.add(new THREE.Points(pointGeo, new THREE.PointsMaterial({ color: 0x00ff88, size: 0.07 })));

      const lineGeo = new THREE.BufferGeometry();
      lineGeo.setAttribute('position', new THREE.Float32BufferAttribute(links.flatMap(([a, b]) => [...points[a], ...points[b]]), 3));
      group.add(new THREE.LineSegments(lineGeo, new THREE.LineBasicMaterial({ color: 0x27f5a2, transparent: true, opacity: 0.22 })));

      const size = (N - 1) * GAP + 0.8;
      group.add(new THREE.LineSegments(
        new THREE.EdgesGeometry(new THREE.BoxGeometry(size, size, size)),
        new THREE.LineBasicMaterial({ color: 0x00ff88, transparent: true, opacity: 0.5 })
      ));

      const resize = () => {
        const { clientWidth: w, clientHeight: h } = canvas;
        if (!w || !h) return;
        renderer.setSize(w, h, false);
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
        renderer.render(scene, camera);
      };
      resize();
      window.addEventListener('resize', resize);

      let spin = 0, tiltX = 0, tiltY = 0;
      const frame = () => {
        if (visible && !document.hidden) {
          spin += 0.003;
          tiltX += (mouse.y * 0.3 - tiltX) * 0.05;
          tiltY += (mouse.x * 0.4 - tiltY) * 0.05;
          group.rotation.set(0.35 + tiltX, spin + tiltY, 0);
          renderer.render(scene, camera);
        }
        requestAnimationFrame(frame);
      };
      if (!reduceMotion) frame();
    }

    function runFallback() {
      const ctx = canvas.getContext('2d');
      let w = 0, h = 0, spin = 0, tiltX = 0, tiltY = 0;

      const resize = () => {
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        w = canvas.clientWidth; h = canvas.clientHeight;
        canvas.width = w * dpr; canvas.height = h * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        draw();
      };

      const project = ([x, y, z], ay, ax) => {
        const x1 = x * Math.cos(ay) + z * Math.sin(ay);
        const z1 = -x * Math.sin(ay) + z * Math.cos(ay);
        const y1 = y * Math.cos(ax) - z1 * Math.sin(ax);
        const z2 = y * Math.sin(ax) + z1 * Math.cos(ax);
        const scale = (Math.min(w, h) / 5) * (5 / (5 - z2));
        return [w / 2 + x1 * scale, h / 2 + y1 * scale];
      };

      function draw() {
        ctx.clearRect(0, 0, w, h);
        const projected = points.map((p) => project(p, spin + tiltY, 0.35 + tiltX));
        ctx.strokeStyle = 'rgba(39,245,162,.22)'; ctx.lineWidth = 1;
        links.forEach(([a, b]) => { ctx.beginPath(); ctx.moveTo(...projected[a]); ctx.lineTo(...projected[b]); ctx.stroke(); });
        ctx.fillStyle = '#00FF88';
        projected.forEach(([x, y]) => { ctx.beginPath(); ctx.arc(x, y, 2, 0, Math.PI * 2); ctx.fill(); });
      }

      const frame = () => {
        if (visible && !document.hidden) {
          spin += 0.003;
          tiltX += (mouse.y * 0.3 - tiltX) * 0.05;
          tiltY += (mouse.x * 0.4 - tiltY) * 0.05;
          draw();
        }
        requestAnimationFrame(frame);
      };
      resize();
      window.addEventListener('resize', resize);
      if (!reduceMotion) frame();
    }
  });
})();
