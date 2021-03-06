// Main Functions

var fileInput = document.getElementById("inputImage");
var image;

fileInput.addEventListener('change', function() {
    if(fileInput.files.length != 0){
        document.getElementById("sendImage").disabled = false;
        image = fileInput.files[0];
        console.log(image);
    }
    else console.log("Empty")
}, false);

/*
AJAX Request to classify image through Google Cloud API
*/

function labelImage(){
    console.log("Button pressed!");
    console.log(image);

    var formData = new FormData();
    if(formData){
        formData.append("image", image);
    }

    for (var key of formData.entries()) {
        console.log(key[0] + ', ' + key[1]);
    }

    $.ajax({
        type:"POST",
        url:"/classify",
        data: formData,
        processData: false,
        contentType: false,
        success: function(content) {
            console.log(content)
            let response = content.image_categories
            alert("Image succesfully uploaded!")
            //var urls = content.urls;
            //var tableBody = document.getElementById("linksTableBody")
            //tableBody.innerHTML = "";
            //document.getElementById("sendImage").disabled = true;
        }
    });
}