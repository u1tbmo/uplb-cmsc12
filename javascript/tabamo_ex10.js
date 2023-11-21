/* Tabamo, Euan Jed S. | B-1L
Exercise 10 | November 21, 2023 */

// Global Variables
const HOME = [3, 4];
let locationObject = {
  Chelsea: [-3, 3],
  Ralph: [8, 9],
  Andrew: [6, 7],
  Dustin: [15, 12],
};

/**
 * This function finds the distance between the origin and the point.
 *
 * @param {number[]} origin - The coordinates of the origin point.
 * @param {number[]} point - The coordinates of the point.
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
 * This function produces the person array and the distance array from an origin and a locations object.
 *
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object} locations - The object containing persons and their coordinates.
 * @return {Array[]} The array containing the person array and the distance array.
 */
function getPersonAndDistanceArrays(origin, locations) {
  let personArray = [];
  let distanceArray = [];
  for (const [person, coords] of Object.entries(locations)) {
    personArray.push(person);
    distanceArray.push(findDistance(origin, coords));
  }
  return [personArray, distanceArray];
}

/**
 * This function collects and manages the specified origin array and all other coordinates.
 * It also outputs all the locations away from home.
 *
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object} locations - The object containing persons and their coordinates.
 * @return {Number[]} The array containing the distances of all locations away from home.
 */
function processMap(origin, locations) {
  const [personArray, distanceArray] = getPersonAndDistanceArrays(
    origin,
    locations
  );
  for (let i = 0; i < personArray.length; i++) {
    console.log(`${personArray[i]}'s distance from HOME: ${distanceArray[i]}`);
  }
  return distanceArray;
}

/**
 * This function finds the farthest distance from the origin.
 * It also outputs the farthest person and their distance.
 * It also returns the array containing the farthest person's name and their distance.
 *
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object} locations - The object containing persons and their coordinates.
 */
function findFarthest(origin, locations) {
  const [personArray, distanceArray] = getPersonAndDistanceArrays(
    origin,
    locations
  );
  let farthestPerson = personArray[0];
  let farthestDistance = distanceArray[0];
  for (let i = 1; i < Object.keys(locations).length; i++) {
    if (distanceArray[i] > farthestDistance) {
      [farthestPerson, farthestDistance] = [personArray[i], distanceArray[i]];
    }
  }
  console.log(
    `The longest distance from home is in ${farthestPerson}'s at ${farthestDistance} units.`
  );
}

/**
 * This function finds the nearest distance from the origin.
 * It also outputs the nearest person and their distance.
 * It also returns the array containing the nearest person's name and their distance.
 *
 * @param {Number[]} origin - The coordinates of the origin point.
 * @param {Object} locations - The object containing persons and their coordinates.
 */
function findNearest(origin, locations) {
  const [personArray, distanceArray] = getPersonAndDistanceArrays(
    origin,
    locations
  );
  let nearestPerson = personArray[0];
  let nearestDistance = distanceArray[0];
  for (let i = 1; i < Object.keys(locations).length; i++) {
    if (distanceArray[i] < nearestDistance) {
      [nearestPerson, nearestDistance] = [personArray[i], distanceArray[i]];
    }
  }
  console.log(
    `The shortest distance from home is in ${nearestPerson}'s at ${nearestDistance} units.`
  );
}

/**
 * The main function.
 */
function main() {
  findFarthest(HOME, locationObject);
  findNearest(HOME, locationObject);
  console.log(`\nAll locations away from HOME\n`);
  processMap(HOME, locationObject);
}

main();
