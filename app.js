// make a function that changes the text of the class clock into the current time

function changeTime() {
  let time = new Date();
  let hours = time.getHours();
  let minutes = time.getMinutes();
  let seconds = time.getSeconds();
  let clock = document.querySelector(".clock");
  // make hours into 12-hour format
  if (hours > 12) {
    hours = hours - 12;
  }
  // add a zero in front of numbers less than 10
  if (hours < 10) {
    hours = "0" + hours;
  }
  if (minutes < 10) {
    minutes = "0" + minutes;
  }
  if (seconds < 10) {
    seconds = "0" + seconds;
  }
  // put the time together
  clock.innerText = `${hours}:${minutes}:${seconds}`;
}

setInterval(changeTime, 1000);