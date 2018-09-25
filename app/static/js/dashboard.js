$(document).ready(function() {
  'use strict'

  function createGraph() {
    return null;
  }

  $.getJSON($SCRIPT_ROOT + "stats", (response)=> {
    console.log(response);
  });
});
