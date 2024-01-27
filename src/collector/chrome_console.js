
// Print info about Node.JS version
console.log(new Date() + ' | Using Node ' + process.version + ' version to run server');


// Setting up server.
const http = require('http');
const server = http.createServer();
const port = 4999;

// Needed for parsing URLs.
const url = require('url');

// Setting WebSockets
const WebSocket = require('ws');
const wss = new WebSocket.Server({ noServer: true, clientTracking: true });

// make this shit accessible via cmdline.
// Needed to generate player ids
//const uuidv4 = require('uuid/v4');
var Set = require("collections/set");
var mySet = new Set();
var readline = require('readline');
var state=true;
var index=0;
var rl = readline.createInterface(process.stdin, process.stdout);
rl.setPrompt('select> ');
rl.prompt();
rl.on('line', function(line) {
	try{
		if (state){
index=parseInt(line);
var inx=mySet.toArray().length
if (index<inx){
//var ws =myArr.toArray()[index];
		rl.setPrompt(index+'> ');
		state=false;
		rl.prompt();}else{console.log("total "+inx+" sessions");}}else{
			var ws =mySet.toArray()[index];
			ws.send(line);
state=true;
			rl.setPrompt('select> ');
    rl.prompt();
		}}catch(err){console.log(err);state=true;
			rl.setPrompt('select> ');
			rl.prompt();
		}
}).on('close',function(){
    process.exit(0);
});
// Websocket connection handler.
wss.on('connection', function connection(ws, request) {
  console.log(new Date() + ' | A new client is connected.');

  // Assign player Id to connected client.

  // Registering player with the session.
mySet.add(ws);
	var id = mySet.toArray().length;
	console.log("new session joined. now "+id+" sessions");
  // Sending confirm message to the connected client.
//  ws.send('print("hello world")');

  // Handle all messages from users.
  ws.on('message', function(msgStr) {
    console.log('Message Received: '+msgStr);
    // Send back the same message.
    // ws.send(msgStr);
  });

  // What to do when client disconnect?
  ws.on('close', function(connection) {
	  mySet.delete(ws);
	  var id = mySet.toArray().length;  
	  console.log("one session closed. now "+id+" sessions");
    console.log(new Date() + ' | Closing connection for a client.');
// remove element.
    // One of the clients has disconnected.
  });
});

// HTTP Server ==> WebSocket upgrade handling:
server.on('upgrade', function upgrade(request, socket, head) {

    console.log(new Date() + ' | Upgrading http connection to wss: url = '+request.url);

    // Parsing url from the request.
    var parsedUrl = url.parse(request.url, true, true);
    const pathname = parsedUrl.pathname

    console.log(new Date() + ' | Pathname = '+pathname);

    // If path is valid connect to the websocket.
    if (pathname === '/chrome_console') {
      wss.handleUpgrade(request, socket, head, function done(ws) {
console.log("add 1 upgraded.");
        wss.emit('connection', ws, request);
      });
    } else {
	    // no fucking destroy!
      socket.destroy();
    }
});

// On establishing port listener.
server.listen(port, function() {
    console.log(new Date() + ' | Server is listening on port ' + port);

    // Server is running.
});
