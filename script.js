const standart = document.getElementById("standartButton");

const standartplus = document.getElementById("standartplusButton");

const premium = document.getElementById("premiumButton");

standart.addEventListener("click", () => {
    window.location.href = "abo.html?abo=standard";
});

standartplus.addEventListener("click", () => {
    window.location.href = "abo.html?abo=standard-plus";
});

premium.addEventListener("click", () => {
    window.location.href = "abo.html?abo=premium";
});