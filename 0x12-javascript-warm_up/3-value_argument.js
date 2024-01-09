#!/usr/bin/node
// Prints first argument

const commands = process.argv.length;
if (commands[2] === undefined) console.log("No argument");
else console.log(process.argv[2]);
