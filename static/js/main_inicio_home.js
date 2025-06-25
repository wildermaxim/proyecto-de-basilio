// Animación de fade-in al cargar elementos
document.addEventListener("DOMContentLoaded", () => {
    const elementos = document.querySelectorAll('.fade-in');
    elementos.forEach((el, i) => {
        setTimeout(() => {
            el.classList.add('visible');
        }, i * 150);
    });
});
document.addEventListener("DOMContentLoaded", () => {
    const mensaje = document.querySelector('.mensaje-exito');
    if (mensaje) {
        setTimeout(() => {
            mensaje.style.transition = "opacity 0.5s ease-out";
            mensaje.style.opacity = "0";
            setTimeout(() => mensaje.remove(), 500);
        }, 4000); // 4 segundos visible
    }
});

// Scroll suave para anclas internas
document.querySelectorAll('a[href^="#"]').forEach(ancla => {
    ancla.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// Confirmación en enlaces de eliminar
document.querySelectorAll('a[href*="eliminar"]').forEach(el => {
    el.addEventListener("click", function (e) {
        if (!confirm("¿Deseas eliminar este registro?")) {
            e.preventDefault();
        }
    });
});
