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
AJAX Request to resize image
*/

function requestResize(){
    console.log("Button pressed!");
    console.log(image);

    var sizes = getCheckedSizes(); //["640 x 480", "800 x 600", "1024 x 768", "1280 x 1024", "1600 x 1200", "1680 x 1050", "1920 x 1200"]
    var formData = new FormData();
    if(formData){
        formData.append("image", image);
        formData.append("sizes", sizes);
    }

    for (var key of formData.entries()) {
        console.log(key[0] + ', ' + key[1]);
    }

    $.ajax({
        type:"POST",
        url:"/resize",
        data: formData,
        processData: false,
        contentType: false,
        success: function(content) {
            console.log(content)
            var urls = content.urls;
            var tableBody = document.getElementById("linksTableBody")
            tableBody.innerHTML = "";
            sizes = sizes.split(";")

            for(sizeIndex in sizes){
                var newRow = tableBody.insertRow(tableBody.rows.length);
                newRow.innerHTML = "<th>" + sizes[sizeIndex] + "</th><th>" + urls[sizeIndex] + "</th>"
            }
            //document.getElementById("sendImage").disabled = true;
        }
    });
}

function getCheckedSizes(){
    var ret = ""; //[];
    var sizeChecks = document.getElementsByClassName("sizes");

    for(check of sizeChecks){
        if(check.checked == true) ret += check.value + ";"
    }
    console.log(ret);
    return ret.slice(0, -1);
}