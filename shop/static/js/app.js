const flashMessage = document.querySelector(".messages");

if (flashMessage) {
  setTimeout(() => {
    flashMessage.style.display = "none";
  }, 3000);
}
