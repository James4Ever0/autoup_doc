const {electron} = require ('electron')
// const args = electron.process.argv
// including 2 extras.
// console.log(process.argv)
var pargs = process.argv;
pargs.shift();
pargs.shift();
console.log(pargs);