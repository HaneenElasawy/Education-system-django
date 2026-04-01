document.addEventListener("DOMContentLoaded", function () {
    console.log("School System loaded successfully");

    const deleteLinks = document.querySelectorAll(".danger");

    deleteLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            const confirmed = confirm("Are you sure you want to delete this item?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function () {
            const btn = form.querySelector("button[type='submit']");
            if (btn) {
                btn.disabled = true;
                btn.innerText = "Saving...";
            }
        });
    });
});