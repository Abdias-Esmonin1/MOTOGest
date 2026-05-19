// MotoGest — Charts helpers
// Les graphiques sont initialisés directement dans chaque template
// Ce fichier contient les utilitaires partagés

window.MotoGestCharts = {
  colors: {
    primary: '#1a472a',
    primaryLight: '#2d6a4f',
    accent: '#f0a500',
    danger: '#dc3545',
    info: '#0d6efd',
    muted: '#adb5bd',
  },

  defaultOptions: function (yLabel) {
    return {
      responsive: true,
      plugins: { legend: { position: 'top' } },
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: function (v) {
              return v.toLocaleString('fr-FR') + ' F';
            }
          }
        }
      }
    };
  }
};
