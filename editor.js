
canvas = document.getElementById("canvas");
ctx = canvas.getContext("2d");
ctx.font = "italic 10pt Arial";
var file;
var nodes = {
	nodes_list : null,
	nodes_list_init : function() {
		let id = 0;
		this.nodes_list.map( (node) => {
			node.is_visible = true;
			node.id = id; id += 1;
		});
	},
	move_from_to: {
		from: null,
		to: null,
		node_id: null
	},
	is_click_on_node: function(x,y) {
		x = x - 5;
		y = y - 5;
		let x1 = x - 5;
		let x2 = x + 5;
		let y1 = y - 5;
		let y2 = y + 5;
		
		this.nodes_list.forEach( (node) => {
			if ( (node.x >= x1) && (node.y >= y1) && (node.x <= x2) && (node.y <= y2)) {
				alert(node.name);
				return true;
			}
		});
		
	},
	is_moving: false,
	show_nodes: function() {
		this.nodes_list.map( (node) => {
			if (node.is_visible) {
				ctx.drawImage(green,node.x, node.y, c_x, c_y);
			}
		})
	},
	
	
};
var c_x = 10;
var c_y = 10;
var move_from_to = {from : 0, to: 0, node_id:-1};

reader = new FileReader();
reader.onload = (e) => {
	nodes.nodes_list = JSON.parse(e.target.result);
	nodes.nodes_list_init()
	nodes.show_nodes()	
}


map = new Image();
map.src = "map.jpg";

green = new Image();
green.src = "green.png";

red = new Image();
red.src = "red.png";

const inputFile = document.getElementById("file");

inputFile.addEventListener('change', handleFile, false);

canvas.onclick = (e) => {
	nodes.is_click_on_node(e.layerX, e.layerY);
}
canvas.ondblclick = (e) => {
	ctx.drawImage(green,e.layerX-c_x/2, e.layerY-c_y/2,c_x,c_y);
}

canvas.onmousemove = (e) => {
	
}
function handleFile() {
	file = this.files[0];
	reader.readAsText(file);
}

map.onload = function() {
	ctx.drawImage(map,0,0,1910,859);
}

