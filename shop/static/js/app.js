const flashMessage = document.querySelector(".messages");

if (flashMessage) {
  setTimeout(() => {
    flashMessage.style.display = "none";
  }, 3000);
}

// Then/Catch
// const endpoint = '/posts/'

// fetch(endpoint)
//   .then(res => res.json())
//   .then(data => console.table(data))
//   .catch(err => console.log(err))


// Async Await
// async function fetchPosts() {
//   try {
//     const res = await fetch('/posts/')
//     const data = await res.json()
//     // console.log(data)
//     render(data)
//   } catch (ex) {
//     console.log(ex)
//   }
// }

// fetchPosts()


// Load more posts
const results = document.querySelector('.results')
const loadButton = document.querySelector('.load-btn')

async function render() {
  try {
    const res = await fetch('/posts/')
    const data = await res.json()

    if (res.ok) {
      loadButton.style.display = 'none'
    }

    const html = data.map((post) => `<li>${post.title}</li>`).join(' ')

    // for (let i ; i < data.length; i++) {
    //   `<li>${post[i].title}</li>`
    // }
    
    results.insertAdjacentHTML('afterbegin', html)
  } catch (ex) {
    console.log(ex)
  }
}


loadButton.addEventListener('click', render)












