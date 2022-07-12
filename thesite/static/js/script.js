window.addEventListener('touchstart', function(event){
  var box = document.getElementById('ul-li-ul');
  if (event.target != box && event.target.parentNode != box) {
    box.style.display = 'none';
  }
});
/*
let aboutLink = document.querySelector('#about_link');
let aboutItem = document.querySelector('#aboutItem');

aboutLink.addEventListener('click', navigateItem, false);

function navigateItem(e){
aboutItem.scrollIntoView({behavior: "smooth"});
}
*/




// talking points smooth link
/*
let talkLink = document.querySelector('#talk-link');
let talkItem = document.querySelector('#talk-link-b');

talkLink.addEventListener('click', navigateItem2, false);

function navigateItem2(e){
talkItem.scrollIntoView({behavior: "smooth"});
}

// template letter smooth link
let tempLink = document.querySelector('#temp-link');
let tempItem = document.querySelector('#temp-link-b');

tempLink.addEventListener('click', navigateItem3, false);

function navigateItem3(e){
tempItem.scrollIntoView({behavior: "smooth"});
}

//contact info smooth link
let contactLink = document.querySelector('#contact-link');
let contactItem = document.querySelector('#contact-link-b');

contactLink.addEventListener('click', navigateItem4, false);

function navigateItem4(e){
contactItem.scrollIntoView({behavior: "smooth"});
}
*/
