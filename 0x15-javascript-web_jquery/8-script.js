$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
  var titles = data.results.map(function(movie) {
    return movie.title;
  });
  $("ul#list_movies").empty();
  $.each(titles, function(i, title) {
    $("ul#list_movies").append("<li>" + title + "</li>");
  });
});
