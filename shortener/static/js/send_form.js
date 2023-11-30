let form = document.getElementById("form");
let data = null;
let fullUrlInput = form[1];

async function getShortenedURL(full_url){
    const response = await fetch("http://localhost:8000/generate-short-url/", {
        method:"POST",
        headers:{
            "Content-type":"application/json",
            "X-CSRFToken": csrftoken
        },
        mode: "same-origin",
        body:JSON.stringify({url:full_url})

    });

    const data = await response.json();
    return data;
}

form.addEventListener("submit", async (e)=>{
    e.preventDefault();
    fullUrlInput.style.border = "none";
    data = await getShortenedURL(fullUrlInput.value);
    domPrinter(data);
});