// materializecss init
$(document).ready(function(){
  $('.button-collapse').sideNav();
  $('.parallax').parallax();
});


// prevent form natively firing and instead store input data
$(document).ready(function() {
  $('#formURLs').on('submit', function(e) {
    // prevent form from submitting normally and refreshing page
    e.preventDefault();

    // store data from form into variable
    var data = $('#textareaURLs').val();

    // validate data
    validateURLs(data);
  });
});


// validate data
function validateURLs(data) {
  // split data lines into array
  var lines = data.split(/\n/);

  // create empty array to store valid urls
  var urlArray = [];

  // loop through list of urls to validate
  for (var i=0; i < lines.length; i++) {
    // handle array item if it contains a non whitespace character.
    if (/\S/.test(lines[i])) {
      // add http protocol if missing
      if (!lines[i].match(/^[a-zA-Z]+:\/\//))
      {
        lines[i] = 'http://' + lines[i];
      };

      // push line to array
      urlArray.push($.trim(lines[i]));
    } else {
      // alert if no valid text is entered
      alert('Please enter at least one valid url.');
    };
  };

  // store length of array
  var arrayLength = urlArray.length;

  // if items exist in array then open urls
  if (arrayLength > 0) {
    openURLs(urlArray, arrayLength);
  };
};


// open validated list of urls
function openURLs(urlArray, arrayLength) {
  // variable for opening urls in tabs
  var win = '';

  // loop through array of urls and open
  for (var i=0; i < arrayLength; i++) {
    win = window.open(urlArray[i], '_blank');
  };
};