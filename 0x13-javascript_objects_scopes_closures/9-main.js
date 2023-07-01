#!/usr/bin/node
const logMe = require('./9-logme').logMe;

for (let index = 0; index < 100; index++) {
    logMe("Big loop " + index);    
}
