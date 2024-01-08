#!/usr/bin/node
// A script that works with command line arguments

const commands = process.argv.length;
if (commands < 0) console.log("No argument");
else if (process.argv.length === 1) console.log("Argument found");
else console.log("Arguments found");
