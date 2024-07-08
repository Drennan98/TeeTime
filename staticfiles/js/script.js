const scrollTopButton = document.getElementById('scrollTopButton');

window.addEventListener('scroll', function() {
    if(this.window.scrollY > 300) {
        scrollTopButton.style.display = 'block';
    } else {
        scrollTopButton.style.display = 'none';
    }
});

scrollTopButton.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});