let shortenedUrl = document.getElementById("shortenedUrl");

function domPrinter(output) {

    if ("error_message" in output) {
        fullUrlInput.style.border = "2px solid red";
        fullUrlInput.value = output["message"];
    }
    else if ("shortened_url" in output){
        shortenedUrl.value = output['shortened_url'];
    }
    
}