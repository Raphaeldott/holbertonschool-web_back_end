export default function appendToEachArrayValue(array, appendString) {
    for (const [index, value] of array.entries()) {  // Get index and value using array.entries()
      array[index] = appendString + value;           // Modify array element
    }
  
    return array;
  }
  