import fs from 'fs/promises';

export function readDatabase(path) {
  return fs.readFile(path, 'utf-8')
    .then(data => {
      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter(line => line);
      const fields = {};

      for (const line of students) {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      }

      return fields;
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}