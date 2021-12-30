export const lineData = {
    type: "line",
    data: {
      labels: [
        "Janvier",
        "Février",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "Juillet",
        "Août",
        "Septembre",
        "Ocotbre",
        "Novembre",
        "Décembre"
      ],
      datasets: [
        {
          label: "Clients",
          data: [0, 0, 1, 2, 79, 82, 27, 14, 17, 20, 45, 100],
          backgroundColor: "#d7ddfd",
          borderColor: "#1f43f4",
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      lineTension: 1,
      legend: {
        display: false
      },
      scales: {
        xAxes: [
          {
            gridLines: {
              display:false
            },
            ticks: {
              maxTicksLimit: 6,
              fontColor: '#cacbcc'
            },
          }
        ],
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              padding: 25,
              maxTicksLimit: 6,
              fontColor: '#cacbcc'
            },  
          }
        ]
      },
    }
  };
  
  export default lineData;