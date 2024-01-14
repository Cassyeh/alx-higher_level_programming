#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, _res, body) {
  if (error) {
    console.log(error);
  } else {
    const completed_tasks = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completed_tasks[userId]) {
        completed_tasks[userId] = 0;
      }

      if (completed) ++completed_tasks[userId];
    }

    console.log(completed_tasks);
  }
});
