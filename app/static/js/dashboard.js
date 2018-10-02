'use strict';

window.chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
};

function range(start, end) {
  return new Array(end - start).fill().map((d, i) => i + start);
}

function createGraph(context, dataset, labels) {
    var axes = [{
        gridLines: {
            display: false,
            drawBorder: false
        },
        ticks: {
            display: false
        }
    }];

    var stats = new Chart(context, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [dataset]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            legend: {
                display: false
            },

            title: {
                display: true,
                text: 'Words Per Minute',
                fontSize: 32
            },

            scales: {
                yAxes: axes,
                xAxes: [{
                    gridLines: {
                        display: false,
                        drawBorder: false
                    }
                }]
            }
        }
    });

}

$(document).ready(function() {
    let context = $('#words')[0].getContext('2d');
    let dataset = {
        label: 'Words Per Minute',
        data: data.values,
        backgroundColor: window.chartColors.purple,
        borderColor: window.chartColors.purple,
        borderWidth: 1
    };

    createGraph(context, dataset, data.labels);
});
