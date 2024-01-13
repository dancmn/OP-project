window.addEventListener('DOMContentLoaded', function () {
  const buttons = Array.from(document.querySelectorAll('button[id]'))
  console.log(buttons)
  for (let button of buttons) {
    console.log(button.id.slice(6))
    button.addEventListener('click', (event) => {
      fetch('http://localhost:8000/join/', {
        body: JSON.stringify({
          id: button.id.slice(6),
        }),
        method: "POST"
      })
    })
  }
});