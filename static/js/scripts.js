document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll("input");

    // Efecto visual al enfocar
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.borderColor = "#cc0000";
        });
        input.addEventListener("blur", () => {
            input.style.borderColor = "#ccc";
        });
    });

    // Mostrar mensaje temporal si existe
    const mensaje = document.querySelector(".mensaje-exito");
    if (mensaje) {
        setTimeout(() => {
            mensaje.style.display = "none";
        }, 4000); // 4 segundos
    }
});
