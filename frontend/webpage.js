
var text = "";
var currImageUrl;
async function onLoad() {
    
    var name = document.getElementById("username").value;
    var proj = document.getElementById("proj").value;
    var org = document.getElementById("org").value;
    var key = document.getElementById("openaikey").value;

    try {

        data = {
            name: name,
            proj: proj,
            org: org,
            key: key,
        }

        const response = await fetch("http://127.0.0.1:8080/onLoad/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch response from server");
        }

        const reply = await response.text();
        updateText(reply);
        sessionStorage.setItem("onLoadExecuted", "true");

    } catch (error) {
        console.error("Error fetching response:", error);
    }
}

function updateText(t) {
    const extractedText = t.split("*")[0].trim();
    text = extractedText;
    document.getElementById('hinaText').textContent=text;
}

function setCurrentUrlImage(imgUrl) {
    currImageUrl = imgUrl;
}

function updateImage(imgUrl){
    const imageElement = document.getElementById('background_img');
    if (imageElement) {
        imageElement.src = imgUrl;
    } else {
        console.warn("⚠️ Image element not found!");
    }
}

async function submitForm(e) {
    e.preventDefault();

    var prompt = document.getElementById("reply").value;
    const data = {
        reply: prompt
    }

    try {
        const response = await fetch("http://127.0.0.1:8080/generate_response/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`text Failed to fetch response from /generate_response/: ${response.status} ${response.statusText}`);
        }

        const reply = await response.text();
        const res = clean_prompt_for_sd(reply)

        const resp = await fetch("http://127.0.0.1:8080/generate_image/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: res }),
        });

        if (!resp.ok) {
            throw new Error(`image Failed to fetch response from /generate_image/: ${resp.status} ${resp.statusText}`);
        }

        const imageBlob = await resp.blob();
        const imageObjectURL = URL.createObjectURL(imageBlob);    
        
        setCurrentUrlImage(imageObjectURL);
        updateImage(imageObjectURL);
        updateText(reply);

    } catch (error) {
        console.error("Error fetching response:", error);
    }
}


function clean_prompt_for_sd(p) {
    const match = p.match(/\*(.*?)\*/);
    const extracted_prompt = match[1].trim();
    return extracted_prompt;
}


document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggleButton");
    const textbox = document.getElementById("textbox");
    const buttonBackground = document.querySelector(".buttonbackground");
    const download = document.getElementById("downloadButton");

    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", submitForm);
    }

    const popupOverlay = document.getElementById("popupOverlay");
    const popupSubmit = document.getElementById("popupSubmit");

    popupOverlay.classList.add("active");

    popupSubmit.addEventListener("click", function (e) {
        e.preventDefault()
        onLoad()
        popupOverlay.classList.remove("active");
    });

    document.getElementById("downloadButton").onclick = () => {
        const link = document.createElement("a");
        link.href = currImageUrl;
        link.download = "generated_image.png";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(imageObjectURL);
    };

    toggleButton.addEventListener("click", (event) => {
        event.stopPropagation();
        textbox.classList.add("hidden");
        toggleButton.style.display = "none";
        buttonBackground.style.display = "none";
        download.style.display = "none";

    });

    document.addEventListener("click", () => {
        textbox.classList.remove("hidden");
        toggleButton.style.display = "block";
        buttonBackground.style.display = "flex";
        download.style.display = "block";

    });

    textbox.addEventListener("click", (event) => {
        event.stopPropagation();
    });

});
