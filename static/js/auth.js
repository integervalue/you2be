function togglePasswordVisibility() {
  var passwordField = document.getElementById("password");
  if (passwordField.type === "password") {
    passwordField.type = "text"; //Make password visible
  } else {
    passwordField.type = "password";
  }
  var confirmPassField = document.getElementById("confirm_password");
  if (confirmPassField.type === "password") {
    confirmPassField.type = "text";
  } else {
    confirmPassField.type = "password";
  }
}

function validatePassword() {
  var passwordField = document.getElementById("password");
  var confirmField = document.getElementById("confirm_password");
  var errorField = document.getElementById("password_error");
  var registerButton = document.getElementById("register_button");

  if (passwordField.value !== confirmField.value) {
    errorField.innerHTML = "Passwords do not match"; //Set error message
    errorField.style.display = "flex"; //Make error div visible
    registerButton.disabled = true; //Don't let them register until passwords match
  } else {
    errorField.innerHTML = "";
    errorField.style.display = "none"; //Make error div invisible
    registerButton.disabled = false; //User can now click "register"
  }
}

//Event listener to validate the entered passwords on register page
var confirmField = document.getElementById("confirm_password");
confirmField.addEventListener("input", validatePassword);
