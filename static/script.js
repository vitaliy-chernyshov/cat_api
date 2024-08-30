function openModal(element) {
    let modal = document.getElementById("myModal");
    let modalImg = document.getElementById("img01");
    modal.style.display = "block";
    modalImg.src = element.src;
    modal.onclick = function () {
        closeModal();
    }
}

function closeModal() {
    let modal = document.getElementById("myModal");
    modal.style.display = "none";
}
