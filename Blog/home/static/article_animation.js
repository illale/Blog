function load() {
	let elem = document.getElementById("id1");
	elem.addEventListener("onClick", showHidden, false);

}
function showHidden(id) {
	if (id === "id123") {
		console.log("AbC");
		event.stopPropagation();
		return;
	}
	if (id != "id1") {
		document.getElementById("id1").style.display = "block";
		let inter = setInterval(frame, 5);
		let top = 100;
		function frame() {
			if (top == 0) {
				clearInterval(inter);
			} else {
				top -= 10;
				document.getElementById("id1").style.top = top + "%";
			}
		}
	} else {
		document.getElementById("id1").style.display = "none";
	}
}
