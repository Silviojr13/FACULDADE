document.addEventListener("DOMContentLoaded", function () {
    fetch("/html_import/menu.html")
      .then(response => response.text())
      .then(data => {
        const menuPlaceholder = document.getElementById("menu-placeholder");
        menuPlaceholder.innerHTML = data;
      })
      .catch(error => {
        console.error("Erro ao carregar o menu:", error);
      });
  });