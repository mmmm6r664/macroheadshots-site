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
