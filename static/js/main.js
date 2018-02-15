"use strict";

function clearScoreboard() {
  document.getElementById("leaderboard").innerHTML = "";
}

function makeElement(name, score) {
  var li = document.createElement("li");
  var mark = document.createElement("mark");
  var small = document.createElement("small");

  li.appendChild(mark);
  li.appendChild(small);

  mark.textContent = name;
  small.textContent = score;

  return li;
}

function addScore(name, score) {
  var li = makeElement(name, score);
  document.getElementById("leaderboard").appendChild(li);
  return li;
}

function parse(response){
    var json = JSON.parse(response);
    console.log(json);
    clearScoreboard();
    json.forEach(function(element){
        addScore(element[0], element[1]);
    });
}

function httpGetAsync(url, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            callback(xmlHttp.responseText);
        }
    }
    xmlHttp.open("GET", url, true); // true for asynchronous
    xmlHttp.send(null);
}

function refresh(){
    var xmlhttp = new XMLHttpRequest();
    var url = "https://api.parkour.ultra-horizon.com/score";

    var json = httpGetAsync(url, parse);
}

function init(){
    console.log("polling system started!");
}

refresh();
setInterval(refresh, 5000);
