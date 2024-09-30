// JavaScript to handle the change of text on window resize
function adjustHomeLinkText() {
    const homeLink = document.getElementById('home-link');
    if (window.innerWidth < 600) {
        homeLink.textContent = 'AC';
    } else {
        homeLink.textContent = 'Ash Chan';
    }
}

// Adjust text on initial load
window.addEventListener('load', adjustHomeLinkText);

// Adjust text on window resize
window.addEventListener('resize', adjustHomeLinkText);

// JavaScript to handle the hamburger menu toggle
document.addEventListener('DOMContentLoaded', () => {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const navList = document.querySelector('.nav-list');

    hamburgerMenu.addEventListener('click', () => {
        navList.classList.toggle('show');
    });

    // JavaScript to show/hide LinkedIn badge on hover
    const linkedinLink = document.getElementById('linkedin-link');
    const linkedinBadge = document.getElementById('linkedin-badge');

    linkedinLink.addEventListener('mouseover', () => {
        linkedinBadge.style.display = 'block';
    });

    linkedinLink.addEventListener('mouseout', () => {
        linkedinBadge.style.display = 'none';
    });
});

// Initialize Bootstrap Carousel
document.addEventListener('DOMContentLoaded', () => {
    const myCarouselElement = document.querySelector('#carouselExampleInterval');
    const carousel = new bootstrap.Carousel(myCarouselElement, {
        interval: 5000,
        touch: true
    });
});

// JavaScript to hide navbar on scroll down and show on scroll up
let lastScrollTop = 0;
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop) {
        header.style.top = '-70px'; // Adjust according to your header's height
    } else {
        header.style.top = '0';
    }
    lastScrollTop = scrollTop;
});

document.addEventListener('DOMContentLoaded', () => {
    const projectContainer = document.getElementById('project-container');
    const projects = Array.from(document.querySelectorAll('.project'));
    const projectCount = projects.length;

    // Clone the projects to make them repeat
    projects.forEach(project => {
        const clone = project.cloneNode(true);
        projectContainer.appendChild(clone);
    });

    // Set the project count CSS variable
    projectContainer.style.setProperty('--project-count', projectCount);

    // Calculate the animation duration based on the width of the container
    const projectWidth = projects[0].offsetWidth;
    const totalWidth = projectWidth * projectCount;
    const animationDuration = (totalWidth / window.innerWidth) * 30; // Adjust the duration accordingly

    projectContainer.style.width = `calc(300px * ${projectCount * 2})`;
    projectContainer.style.animationDuration = `${animationDuration}s`;

    // Reset animation on iteration end
    projectContainer.addEventListener('animationiteration', () => {
        projectContainer.style.animationName = 'none';
        setTimeout(() => {
            projectContainer.style.animationName = 'scrollProjects';
        }, 10);
    });
});
