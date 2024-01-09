#!/usr/bin/node
// A script that works with command line arguments

const commands = process.argv.length;
if (commands === 2) console.log('No argument');
else if (process.argv.length === 3) console.log('Argument found');
else console.log('Arguments found');
