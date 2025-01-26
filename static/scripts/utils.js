function toggleNav() {
  const hamburgerBtn = document.getElementById("hamburger-btn");
  const navList = document.getElementById("nav-list");

  hamburgerBtn.addEventListener("click", () => {
    navList.classList.toggle("nav-open");
  });
}

window.addEventListener("DOMContentLoaded", toggleNav);
