#!/usr/bin/node
const request = require('request');

function getNumberOfMoviesWithCharacter (apiUrl, characterId) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
      return;
    }

    const films = JSON.parse(body).results;
    const moviesWithCharacter = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(`${moviesWithCharacter.length}`);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <api_url>');
} else {
  const apiUrl = process.argv[2];
  const characterId = 18; // Character ID for Wedge Antilles
  getNumberOfMoviesWithCharacter(apiUrl, characterId);
}
