// materializecss init
$(document).ready(function(){
  $('.button-collapse').sideNav();
  $('.parallax').parallax();
});


// prevent form natively firing
$(document).ready(function() {
  $('#formURLs').on('submit', function(e) {
    // prevent form from submitting normally and refreshing page
    e.preventDefault();
  });
});


// select opening or listing urls
function methodType(buttonid) {
    // store data from form into variable
    var data = $('#textareaURLs').val();

    // check what method has been used to submit form
    if (buttonid == 'links_open') {
      var method = 'open';
    } else if (buttonid == 'links_list') {
      var method = 'list';
    } else {
      var method = 'error';

      // insert alert string
      document.getElementById('modal1-header').innerHTML = 'Oops!';
      document.getElementById('modal1-text').innerHTML = 'Something went wrong. Please check your input and try again.';

      // alert if no valid method is selected
      $('#modal1').openModal();
      return false;
    };

    // validate data
    validateURLs(data, method);
};


// validate data
function validateURLs(data, method) {
  // split data lines into array
  var lines = data.split(/\n/);

  // create empty array to store valid urls
  var urlArray = [];

  // create variable to count skipped rows
  var skipped = 0;

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
      // increment skipped line count
      skipped++;
    };
  };

  // store length of array
  var arrayLength = urlArray.length;

  // check if array is empty
  if ( !(arrayLength > 0) ) {
    // insert alert string
    document.getElementById('modal1-header').innerHTML = 'Oops!';
    document.getElementById('modal1-text').innerHTML = 'Please enter at least one valid url.';

    // alert if no valid text is entered
    $('#modal1').openModal();
    return false;
  };

  // if items exist in array then run with correct function
  if ( (arrayLength > 0) && (method == 'open') ) {
    openURLs(urlArray, arrayLength, skipped);
  } else if ( (arrayLength > 0) && (method == 'list') ) {
    listURLs(urlArray, arrayLength, skipped);
  } else {
    // insert alert string
    document.getElementById('modal1-header').innerHTML = 'Oops!';
    document.getElementById('modal1-text').innerHTML = 'Something went wrong. Please check your input and try again.';

    // alert if no valid method is selected
    $('#modal1').openModal();
    return false;
  };
};


// open validated list of urls
function openURLs(urlArray, arrayLength, skipped) {
  console.log('open function');

  // alert for skipped lines
  alertSkipped(skipped);

  // variable for opening urls in tabs
  var win = '';

  // loop through array of urls and open
  for (var i=0; i < arrayLength; i++) {
    win = window.open(urlArray[i], '_blank');
  };
};


// list validated list of urls
function listURLs(urlArray, arrayLength, skipped) {
  console.log('list function');

  // alert for skipped lines
  alertSkipped(skipped);

  // unhide results table
  document.getElementById('linkCollection').className = 'collection with-header white left-align';

  // variables for building html list of urls
  var listTitleHTML = '<h4 class="collection-header grey-text text-darken-3">Submitted URLs</h4>';
  var listBodyHTML = '';

  // loop through array of urls and open
  for (var i=0; i < arrayLength; i++) {
    listBodyHTML += '<a href="' + urlArray[i] + '" class="collection-item truncate" target="_blank"><div class="left truncate">' + urlArray[i] + '</div><span class="secondary-content"><i class="material-icons">open_in_new</i></span></a>';
  };

  // concatenate html to be injected
  listHTML = listTitleHTML + listBodyHTML;

  // inject html into page
  document.getElementById('linkCollection').innerHTML = listHTML;
};


// alert to announce skipped lines
function alertSkipped(skippedQty) {
  if (skippedQty > 0) {
    // insert alert string
    document.getElementById('modal1-header').innerHTML = 'Lines Skipped';
    document.getElementById('modal1-text').innerHTML = 'Please note there were ' + skippedQty + ' lines skipped in your submitted data.';

    // alert if no valid text is entered
    $('#modal1').openModal();
  } else {
    return false;
  };
};