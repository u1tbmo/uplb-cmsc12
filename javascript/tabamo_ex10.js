/* Tabamo, Euan Jed S. | B-1L
Exercise 10 | November 21, 2023 */

// Global Variables
const HOME = [3, 4];
let peopleLocations = {
  Chelsea: [-3, 3],
  Ralph: [8, 9],
  Andrew: [6, 7],
  Dustin: [15, 12],
};
let peopleDistances = {};

/**
 * This function creates a distance object from an origin and a locations object.
 *
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object} locations - The object containing persons and their coordinates.
 * @return {Object} The object containing persons and their distances from the origin.
 */
function createDistanceObject(origin, locations) {
  let distanceObject = {};
  for ([personName, personCoordinate] of Object.entries(locations)) {
    distanceObject[personName] = findDistance(origin, personCoordinate);
  }
  return distanceObject;
}

/**
 * This function finds the distance between the origin and the point.
 *
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Number[]} point - The coordinates of the point.
 * @return {Number} The distance between the origin and the point.
 */
function findDistance(origin, point) {
  const x2 = origin[0];
  const y2 = origin[1];
  const x1 = point[0];
  const y1 = point[1];
  return Number(Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2).toFixed(3));
}

/**
 * This function collects and manages the specified origin array and all other coordinates.
 * It outputs all the locations away from home.
 *
 * @param {Object} distances - The object containing persons and their distances from the origin.
 * @return {Number[]} The array containing the distances of all locations away from home.
 */
function processMap(distances) {
  let distanceArray = [];
  for ([personName, personDistance] of Object.entries(distances)) {
    console.log(`${personName}'s distance from HOME: ${personDistance}`);
    distanceArray.push(personDistance);
  }
  return distanceArray;
}

/**
 * This function finds the farthest distance from the origin.
 *
 * @param {Object} distances - The object containing persons and their distances from the origin.
 */
function findFarthest(distances) {
  let farthestPerson = null;
  let farthestDistance = null;
  for ([personName, personDistance] of Object.entries(distances)) {
    if (farthestDistance === null || farthestDistance < personDistance) {
      farthestPerson = personName;
      farthestDistance = personDistance;
    }
  }
  console.log(
    `The farthest distance from HOME is at ${farthestPerson}'s with a distance of ${farthestDistance}.`
  );
}

function findNearest(distances) {
  let nearestPerson = null;
  let nearestDistance = null;
  for ([personName, personDistance] of Object.entries(distances)) {
    if (nearestDistance === null || nearestDistance > personDistance) {
      nearestPerson = personName;
      nearestDistance = personDistance;
    }
  }
  console.log(
    `The nearest distance from HOME is at ${nearestPerson}'s with a distance of ${nearestDistance}.`
  );
}

/**
 * The main function.
 */
function main() {
  peopleDistances = createDistanceObject(HOME, peopleLocations);
  findFarthest(peopleDistances);
  findNearest(peopleDistances);
  console.log(`\nAll locations away from HOME\n`);
  processMap(peopleDistances);
}
main();
