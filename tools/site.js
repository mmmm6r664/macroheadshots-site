// Small replacements for the interactive bits the original site got from its builder's app bundle.
(function () {
  // FAQ accordion
  document.querySelectorAll('.hl-faq-child').forEach(function (item) {
    var head = item.querySelector('.hl-faq-child-heading');
    var panel = item.querySelector('.hl-faq-child-panel');
    if (!head || !panel) return;
    head.style.cursor = 'pointer';
    head.addEventListener('click', function () {
      var open = item.classList.toggle('faq-open');
      if (open) {
        panel.style.height = 'auto';
        panel.style.padding = '';
        panel.style.opacity = '1';
      } else {
        panel.style.height = '0';
        panel.style.padding = '0';
        panel.style.opacity = '0';
      }
      var icon = item.querySelector('.hl-faq-child-heading-icon');
      if (icon) icon.style.transform = open ? 'rotate(90deg)' : '';
    });
  });

  // Mobile navigation menu
  var css = document.createElement('style');
  css.textContent =
    '.mh-nav-open .nav-menu{display:flex!important;flex-direction:column;position:fixed;top:0;right:0;' +
    'height:100vh;width:min(80vw,320px);background:#fff;z-index:99999;padding:70px 24px 24px;margin:0;' +
    'box-shadow:-4px 0 20px rgba(0,0,0,.25);gap:8px}' +
    '.mh-nav-open .nav-menu .nav-menu-item a{color:#000!important;font-size:18px}' +
    '.mh-nav-open .nav-menu-mobile{position:fixed;top:18px;right:18px;z-index:100000}' +
    '.mh-nav-open .menu-icon{filter:invert(1)}' +
    '.hl-faq-child-heading-icon{transition:transform .2s}';
  document.head.appendChild(css);
  document.querySelectorAll('.nav-menu-wrapper').forEach(function (nav) {
    var btn = nav.querySelector('.menu-icon');
    if (!btn) return;
    function toggle() { nav.classList.toggle('mh-nav-open'); }
    btn.addEventListener('click', toggle);
    btn.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
  });
})();
