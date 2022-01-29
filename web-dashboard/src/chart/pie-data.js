function generatePieData(labels, dataset, type, legend) {
  return {
    type: type,
    data: {
      labels: labels,
      datasets: dataset
    },
    options: {
      responsive: true,
      tooltips: {
        callbacks: {
          title: function(tooltipItem, data) {
            const index = tooltipItem[0]['index'];
            return data['labels'][index];
          },
          label: function(tooltipItem, data) {
            const index = tooltipItem['index'];
            const dataset = data['datasets'][0]['data'];
            const value = dataset[index];
            return `${legend}: ${ numberWithSpaces(value) }`;
          },
        },
      },
      legend: {
        position: "right",
        labels: {
          boxWidth: 10
        }
      }
    }
  };
}

function numberWithSpaces(x) {
  if (x > 1000) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  }
  return x;
}

export default generatePieData;