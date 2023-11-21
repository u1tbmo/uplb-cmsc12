/* Tabamo, Euan Jed S. | B-1L
Exercise 10 | November 21, 2023 */

const HOME = [3, 4];
let locationObject = {
  Chelsea: [-3, 3],
  Ralph: [8, 9],
  Andrew: [6, 7],
  Dustin: [15, 12],
};
let distanceArray = [];

function findDistance(origin, point) {
  let x2 = origin[0];
  let y2 = origin[1];
  let x1 = point[0];
  let y1 = point[1];
  return Number(Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2).toFixed(3));
}
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

function main() {
  findFarthest(HOME, locationObject);
  findNearest(HOME, locationObject);

  console.log(`\n--- All locations away from HOME ---\n`);

  distanceArray = processMap(HOME, locationObject);
}

main();
