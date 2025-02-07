const icons = document.querySelectorAll(".icon");
const optionContainers = document.querySelectorAll(".option-container");

icons.forEach((icon, index) => {
    icon.addEventListener("click", (evt) => {
        evt.stopPropagation()

        optionContainers.forEach(container => {
            container.style.display = "none";
        });

        optionContainers[index].style.display = "block";
    });
});

window.addEventListener("click", () => {
    optionContainers.forEach((container) => {
        if (container.style.display == "block") container.style.display = "none";
    })
})

const deleteButtons = document.querySelectorAll(".button-delete");
const deleteBackgrounds = document.querySelectorAll(".delete-background");

deleteButtons.forEach((button, index) => {
    button.addEventListener("click", (e) => {
        e.stopPropagation();

        deleteBackgrounds[index].style.display = "flex";
    })
})


const deleteNot = document.querySelectorAll('.button-not');

deleteNot.forEach((button, index) => {
    button.addEventListener("click", (e) => {
        e.stopPropagation();

        deleteBackgrounds[index].style.display = "none";
    })
})