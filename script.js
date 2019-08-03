ctx = document.getElementById("canvas").getContext("2d");
ctx.font = "italic 10pt Arial";
map = new Image();
map.src = "map.jpg";

green = new Image();
green.src = "green.png";

red = new Image();
red.src = "red.png";

document.onclick = (e) => {
	ctx.drawImage(green,e.clientX, e.clientY,10,10);
	ctx.drawImage(red,e.clientX+100, e.clientY,10,10);
}
map.onload = function() {
	ctx.drawImage(map,0,0,1910,859);
}

