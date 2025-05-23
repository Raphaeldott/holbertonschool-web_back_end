const express = require('express');
const fs = require('fs');

const app = express();
const PORT = 1245;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines
        .filter((line, index) => line && index !== 0) // skip header, ignore empty lines
        .map((line) => line.split(','));

      const groups = {};
      for (const student of students) {
        const field = student[3];
        if (!groups[field]) groups[field] = [];
        groups[field].push(student[0]);
      }

      let output = `Number of students: ${students.length}`;
      for (const [field, names] of Object.entries(groups)) {
        output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      resolve(output);
    });
  });
}

// Route: /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route: /students
app.get('/students', async (req, res) => {
  const database = process.argv[2];
  if (!database) {
    res.status(500).send('Cannot load the database');
    return;
  }

  try {
    const studentSummary = await countStudents(database);
    res.send(`This is the list of our students\n${studentSummary}`);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.listen(PORT);

module.exports = app;
