#!/usr/bin/node

const request = require('request');

// Make the GET request
request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error(error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
