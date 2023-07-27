#!/usr/bin/node

const request = require('request');

// API URL
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

// Make the GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    // Parse the response body to extract the title
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
