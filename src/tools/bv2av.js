var args = process.argv;

var table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF',
  tr = {};
for (var i = 0; i < 58; i++) {
  tr[table[i]] = i;
}
var s = [11, 10, 3, 8, 4, 6],
  xor = 177451812,
  add = 8728348608;

function bv2av(x) {
  var r = 0;
  for (var i = 0; i < 6; i++) {
    r += tr[x[s[i]]] * 58 ** i;
  }
  return (r - add) ^ xor;
}

function av2bv(x) {
  x = (x ^ xor) + add;
  r = 'BV1  4 1 7  '.split('');
  for (var i = 0; i < 6; i++) {
    r[s[i]] = table[Math.floor(x / 58 ** i) % 58];
  }
  return r.join('');
}

function bvUrl2AvUrl(url) {
  return url.replace(/\/video\/(BV([a-zA-Z0-9]+))/, function (str, bv) {
    var avCode = bv2av(bv);
    return str.replace(bv, 'av' + avCode);
  });
}
args.shift()
args.shift()
function print_help(){console.log("command format: (-bv2av BV<remainder>)|(-av2bv av<remainder>)");}
if (args.length!==2){print_help();}
else {
if (args[0] == "-bv2av"){if (args[1].startsWith("BV")){console.log("av"+bv2av(args[1]))}else{print_help();}}
	else if (args[0] == "-av2bv"){if (args[1].startsWith("av")){console.log(av2bv(args[1].substring(2,args[1].length)))}else{print_help()}}
	else{print_help()}
}
