// Macro Headshots site script: mobile navigation and cookie consent.
(function () {
  // ----- mobile navigation -----
  var nav = document.getElementById('nav');
  if (nav) {
    var btn = nav.querySelector('.nav-toggle');
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); });
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') nav.classList.remove('open'); });
  }

  // ----- cookie consent -----
  var KEY = 'mh-consent';
  function getConsent() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setConsent(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  var banner = document.getElementById('cookie-banner');

  function loadEmbeds() {
    document.querySelectorAll('[data-consent-embed]').forEach(function (box) {
      if (box.getAttribute('data-loaded')) return;
      box.setAttribute('data-loaded', '1');
      box.classList.add('consented');
      var s = document.createElement('script');
      s.src = box.getAttribute('data-consent-embed');
      s.async = true;
      document.body.appendChild(s);
    });
  }
  function apply(v) {
    if (v === 'all') loadEmbeds();
    if (banner) banner.hidden = true;
    document.body.classList.remove('has-cookie-banner');
  }
  function choose(v) { setConsent(v); apply(v); if (v === 'necessary') location.reload(); }

  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-consent]');
    if (t) { e.preventDefault(); choose(t.getAttribute('data-consent')); return; }
    if (e.target.closest('[data-cookie-settings]')) {
      e.preventDefault();
      if (banner) { banner.hidden = false; document.body.classList.add('has-cookie-banner'); banner.querySelector('button').focus(); }
    }
  });

  var current = getConsent();
  if (current) { apply(current); }
  else if (banner) { banner.hidden = false; document.body.classList.add('has-cookie-banner'); }
})();

// Gallery filters and lightbox
(function () {
  var grid = document.getElementById('gallery-grid');
  if (!grid) return;
  var items = [].slice.call(grid.querySelectorAll('.g-item'));
  document.querySelectorAll('.filter').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.filter').forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active');
      var f = b.getAttribute('data-filter');
      items.forEach(function (it) { it.classList.toggle('hide', f !== 'all' && it.getAttribute('data-cat') !== f); });
    });
  });
  var lb = document.getElementById('lightbox'), img = lb.querySelector('img'), cur = 0;
  function visible() { return items.filter(function (it) { return !it.classList.contains('hide'); }); }
  function show(i) { var v = visible(); cur = (i + v.length) % v.length; var src = v[cur].querySelector('img'); img.src = src.src; img.alt = src.alt; }
  items.forEach(function (it) {
    it.tabIndex = 0;
    function open() { lb.hidden = false; document.body.style.overflow = 'hidden'; show(visible().indexOf(it)); lb.querySelector('.lb-close').focus(); }
    it.addEventListener('click', open);
    it.addEventListener('keydown', function (e) { if (e.key === 'Enter') open(); });
  });
  function close() { lb.hidden = true; document.body.style.overflow = ''; }
  lb.querySelector('.lb-close').addEventListener('click', close);
  lb.querySelector('.lb-prev').addEventListener('click', function () { show(cur - 1); });
  lb.querySelector('.lb-next').addEventListener('click', function () { show(cur + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') close(); else if (e.key === 'ArrowLeft') show(cur - 1); else if (e.key === 'ArrowRight') show(cur + 1);
  });
  var x0 = null;
  lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) show(cur + (dx < 0 ? 1 : -1)); x0 = null; });
})();
