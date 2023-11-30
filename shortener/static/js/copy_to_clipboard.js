let copyBtn = document.getElementById("copyBtn");

function copyShortenedUrl() {

    // Select the text field
    shortenedUrl.select();

    // Copy the text inside the text field
    navigator.clipboard.writeText(shortenedUrl.value);
    
}

copyBtn.addEventListener("click", (e)=>{
    e.preventDefault();
    copyShortenedUrl();
});