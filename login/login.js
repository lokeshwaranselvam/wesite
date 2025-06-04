function toggleForm() {
  const formSlider = document.querySelector(".form-slider");
  formSlider.classList.toggle("show-signup");
}

// LOGIN
function login() {
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  fetch("http://localhost:3000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  })
    .then(res => res.json())
    .then(data => {
      const msg = document.getElementById("loginMessage");
      msg.textContent = data.message;
      msg.style.color = data.success ? "green" : "red";
      if (data.success) {
        setTimeout(() => {
          window.location.href = "/landpage";
        }, 1000);
      }
    });
}

// SIGNUP
function signup() {
  const username = document.getElementById("newUsername").value.trim();
  const email = document.getElementById("newEmail").value.trim();
  const password = document.getElementById("newPassword").value.trim();
  const confirmPassword = document.getElementById("confirmPassword").value.trim();

  const msg = document.getElementById("signupMessage");

  if (password !== confirmPassword) {
    msg.textContent = "Passwords do not match";
    msg.style.color = "red";
    return;
  }

  fetch("http://localhost:3000/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email, password })
  })
    .then(res => res.json())
    .then(data => {
      msg.textContent = data.message;
      msg.style.color = data.success ? "green" : "red";
      if (data.success) {
        setTimeout(() => toggleForm(), 1500);
      }
    });
}
