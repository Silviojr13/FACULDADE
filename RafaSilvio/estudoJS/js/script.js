const themeStyle = document.getElementById('theme-style');
const themeToggle = document.getElementById('theme-toggle');

let isDarkMode = false;

themeToggle.addEventListener('click', () => {
  isDarkMode = !isDarkMode;
  
  if (isDarkMode) {
    themeStyle.textContent = `
      body {
        background-color: #333; /* Cor de fundo escura */
        color: #fff; /* Cor do texto em modo escuro */
      }
    `;
  } else {
    themeStyle.textContent = `
      body {
        background-color: #fff; /* Cor de fundo padrão */
        color: #000; /* Cor do texto em modo claro */
      }
    `;
  }
});
