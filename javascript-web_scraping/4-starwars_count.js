#!/usr/bin/node
const request = require('request');

function countMoviesWithCharacter (apiUrl, characterId) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
      return;
    }

    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    });

    console.log(count);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <api_url>');
} else {
  const apiUrl = process.argv[2];
  const characterId = 18;
  countMoviesWithCharacter(apiUrl, characterId);
}
