// Function to initialize tooltips
function initializeTooltips() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Function to initialize modals
function initializeModals() {
    var modalTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="modal"]'));
    var modalList = modalTriggerList.map(function (modalTriggerEl) {
        return new bootstrap.Modal(modalTriggerEl);
    });
}

// Attach event listeners for non-critical UI elements
document.addEventListener('DOMContentLoaded', function() {
    initializeTooltips();
    initializeModals();
});