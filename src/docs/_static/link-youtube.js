// Link a YouTube in una nuova scheda. Gli ascolti guidati, il canale nell'intestazione
// e gli altri collegamenti a youtube.com o youtu.be si aprono in una scheda separata,
// così il lettore non perde la pagina degli appunti. reStructuredText non permette
// di indicare il target di un link: lo script lo aggiunge dopo il caricamento.
// File identico nei tre volumi.
(function () {
  'use strict';
  var YOUTUBE = /(^|\.)(youtube\.com|youtu\.be)$/i;

  function apriInNuovaScheda() {
    var link = document.querySelectorAll('a[href]');
    for (var i = 0; i < link.length; i++) {
      var a = link[i];
      if (!YOUTUBE.test(a.hostname)) continue;
      a.target = '_blank';
      var rel = (a.getAttribute('rel') || '').split(/\s+/).filter(Boolean);
      ['noopener', 'noreferrer'].forEach(function (r) {
        if (rel.indexOf(r) < 0) rel.push(r);
      });
      a.setAttribute('rel', rel.join(' '));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apriInNuovaScheda);
  } else {
    apriInNuovaScheda();
  }
})();
