/* HAMBURGUER MENU */

const hamburger = document.querySelector(".hamburger-container");
const menu = document.querySelector(".menu");
const menuItem = document.querySelectorAll("menu-item")

hamburger.addEventListener('click', () => {
    menu.classList.toggle("open")
})

/* PORTFOLIO GALLERY */

galleries = document.getElementsByClassName("amindsight-portfolio-container")

/* HIDE ALL GALLERIES BUT THE FIRST AT START */

for (i=0; i<galleries.length; i++) {  
  if (galleries[i].id != "1"){
    $("#"+galleries[i].id).hide()
  }
}

/* SELECT GALLERY FROM INDEX */

$(".p-index-btn").click(function() {
  $(".amindsight-portfolio-container").hide()
  galleryId = this.id.replace("index", "#")
  $(galleryId).show()
});
