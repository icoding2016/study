
console.log('Hi~')
console.log(global)


const os = require('os')
const path = require('path')
const mymath = require('./mymath')
const {add, multiply, square} = require('./mymath')   // another way to import

console.log(os.hostname())
console.log(os.type())
console.log(os.version())
console.log(os.homedir())

console.log(__dirname, ', ', __filename)
console.log(path.basename(__filename), ', ', path.extname(__filename))
console.log(path.parse(__filename))

console.log('----------------------')

// functions

console.log(add(1,2))
console.log(multiply(2,3))
console.log(square(10))

