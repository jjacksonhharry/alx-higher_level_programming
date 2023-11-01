$(document).ready(function() {
  $("input#btn_translate").click(function() {
    var languageCode = $("input#language_code").val();
    var url = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;
    $.getJSON(url, function(data) {
      $("div#hello").text(data.hello);
    });
  });
});
