/**
 * This is my back to top button which makes it easy for users to go back to top of the page. 
 */

const scrollTopButton = document.getElementById('scrollTopButton');

window.addEventListener('scroll', function() {
    if(this.window.scrollY > 900) {
        scrollTopButton.style.display = 'block';
    } else {
        scrollTopButton.style.display = 'none';
    }
});

scrollTopButton.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});