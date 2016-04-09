// init
$(document).ready(function(){
  $('.button-collapse').sideNav();
  $('.parallax').parallax();
});


// main url opener function
$(document).ready(function() {
  $('#formURLs').on('submit', function(e) {
    // prevent form from submitting normally and refreshing page
    e.preventDefault();

    // store textarea field into variable
    var data = document.getElementById('textareaURLs').value;

    // store url in variable
    var url = data;

    // append http if does not exist
    if (!url.match(/^[a-zA-Z]+:\/\//))
    {
      url = 'http://' + url;
    }

    // open url
    var win = window.open(url, '_blank');

    // focus on opened tab or alert that function is disabled
    if(win) {
      // if new tab is allowed
      win.focus();
      url = '';
      win = '';
    } else {
      // if new tab is not allowed
      alert('Please allow popups for this site');
      url = '';
      win = '';
    };
  });
});