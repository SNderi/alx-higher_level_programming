#!/usr/bin/node
// Node.js script that computes the number of tasks completed by user id.

const request = require('request');
const reqUrl = process.argv[2];
request(reqUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const tasks = {};
  for (const item in todos) {
    const key = todos[item];
    const id = key.userId;
    if (id in tasks === false) {
      tasks[id] = 0;
    }
    if (key.completed) {
      tasks[id] = tasks[id] + 1;
    }
  }
  console.log(tasks);
});
