#!/usr/bin/node
// Prints first argument

let i;
if (isNaN(process.argv[2])) {
  console.log("Missing number of occurences");
} else {
  for (i = 0; i < Number(process.argv[2]); i++) {
    console.log("C is fun");
  }
}
