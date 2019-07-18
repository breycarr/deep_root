window.onload = function(){

var interval, cnt, startButton, stopButton

cnt = 0;

// Create graph lines
Plotly.plot("chart",[{
  y:[],
  line: {shape: 'spline'},
  type:'line'
}], {
  yaxis: {
    range: [300, 1030]
  },
  height:200,
  width:450,
  margin: {l: 35, r: 35, t: 10, b: 20},
}, {displayModeBar: false});

startButton = document.getElementById("startButton");
stopButton = document.getElementById("stopButton");
displaying_reading = document.getElementById("displaying-reading");
display = document.getElementById("reading");
moistureText = document.getElementById("moisture-text");
showHist = document.getElementById("showHist");
showLive = document.getElementById("showLive");
histPage = document.getElementById("all-time-chart-page");
livePage = document.getElementById("live-chart-page");

showHist.onclick = function() {
  createHistGraph();
  histPage.style.display = "block";
  livePage.style.display = "none";
}

showLive.onclick = function() {
  histPage.style.display = "none";
  livePage.style.display = "block";
}

startButton.onclick = function() {
  alert("Make sure the sensor is in the soil")
  startButton.style.display = "none"
  stopButton.style.display = "block"
  displaying_reading.style.visibility = "visible"

  interval = setInterval(async function(){
    reading = await getReading();

    moistureText.innerHTML = categoriseReading(reading);

    display.innerHTML = reading;
    eel.create(reading)();
    plotGraph(reading);
  }, 1000);
}

stopButton.onclick = function() {
  startButton.style.display = "block"
  stopButton.style.display = "none"
  displaying_reading.style.visibility = "hidden"
  clearInterval(interval)

}

function categoriseReading(reading){
  if (reading < 500){
      body.setAttribute('bgcolor', '#F07070')
      return "Soil is too dry"
    } else if (reading > 799) {
      body.setAttribute('bgcolor', '#2177CD')
      return "Soil is too wet"
    } else {
      body.setAttribute('bgcolor', '#21CD6D')
      return "Soil is juuust right"
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

async function createHistGraph() {
  let all_time_data = await eel.format_readings()();

  var data = [
    {
      x: all_time_data[1],
      y: all_time_data[0],
      line: {shape: 'spline'},
      type: 'scatter'
    }
  ];

  Plotly.newPlot('all-time-chart', data);

};

};
