function generateBarData(labels, dataset) {
  return {
      type: "bar",
      data: {
        labels: labels,
        datasets: dataset
      },
      options: {
        responsive: true,
        legend: {
          display: false
        },
        tooltips: {
          callbacks: {
            label: (item) => (item.datasetIndex == 1) ? 
              `CA : ${numberWithSpaces(parseInt(item.yLabel))} €` : 
              `Clients: ${numberWithSpaces(parseInt(item.yLabel))}`,
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
                maxTicksLimit: 8,
                beginAtZero: true,
                padding: 25,
                fontColor: '#cacbcc',
                callback: function(value) {
                  const k = parseInt(value) / 1000;
                  return k > 1 ? `${k}k` : value;
                }
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

export default generateBarData;