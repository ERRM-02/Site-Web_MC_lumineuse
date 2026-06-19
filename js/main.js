const toggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

if (toggle && navLinks) {
    toggle.addEventListener("click", () => {
        const open = navLinks.classList.toggle("open");
        toggle.setAttribute("aria-expanded", String(open));
    });

    navLinks.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("open");
            toggle.setAttribute("aria-expanded", "false");
        });
    });
}

const navbar = document.querySelector(".navbar");

if (navbar) {
    const updateNavbar = () => {
        navbar.classList.toggle("is-scrolled", window.scrollY > 20);
    };

    updateNavbar();
    window.addEventListener("scroll", updateNavbar, { passive: true });
}

const lightbox = document.querySelector(".lightbox");
const lightboxImg = document.querySelector(".lightbox-img");
const lightboxClose = document.querySelector(".lightbox-close");

if (lightbox && lightboxImg) {
    document.querySelectorAll("[data-lightbox]").forEach((item) => {
        item.addEventListener("click", () => {
            lightboxImg.src = item.getAttribute("data-lightbox");
            lightbox.classList.add("active");
            lightbox.setAttribute("aria-hidden", "false");
            document.body.style.overflow = "hidden";
        });
    });

    const closeLightbox = () => {
        lightbox.classList.remove("active");
        lightbox.setAttribute("aria-hidden", "true");
        lightboxImg.src = "";
        document.body.style.overflow = "";
    };

    lightbox.addEventListener("click", (event) => {
        if (event.target === lightbox) closeLightbox();
    });

    if (lightboxClose) {
        lightboxClose.addEventListener("click", closeLightbox);
    }

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") closeLightbox();
    });
}
