// MotoGest — JS global

document.addEventListener('DOMContentLoaded', function () {

  // --- Auto-dismiss alerts after 4s ---
  document.querySelectorAll('.alert.alert-dismissible').forEach(function (el) {
    setTimeout(function () {
      var bsAlert = bootstrap.Alert.getOrCreateInstance(el);
      if (bsAlert) bsAlert.close();
    }, 4000);
  });

  // --- Sidebar mobile overlay close on backdrop click ---
  document.addEventListener('click', function (e) {
    var sidebar = document.getElementById('sidebar');
    if (sidebar && sidebar.classList.contains('open')) {
      if (!sidebar.contains(e.target) && !e.target.closest('[onclick*="sidebar"]')) {
        sidebar.classList.remove('open');
      }
    }
  });

  // --- Saisie journalière : ajustement statut auto selon montant ---
  document.querySelectorAll('input[name^="montant_"]').forEach(function (input) {
    input.addEventListener('input', function () {
      var id = this.name.replace('montant_', '');
      var select = document.querySelector('select[name="statut_' + id + '"]');
      var val = parseInt(this.value) || 0;
      var max = parseInt(this.getAttribute('max') || this.dataset.max || 0);
      if (!select) return;
      if (val === 0) {
        select.value = 'absent';
      } else if (max > 0 && val < max) {
        select.value = 'partiel';
      } else if (val >= max && max > 0) {
        select.value = 'paye';
      }
    });
  });

  // --- Confirm suppression ---
  document.querySelectorAll('[data-confirm]').forEach(function (el) {
    el.addEventListener('click', function (e) {
      if (!confirm(this.dataset.confirm || 'Confirmer cette action ?')) {
        e.preventDefault();
      }
    });
  });

  // --- Tooltips Bootstrap ---
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.forEach(function (el) {
    new bootstrap.Tooltip(el);
  });

});
