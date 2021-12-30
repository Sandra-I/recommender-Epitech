export const lineData = {
    type: "doughnut",
    data: {
      labels: [
        "Gold",
        "Silver",
        "Bronze"
      ],
      datasets: [
        {
          label: "Clients",
          data: [43555, 12004, 10000],
          backgroundColor: ["#d7ddfd", "#fafafa", "#1f43f4"],
        }
      ]
    },
    options: {
      responsive: true,
      legend: {
        position: "right"
      }
    }
  };
  
  export default lineData;