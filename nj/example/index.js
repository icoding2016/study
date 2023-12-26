const fs = require('fs')
const path = require('path')

const fn_r = path.join(__dirname, 'data', 'example_r.txt')
const fn_w = path.join(__dirname, 'data', 'example_w.txt')
const fn_a = path.join(__dirname, 'data', 'example_a.txt')


console.log(`file name: ${fn_r}`)

fs.readFile(fn_r, (err, data) => {
    if (err)  throw err;
    console.log(data);
})

fs.readFile(fn_r, (err, data) => {
    if (err)  throw err;
    console.log(data.toString());
})

fs.readFile(fn_r, 'utf8', (err, data) => {
    if (err)  throw err;
    console.log(data);
})

console.log('>> This appears before the file content, because the file read is ansync...')


// fs.readFile('./data/not_exist', 'utf8', (err, data) => {
//     if (err)  throw err;
//     console.log(data);
// })



fs.writeFile(fn_w, 'Test writting to file.', (err) => {
    if (err)  throw err;
    console.log(`Write file ${fn_w} finished.`)
})


fs.appendFile(fn_a, 'Test appending file.\n', (err) => {
    if (err)  throw err;
    console.log(`Append file ${fn_a} finished.`)
})




process.on('uncaughtException', err => {
    console.error('Uncaught err:', err);
    process.exit(1)
})

