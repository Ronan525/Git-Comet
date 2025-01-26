// Function to show the update form
function showUpdateForm() {
    document.getElementById('post-content').style.display = 'none';
    document.getElementById('update-form').style.display = 'block';
}

// Function to hide the update form
function hideUpdateForm() {
    document.getElementById('post-content').style.display = 'block';
    document.getElementById('update-form').style.display = 'none';
}

// Attach event listeners for critical UI elements
document.addEventListener('DOMContentLoaded', function() {
    // Example: Attach event listeners to buttons
    document.querySelectorAll('.btn-warning').forEach(function(button) {
        button.addEventListener('click', showUpdateForm);
    });

    document.querySelectorAll('.btn-secondary').forEach(function(button) {
        button.addEventListener('click', hideUpdateForm);
    });
});