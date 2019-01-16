"use strict";

window.chartColors = {
  red: "rgb(255, 99, 132)",
  orange: "rgb(255, 159, 64)",
  yellow: "rgb(255, 205, 86)",
  green: "rgb(75, 192, 192)",
  blue: "rgb(54, 162, 235)",
  purple: "rgb(153, 102, 255)",
  grey: "rgb(201, 203, 207)",
  white: "rgb(255, 255, 255)"
};

function range(start, end) {
  return new Array(end - start).fill().map((d, i) => i + start);
}

function createGraph(context, datasets, labels, text) {
  var axes = [
    {
      gridLines: {
        display: false,
        drawBorder: false
      },
      ticks: {
        display: false
      }
    }
  ];

  var stats = new Chart(context, {
    type: "line",
    data: {
      labels: labels,
      datasets: datasets
    },

    options: {
      responsive: true,
      maintainAspectRatio: false,

      legend: {
        display: false
      },

      title: {
        display: true,
        text: text,
        fontSize: 32
      },

      scales: {
        yAxes: axes,
        xAxes: [
          {
            gridLines: {
              display: false,
              drawBorder: false
            }
          }
        ]
      }
    }
  });
}

function buildDataset(statistics, title, color) {
  let values = statistics.map(element => element.value);

  let dataset = {
    label: title,
    data: values,
    backgroundColor: color,
    borderColor: color,
    borderWidth: 1,
    fill: false,
    pointRadius: 2,
    pointHoverRadius: 5
  };

  return dataset;
}

function getLabels(statistics) {
  return statistics.words.map(element => element.time);
}

function buildStatistics(statistics) {
  let labels = getLabels(statistics);
  let canvas = $("#canvas")[0];
  let context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);
  let datasets = [];

  datasets.push(
    buildDataset(statistics.words, "Words", window.chartColors.red)
  );

  datasets.push(
    buildDataset(statistics.chars, "Characters", window.chartColors.blue)
  );

  datasets.push(
    buildDataset(statistics.accuracy, "Accuracy", window.chartColors.green)
  );

  createGraph(context, datasets, labels, "");
}

$(document).ready(function() {
  $("#daily").click(() => {
    buildStatistics(statistics.daily);
  });

  $("#weekly").click(() => {
    buildStatistics(statistics.weekly);
  });

  $("#monthly").click(() => {
    buildStatistics(statistics.monthly);
  });
  buildStatistics(statistics.daily);
});
