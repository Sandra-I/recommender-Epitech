function generatePieData(labels, dataset) {
  return {
    type: "doughnut",
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
            return `Nombre ventes: ${ numberWithSpaces(value) }`;
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
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
}

export default generatePieData;