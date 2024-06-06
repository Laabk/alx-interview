#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (erro, res, body) => {
  erro && console.log(erro);

  const charactersArray = (JSON.parse(res.body).characters);
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (erro, res, body) => {
        erro && console.log(erro);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
