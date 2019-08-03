
canvas = document.getElementById("canvas");
ctx = canvas.getContext("2d");
ctx.font = "italic 10pt Arial";
var circleXSize = 10;
var circleYSize = 10;

reader = new FileReader();
reader.onload = (e) => {
	nodes = JSON.parse(e.target.result);
	nodes.map( (node) => { node["is_visible"] = true;})
	
	nodes.map( (node) => {
		ctx.drawImage(green,node.x, node.y, circleXSize, circleYSize);
	})
}

var nodes = [];
var file = 0;
map = new Image();
map.src = "map.jpg";

green = new Image();
green.src = "green.png";

red = new Image();
red.src = "red.png";

const inputFile = document.getElementById("file");

inputFile.addEventListener('change', handleFile, false);

canvas.onclick = (e) => {
	
}

function handleFile() {
	file = this.files[0];
	reader.readAsText(file);
}

map.onload = function() {
	ctx.drawImage(map,0,0,1910,859);
}

