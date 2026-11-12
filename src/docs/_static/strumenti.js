// Link verso gli Strumenti per la pratica (ADR 0005, punto 7).
// Gli strumenti sono su un altro dominio e non vedono il tema scelto in Shibuya
// (localStorage._theme): il parametro `theme` del deep link lo porta con sé.
// I link si aprono in una nuova scheda, così il capitolo resta dov'era.
(function () {
  'use strict';
  var script = document.currentScript;
  var base = script && script.getAttribute('data-base');
  if (!base) return;

  function mode() {
    var m = document.documentElement.getAttribute('data-color-mode');
    return m === 'dark' || m === 'light' ? m : 'auto';
  }

  function withTheme(href, theme) {
    var i = href.indexOf('#');
    var page = i < 0 ? href : href.slice(0, i);
    var params = (i < 0 ? '' : href.slice(i + 1)).split('&').filter(function (p) {
      return p && p.indexOf('theme=') !== 0;
    });
    if (!params.some(function (p) { return p.indexOf('v=') === 0; })) params.unshift('v=1');
    params.push('theme=' + theme);
    return page + '#' + params.join('&');
  }

  function update() {
    var theme = mode();
    var links = document.querySelectorAll('a[href^="' + base + '"]');
    for (var k = 0; k < links.length; k++) {
      var a = links[k];
      a.href = withTheme(a.getAttribute('href'), theme);
      a.target = '_blank';
      a.rel = 'noopener';
    }
  }

  update();
  new MutationObserver(update).observe(document.documentElement, {
    attributes: true, attributeFilter: ['data-color-mode'],
  });
})();
