
function events(){
    document.getElementById("file").addEventListener("change", readFileAsString);    
    console.log("edded event");
}
function readFileAsString() {
    let files = this.files;
    if (files.length === 0) {
        console.log("No file is selected");
        return;
    }

    let reader = new FileReader();
    reader.onload = function(event) {
        console.log("File content:", event.target.result)
        let text = document.getElementById("filecontent")
        text.innerHTML = event.target.result

    };

    reader.readAsText(files[0]);

}