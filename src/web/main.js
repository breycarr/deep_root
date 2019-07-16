window.onload = function(){

var interval, cnt, startButton, stopButton

cnt = 0;

function getData() {
  return Math.random();
}


// Create graph lines	
Plotly.plot("chart",[{
  y:[],
  type:'line'
}], {
  yaxis: {
    range: [300, 1015]
  }
});

startButton = document.getElementById("startButton")
stopButton = document.getElementById("stopButton")

startButton.onclick = function() {
  alert("Make sure the sensor is in the soil")
  startButton.style.display = "none"
  stopButton.style.display = "block"
 
  interval = setInterval(async function(){
    reading = await getReading();
    eel.create(reading)();
    plotGraph(reading);       
  }, 1000);

stopButton.onclick = function() {
  startButton.style.display = "block"
  stopButton.style.display = "none"
  clearInterval(interval)
}



}

function plotGraph(reading){
  Plotly.extendTraces("chart",{y:[[reading]]},[0]);
cnt++;

//moving y axis along 
  if(cnt > 20) {
    Plotly.relayout('chart', {
	  xaxis: {
	    range: [cnt-20,cnt]
	  }
    });
   }
}

function getReading() {
    return eel.get_reading_for_eel()()
}

};
