(function () {
  const root = document.documentElement;
  const saved = localStorage.getItem("book-theme");
  if (saved) root.setAttribute("data-theme", saved);
  const btn = document.querySelector("[data-theme-toggle]");
  function label() {
    const dark = root.getAttribute("data-theme") === "dark";
    if (btn) btn.textContent = dark ? "Light" : "Dark";
  }
  label();
  if (btn) {
    btn.addEventListener("click", function () {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("book-theme", next);
      label();
    });
  }
})();
