let images = document.querySelectorAll(".landing .cont")
let count = images.length
let slideCounter = 1
let indicators = document.querySelectorAll(".landing .indicators div")
setInterval(function() {
    slideCounter++
    if (slideCounter == 4) {
        slideCounter = 1
        check()
    } else {
        check()
    }
}, 3000)
let check = function() {
    remove()
    images[slideCounter - 1].classList.add("active")
    indicators[slideCounter - 1].classList.add("active")
}
let remove = function() {
    images.forEach((e) => {
        e.classList.remove("active")
    })
    indicators.forEach((e) => {
        e.classList.remove("active")
    })
}
check()
for (let i = 0; i < count; i++) {
    indicators[i].onclick = function() {
        slideCounter = i + 1
        check()
    }
}


let btn = document.querySelectorAll(".service .box button")
btn[0].onclick = () => {
    window.location.href = "./laboP2.html"
}
btn[1].onclick = () => {
    window.location.href = "./laboP3.html"
}
btn[2].onclick = () => {
        window.location.href = "./laboP4.html"
    }

    