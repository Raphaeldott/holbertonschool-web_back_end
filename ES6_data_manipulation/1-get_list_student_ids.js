export default function getListStudentIds(studentlist) {
  if (!Array.isArray(studentlist)) {
    return [];
  }
  return studentlist.map((studentlist) => studentlist.id);
}
