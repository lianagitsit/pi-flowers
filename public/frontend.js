$(document).ready(function() {
  console.log('frontend.js loaded');
  setInterval(checkServer, 500);
});

function checkServer() {
  console.log('checking flower status...');
  $.get("/status", function(data) {
    $('#eric').text(data.eric);
    $('#liana').text(data.liana);
  });
}
