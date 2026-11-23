// Menu laterale richiudibile. Shibuya non permette di chiudere la barra di
// navigazione a sinistra su schermi larghi: questo script aggiunge nell'intestazione,
// accanto al pulsante del tema, un pulsante che la nasconde o la mostra, così il
// contenuto (spartiti compresi) usa tutta la larghezza. La scelta vale per tutte
// le pagine del volume (localStorage) e si applica prima che la pagina compaia,
// senza sfarfallii. Su mobile il pulsante non c'è: lì il menu è già a scomparsa.
// Lo stile è in custom.css («Menu laterale richiudibile»).
(function () {
  'use strict';
  var KEY = 'appunti-menu-laterale';
  var root = document.documentElement;

  function chiuso() {
    return root.getAttribute('data-menu-laterale') === 'chiuso';
  }

  function imposta(c) {
    if (c) root.setAttribute('data-menu-laterale', 'chiuso');
    else root.removeAttribute('data-menu-laterale');
    try { localStorage.setItem(KEY, c ? 'chiuso' : 'aperto'); } catch (e) { /* storage non disponibile */ }
  }

  try {
    if (localStorage.getItem(KEY) === 'chiuso') root.setAttribute('data-menu-laterale', 'chiuso');
  } catch (e) { /* storage non disponibile: menu aperto */ }

  // Icona «panel-left» di Lucide, la stessa famiglia di icone di Shibuya.
  var ICONA = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" ' +
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/></svg>';

  function aggiorna(btn) {
    var c = chiuso();
    btn.setAttribute('aria-pressed', c ? 'true' : 'false');
    btn.setAttribute('aria-label', c ? 'Mostra il menu laterale' : 'Nascondi il menu laterale');
    btn.title = btn.getAttribute('aria-label');
  }

  function monta() {
    var azioni = document.querySelector('.sy-head-actions');
    if (!azioni || !document.getElementById('lside')) return;
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'menu-laterale-toggle';
    btn.setAttribute('aria-controls', 'lside');
    btn.innerHTML = ICONA;
    aggiorna(btn);
    btn.addEventListener('click', function () {
      imposta(!chiuso());
      aggiorna(btn);
    });
    azioni.insertBefore(btn, azioni.firstChild);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', monta);
  else monta();
})();
