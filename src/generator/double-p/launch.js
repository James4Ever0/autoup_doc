const electron = require('electron')
const createVideoRecorder = require('electron-recorder')
const fs = require("fs");
try{
fs.mkdir("outputs",(_)=>{})
}catch(e){}
var pargs = process.argv;
pargs.shift();
pargs.shift();

const app = electron.app // electron module
const BrowserWindow = electron.BrowserWindow //enables UI
const fileurl = "file:///root/AGI/AutoUP/generator/double-p/double-pendulum/index.html"
//const fileurl = "https://www.baidu.com"

app.on("ready", _ => {
	// what's wrong with the fucking fan?
const width = 1500;
const height = 1500;
	// not divisible by 2?
	// use xvfb.
	const fps=60;
    win = new BrowserWindow({
        width: width,
        height: height,
        show: true,
	    frame: false
    })
      win.setSize(width,height)
win.loadURL(fileurl);
      // Here we create recorder object
      const video = createVideoRecorder(win, {
        fps: fps,
        output: "outputs/"+Date.now()+'_pendulum.mp4'
      })

      let frameCount = fps*60*10;
      async function renderFrame () {
	      console.log(frameCount);
	      frameCount -=1;
        if (frameCount > 0) {
	setTimeout(()=>{renderFrame();},Math.floor(1000/fps));
          video.frame()
		// what the fuck?
        } else {
          // Otherwise, movie is over and we save the snapshot to file
await video.end()
		console.log("=================video end.===================")
//		console.log("vlog:",video.log);
//		then(()=>{
          win.close()
		app.quit()
	//})
        }
      }
	var contents = win.webContents;
win.webContents.on('did-stop-loading', () => {
	contents.insertCSS('html,body{ overflow: hidden !important; }');
//	win.blur()
	console.log("did-stop-loading");
//	console.dir(contents);
//	console.dir(win);
/*	setInterval(()=>{
contents.capturePage().then((image)=>{console.log(image);})
	},500);*/
      renderFrame()

})
})
