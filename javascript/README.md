# tabamo_ex10.js

A JavaScript program that will estimate the distance between two coordinate points.

## Code Explanation

### Global Variables

```js
// Global Variables
const HOME = [3, 4];
let peopleLocations = {
  Chelsea: [-3, 3],
  Ralph: [8, 9],
  Andrew: [6, 7],
  Dustin: [15, 12],
};
let peopleDistances = {};
```

1. `HOME` is a constant variable that holds the coordinates of the home location. This is the specified origin point.
2. `locationObject` is an object that holds the coordinates of each person's location.

   1. Each property is a string, the name of the person.
   2. The value of each property is an array of two numbers, the x and y coordinates of the person's location.

3. `peopleDistances` is an object that will hold the distance between each person's location and the home location.
   1. Each property is a string, the name of the person.
   2. The value of each property is a number, the distance between the person's location and the home location.

### Function: findDistance()

```js
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
```

1. `findDistance()` takes two parameters, `origin` and `point`, both of which are arrays of two numbers.
2. The function returns the distance between the origin and the point using the distance formula.

### Function: processMap()

```js
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
```

1. `processMap()` takes one parameter, `distances`, which is an object containing the distances between each person's location and the home location.

   1. Each property is a string, the name of the person.
   2. The value of each property is a number, the distance between the person's location and the home location.

2. The function outputs the distance between each person's location and the specified origin point.
3. The function returns an array containing the distances of all locations away from home.

### Function: findFarthest()

```js
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
```

1. `findFarthest()` takes one parameter, `distances`, which is an object containing the distances between each person's location and the home location.

   1. Each property is a string, the name of the person.
   2. The value of each property is a number, the distance between the person's location and the home location.

2. The function finds the farthest distance from the origin and outputs the person's name and distance.
   1. The function uses a for loop to iterate through each property in the `distances` object.
   2. If the `farthestDistance` variable is `null` or less than the current person's distance, the `farthestPerson` and `farthestDistance` variables are updated with the current person's name and distance.
   3. The function outputs the person's name and distance.
   4. The function returns nothing.

### Function: findNearest()

```js
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
```

1. `findNearest()` takes one parameter, `distances`, which is an object containing the distances between each person's location and the home location.

   1. Each property is a string, the name of the person.
   2. The value of each property is a number, the distance between the person's location and the home location.

2. The function finds the nearest distance from the origin and outputs the person's name and distance.
   1. The function uses a for loop to iterate through each property in the `distances` object.
   2. If the `nearestDistance` variable is `null` or greater than the current person's distance, the `nearestPerson` and `nearestDistance` variables are updated with the current person's name and distance.
   3. The function outputs the person's name and distance.
   4. The function returns nothing.

### Function: main()

```js
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
```

1. This function is the main function of the program.
2. It is called at the end of the program.
