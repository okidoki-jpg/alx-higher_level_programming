#!/usr/bin/node

const request = require('request');

// Make the GET request to the API
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    // Parse the response body as JSON
    const todosData = JSON.parse(body);

    // Create an object to store completed tasks count per user id
    const taskCount = {};

    // Iterate through the todos and count completed tasks per user id
    for (const todo of todosData) {
      if (todo.completed) {
        if (taskCount[todo.userId]) {
          taskCount[todo.userId]++;
        } else {
          taskCount[todo.userId] = 1;
        }
      }
    }

    // Print users with completed tasks and their count
    console.log(taskCount);
  }
});
