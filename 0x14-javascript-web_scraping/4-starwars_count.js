#!/usr/bin/node

const request = require('request');

// Make the GET request to the Star Wars API to get all films
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    // Parse the response body to extract film data
    const filmsData = JSON.parse(body);

    // Filter films where Wedge Antilles is present
    const filmCount = filmsData.results.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    // Print the number of movies with Wedge Antilles
    console.log(filmCount.length);
  }
});
