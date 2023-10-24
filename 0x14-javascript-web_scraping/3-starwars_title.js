#!/usr/bin/node
# script that prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node 3-starwars_title.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    } else {
      console.log(`Movie with ID ${movieId} not found.`);
    }
  }
});
