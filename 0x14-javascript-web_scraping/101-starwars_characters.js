#!/usr/bin/node

const request = require('request');

function getDataFrom (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, _res, body) {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

function errHandler (error) {
  console.log(error);
}

function printMovieCharacters (movieId) {
  const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUrl)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      for (let i = 0; i < characters.length; ++i) {
        promises.push(getDataFrom(characters[i]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let i = 0; i < results.length; ++i) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    });
}

printMovieCharacters(process.argv[2]);
