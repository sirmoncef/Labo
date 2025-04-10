let logo=document.querySelector(".logo")
let bar=document.querySelector(".bar")
let header=document.querySelector("header .container")
logo.addEventListener("click",()=>{
    bar.classList.toggle("active")
let timeOut=setTimeout(()=>{
    if (header.classList.contains("active")){
       let timeIn=setTimeout(()=>{
         bar.style.cssText = "display: block;"
        clearTimeout(timeIn)
        },250)

    }else{
        bar.style.cssText = "display: none;"
    }
    header.classList.toggle("active")
    clearTimeout(timeOut)
},250)
console.log("f")
})
//------------------------------------------------------------------------------
let filter = document.querySelector(".filter");
let form = document.querySelector(".form-container");
let login=document.querySelector("header .bar li:last-child");


filter.addEventListener("click", () => {
    filter.classList.toggle("active");
    form.classList.toggle("active");

});

login.onclick=()=>{
    filter.classList.toggle("active");
    form.classList.toggle("active");
}