var args = process.argv;
args.shift()
args.shift()
function print_help(){console.log("command format: (-bv2av <bv>)|(-av2bv <av>)");}
if (args.length!==2){print_help();}
else {
if (args[0] == "-bv2av"){}
	else if (args[0] == "-av2bv"){}
	else{print_help()}
}
