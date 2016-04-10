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
    var lines = $('#textareaURLs').val().split(/\n/);

    // create empty variables
    var texts = []; // for array of urls
    var win = ''; // for opening urls in tabs

    // loop through list of urls to validate
    for (var i=0; i < lines.length; i++) {
      // only manage this line if it contains a non whitespace character.
      if (/\S/.test(lines[i])) {

        // validate url and add http protocol if missing
        if (!lines[i].match(/^[a-zA-Z]+:\/\//))
        {
          lines[i] = 'http://' + lines[i];
        }

        // push line to array
        texts.push($.trim(lines[i]));
      };
    };

    // get length of array
    var textsLength = texts.length;

    // loop through array of urls and open
    for (var i=0; i < textsLength; i++) {
      win = window.open(texts[i], '_blank');
    };
  });
});