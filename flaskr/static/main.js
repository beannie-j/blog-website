$(document).ready(function () {
    $(".nav-link").removeClass("active");
    let current = location.pathname;
    if (current == '/') $('.about').addClass('active')
    if (current == '/projects') $('.projects').addClass('active')
    if (current == '/contact') $('.contact').addClass('active')
});

window.onload = function() {
    const downloadCVButton = document.getElementById("download-cv-button");
    downloadCVButton.onclick = function() {
        let pdf = './media/Jeannie_AN_CV.pdf';
        window.open(pdf);
    }
}




