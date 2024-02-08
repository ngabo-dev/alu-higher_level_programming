#!/usr/bin/node
const request = require('request');

function getNumberOfMoviesWithCharacter (apiUrl, characterId) {
  let totalMovies = 0;

  function fetchMovies (url) {
    request.get(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
        return;
      }

      const data = JSON.parse(body);
      const movies = data.results;

      // Check if Wedge Antilles is present in each movie
      movies.forEach(movie => {
        if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          totalMovies++;
        }
      });

      // Check if there are more pages to fetch
      if (data.next) {
        fetchMovies(data.next);
      } else {
        console.log(`${totalMovies}`);
      }
    });
  }

  fetchMovies(apiUrl);
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <api_url>');
} else {
  const apiUrl = process.argv[2];
  const characterId = 18; // Character ID for Wedge Antilles
  getNumberOfMoviesWithCharacter(apiUrl, characterId);
}
