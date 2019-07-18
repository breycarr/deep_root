window.onload = function () {
  const startButton = document.getElementById('startButton');
  const stopButton = document.getElementById('stopButton');
  const resetButton = document.getElementById('resetButton');
  const displayingReading = document.getElementById('displaying-reading');
  const display = document.getElementById('reading');
  const moistureText = document.getElementById('moisture-text');
  const showHist = document.getElementById('showHist');
  const showLive = document.getElementById('showLive');
  const histPage = document.getElementById('all-time-chart-page');
  const livePage = document.getElementById('live-chart-page');

  let interval;
  let cnt;

  cnt = 0;

  // Create graph lines
  Plotly.plot('chart', [{
    y: [],
    line: {
      shape: 'spline',
    },
    type: 'line',
  }], {
    yaxis: {
      range: [300, 1030],
    },
    height: 200,
    width: 450,
    margin: {
      l: 35,
      r: 35,
      t: 10,
      b: 20,
    },
  }, {
    displayModeBar: false,
  });

  function plotGraph(reading) {
    Plotly.extendTraces('chart', {
      y: [
        [reading],
      ],
    }, [0]);
    cnt += 1;

    // moving y axis along
    if (cnt > 20) {
      Plotly.relayout('chart', {
        xaxis: {
          range: [cnt - 20, cnt],
        },
      });
    }
  }

  async function createHistGraph() {
    let allTimeData = await eel.format_readings()();

    let data = [{
      x: allTimeData[1],
      y: allTimeData[0],
      line: {
        shape: 'spline',
      },
      type: 'scatter',
    }];

  Plotly.newPlot('all-time-chart', data, {
    height:200,
    width:450,
    margin: {l: 35, r: 35, t: 10, b: 20},
    }, {displayModeBar: false});
  }

  function getReading() {
    return eel.get_reading_for_eel()();
  }

  function categoriseReading(reading) {
    if (reading < 500) {
      body.setAttribute('style', 'background:url(images/too_dry.gif); background-repeat:no-repeat; background-size:cover; rotate="180"')
      return 'Soil is too dry';
    } if (reading > 799) {
      body.setAttribute('style', 'background:url(https://i.imgur.com/aFXxThM.gif); background-repeat:no-repeat; background-size:cover');
      return 'Soil is too wet';
    } else {
      body.setAttribute('style', 'background:url(images/just_right.gif); background-repeat:no-repeat; background-size:cover');
      return 'Soil is juuust right';
    }
  }

  showHist.onclick = function () {
    createHistGraph();
    histPage.style.display = 'block';
    livePage.style.display = 'none';
  };

  showLive.onclick = function () {
    histPage.style.display = 'none';
    livePage.style.display = 'block';
  };

  startButton.onclick = function () {
    alert('Make sure the sensor is in the soil');
    startButton.style.display = 'none';
    stopButton.style.display = 'inline-block';
    displayingReading.style.visibility = 'visible';

    interval = setInterval(async function () {
      let reading = await getReading();

      moistureText.innerHTML = categoriseReading(reading);

      display.innerHTML = reading;
      eel.create(reading)();
      plotGraph(reading);
    }, 1000);
  };

  stopButton.onclick = function () {
    startButton.style.display = 'inline-block';
    stopButton.style.display = 'none';
    displayingReading.style.visibility = 'hidden';
    clearInterval(interval);
  };

  resetButton.onclick = function () {
    window.location.reload();
  };
};
