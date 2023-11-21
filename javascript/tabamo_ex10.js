/* Tabamo, Euan Jed S. | B-1L
Exercise 10 | November 21, 2023 */
/**
 * {DataTypeHere} - Note: used for usual data type declaration.
 * {(OneDataType|AnotherDataType)} - Note: used for cases where data type could be either of the two.
 * {DataType[]} - Note: used for an array of DataType instances.
 * {?DataTypeHere} - Note: used for data types which could be the data type mentioned or null.
 * {DataTypeHere} [parameterNameHere] - Note: used for optional parameters.
 * {Object.<KeyDataType, ValueDataType>} - Note: used for an object with KeyDataType keys and ValueDataType values
 */

const HOME = [3, 4];
let locationObject = {
  Chelsea: [-3, 3],
  Ralph: [8, 9],
  Andrew: [6, 7],
  Dustin: [15, 12],
};
let distanceArray = [];
/**
 * Finds the distance using the distance formula.
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Number[]} point - The coordinates of a point.
 * @return {Number} The distance between the origin and the point.
 */
function findDistance(origin, point) {
  let x2 = origin[0];
  let y2 = origin[1];
  let x1 = point[0];
  let y1 = point[1];
  return Number(Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2).toFixed(3));
}

/**
 * Collects and manages the specified origin array and all othercoordinates.
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object.<String,Number[]>} locations - The object containing persons and their coordinates
 * @return {Number[]} The array of distances.
 */
function processMap(origin, locations) {
  let entryArray = Object.entries(locations);
  let personArray = [];
  let distanceArray = [];
  for ([person, coordinates] of entryArray) {
    distanceFromHome = findDistance(origin, coordinates);
    console.log(`${person}'s distance from HOME: ${distanceFromHome}`);
    personArray.push(person);
    distanceArray.push(distanceFromHome);
  }
  // console.log(personArray);
  // console.log(distanceArray);
  return distanceArray;
}
/**
 * Finds the farthest distance.
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object.<String,Number[]>} locations - The object containing persons and their coordinates
 * @return {Array} The array containing the farthest person's name and their distance.
 */
function findFarthest(origin, locations) {
  let entryArray = Object.entries(locations);
  let personArray = [];
  let distanceArray = [];
  for ([person, coordinates] of entryArray) {
    distanceFromHome = findDistance(origin, coordinates);
    personArray.push(person);
    distanceArray.push(distanceFromHome);
  }

  let farthestDistance = 0;
  let i = 0;
  while (i < distanceArray.length) {
    if (distanceArray[i] > farthestDistance) {
      farthestPerson = personArray[i];
      farthestDistance = distanceArray[i];
    }
    i++;
  }

  console.log(
    `The longest distance from HOME is in ${farthestPerson} at ${farthestDistance}.`
  );
  return [farthestPerson, farthestDistance];
}

/**
 * Finds the nearest distance.
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object.<String,Number[]>} locations - The object containing persons and their coordinates
 * @return {Array} The array containing the nearest person's name and their distance.
 */
function findNearest(origin, locations) {
  entryArray = Object.entries(locations);
  let personArray = [];
  let distanceArray = [];
  for ([person, coordinates] of entryArray) {
    distanceFromHome = findDistance(origin, coordinates);
    personArray.push(person);
    distanceArray.push(distanceFromHome);
  }

  let nearestDistance = null;
  let i = 0;
  while (i < distanceArray.length) {
    if (i === 0) {
      nearestDistance = distanceArray[i];
    } else if (distanceArray[i] < nearestDistance) {
      nearestPerson = personArray[i];
      nearestDistance = distanceArray[i];
    }
    i++;
  }

  console.log(
    `The nearest distance from HOME is in ${nearestPerson} at ${nearestDistance}.`
  );

  return [nearestPerson, nearestDistance];
}
/**
 * The main function.
 */
function main() {
  findFarthest(HOME, locationObject);
  findNearest(HOME, locationObject);

  console.log(`\n--- All locations away from HOME ---\n`);

  distanceArray = processMap(HOME, locationObject);
}

// Calls the main function.
main();
