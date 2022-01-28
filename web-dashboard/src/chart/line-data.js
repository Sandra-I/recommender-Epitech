function generateLineData(labels, dataset) {
  return {
    type: "line",
    data: {
      labels: labels,
      datasets: dataset
    },
    options: {
      responsive: true,
      lineTension: 1,
      legend: {
        display: false
      },
      tooltips: {
        callbacks: {
          label: (item) => `Ventes : ${numberWithSpaces(parseInt(item.yLabel))}`
        },
      },
      scales: {
        xAxes: [
          {
            gridLines: {
              display:false
            },
            ticks: {
              fontColor: '#cacbcc'
            },
          }
        ],
        yAxes: [
          {
            type: 'logarithmic',
            ticks: {
              beginAtZero: true,
              padding: 15,
              fontColor: '#cacbcc'
            },  
          }
        ]
      },
    }
  };
}

function numberWithSpaces(x) {
  if (x > 1000) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  }
  return x;
}

export default generateLineData;