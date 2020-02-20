
function events(){
    document.getElementById("file").addEventListener("change", readFileAsString);    
    console.log("edded event");
}
function readFileAsString() {
    var files = this.files;
    if (files.length === 0) {
        console.log("No file is selected");
        return;
    }

    var reader = new FileReader();
    reader.onload = function(event) {
        console.log("File content:", event.target.result);
    };
    reader.readAsText(files[0]);
    console.log(reader);
}