// make a function that changes the text of the class clock into the current time

let slideSpeed = 500;

// clock with jQuery
$(document).ready(function() {
  $("#portable").click(() => {
    $("#portable .repo-desc").toggle(slideSpeed);
    $(`#portable .doc`).slideToggle(slideSpeed);
  });
  $("#ll").click(() => {
    $("#ll .repo-desc").toggle(slideSpeed);
    $(`#ll .doc`).slideToggle(slideSpeed);
  });

  setInterval(function() {
    let currentTime = new Date();
    let hours = currentTime.getHours();
    let minutes = currentTime.getMinutes();
    let seconds = currentTime.getSeconds();

    if (hours < 10) {
      hours = "0" + hours;
    }
    if (minutes < 10) {
      minutes = "0" + minutes;
    }
    if (seconds < 10) {
      seconds = "0" + seconds;
    }
    // 24 hour to 12 hour
    if (hours > 12) {
      hours = hours - 12;
    }
    let formattedTime = `${hours}:${minutes}:${seconds}`;

    $('.clock').text(formattedTime);
  }, 1000);
});