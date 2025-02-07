const barra = document.querySelector(".bar-icon")
const navbar = document.querySelector(".navbar")

barra.addEventListener("click", () => {
    if (navbar.style.display == "block"){
        navbar.style.display = "none"
    }else{
        navbar.style.display = "block"
    }
    
})