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
  }
});

startButton = document.getElementById("startButton")
stopButton = document.getElementById("stopButton")
displaying_reading = document.getElementById("displaying-reading")
display = document.getElementById("reading")
moistureText = document.getElementById("moisture-text")

startButton.onclick = function() {
  alert("Make sure the sensor is in the soil")
  startButton.style.display = "none"
  stopButton.style.display = "block"
  displaying_reading.style.display = "block"
 
  interval = setInterval(async function(){
    reading = await getReading();
    
    moistureText.innerHTML = categoriseReading(reading);
    
    display.innerHTML = reading;
    eel.create(reading)();
    plotGraph(reading);    
  }, 1000);

stopButton.onclick = function() {
  startButton.style.display = "block"
  stopButton.style.display = "none"
  clearInterval(interval)
  
}



}


function categoriseReading(reading){
  if (reading < 500){
      return "Soil is too dry"
    } else if (reading > 799) {
      return "Soil is too wet"
    } else {
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

(async function() {
  let all_time_data = await eel.format_readings()();
  
  console.log(all_time_data)
  console.log(all_time_data[0])
  console.log(all_time_data[1])

  
  var data = [
    {
      x: all_time_data[1],
      y: all_time_data[0],
      line: {shape: 'spline'},
      type: 'scatter'
    }
  ];
  
  Plotly.newPlot('all-time-chart', data);
  
})();

};
