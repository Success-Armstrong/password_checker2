function checkPasswordStrength(password) {
    const meter = document.getElementById('strength-meter');
    const suggestions = document.getElementById('suggestions-list');

    let strength = 0;
    let suggestionList = [];

    if (password.length >= 8) strength++;
    else suggestionList.push("Use at least 8 characters");

    if (/[0-9]/.test(password)) strength++;
    else suggestionList.push("Add numbers");

    if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) strength++;
    else suggestionList.push("Add special characters");

    if (/[A-Z]/.test(password)) strength++;
    else suggestionList.push("Use uppercase letters");

    if (/[a-z]/.test(password)) strength++;
    else suggestionList.push("Use lowercase letters");

    // Strength label
    let label = "";
    if (strength <= 2) {
        label = "<span style='color:red;'>Weak</span>";
    } else if (strength === 3 || strength === 4) {
        label = "<span style='color:orange;'>Medium</span>";
    } else {
        label = "<span style='color:green;'>Strong</span>";
    }

    meter.innerHTML = "Strength: " + label;

    // Show suggestions
    suggestions.innerHTML = "";
    suggestionList.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        suggestions.appendChild(li);
    });
}

// Optional: block submission if password is still weak
function validateBeforeSubmit() {
    const password = document.getElementById('password').value;
    if (password.length < 6) {
        alert("Password is too short!");
        return false;
    }
    return true;
}

function toggleDarkMode() {
    const body = document.body;
    const currentTheme = body.classList.contains("dark");

    if (currentTheme) {
        body.classList.remove("dark");
        localStorage.setItem("theme", "light");
    } else {
        body.classList.add("dark");
        localStorage.setItem("theme", "dark");
    }
}

// Load the last saved theme on page load
window.onload = function () {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark");
    }
};
