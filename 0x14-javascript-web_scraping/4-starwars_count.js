#!/usr/bin/node
// Node.js script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const reqUrl = process.argv[2];
request(reqUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  const results = data.results;
  let moviesNum = 0;
  const antilles = 'https://swapi-api.hbtn.io/api/people/18/';

  for (let idx = 0; idx < data.count; idx++) {
    const actors = results[idx].characters;
    for (const actor in actors) {
      if (actors[actor] === antilles) {
        moviesNum += 1;
      }
    }
  }
  console.log(moviesNum);
});
