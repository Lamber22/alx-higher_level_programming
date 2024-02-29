// Toggles the class of HTML tag 'HEADER' when user clicks the
// div#toggle_header tag

$('div#toggle_header').on('click', function () {
    $('header').ToggleClass('red');
  });