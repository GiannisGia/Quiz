function setBackgroundImage(imageUrl) {
    document.body.style.backgroundImage = `url('${imageUrl}')`;
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundRepeat = 'no-repeat';
}

// Set background image when the page loads
window.onload = function() {
    setBackgroundImage('C:\\Users\\johng\\OneDrive\\Υπολογιστής\\Quiz\\static\\Backround.jpg')
}