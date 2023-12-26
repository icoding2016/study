function add(x, y) {  return x + y  }
let multiply = function (x, y) {  return x * y  }
let square = (x) => x * x

exports.divide = (x,y) => x/y    // funtion exporting method 1

module.exports = { add, multiply, square }    // funtion exporting method 2