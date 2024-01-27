var getlink = document.getElementsByClassName("imglink"); 
var dataOutput = {};
for (let links of getlink){for (let link of links.childNodes){try{if (link.tagName.toLowerCase() == "img") {dataOutput[link.getAttribute("src")]=link.getAttribute("alt").replace("<strong>","").replace("</strong>","")}}catch(e){}}}
// then we will get the Map.
console.log(JSON.stringify(dataOutput))