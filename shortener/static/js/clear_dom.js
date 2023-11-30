let clearBtn = document.getElementById("clearBtn");

clearBtn.addEventListener("click", (e)=>{
    e.preventDefault();
    fullUrlInput.value = "";
    shortenedUrl.value = "";
    fullUrlInput.style.border = "none";

});