const readline = require('readline');

const readLine = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

readLine.question('', (name) => {
  console.log(`Your name is: ${name}`);

  // Only print closing message if input is NOT a TTY (i.e., piped input)
  if (!process.stdin.isTTY) {
    console.log('This important software is now closing');
  }

  readLine.close();
});
