// make a function that changes the text of the class clock into the current time

function changeTime() {
  document.querySelector(".clock").innerHTML = Date();
}

function any() {
    const list = document.getElementsByTagName("hr");
    for (let i = 0; i < list.length; i++) {
        list[i].before("hello");
;    }
}

setInterval(changeTime, 1000);

any();