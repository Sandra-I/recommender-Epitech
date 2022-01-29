<template>
  <div>
    <canvas id="line-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import generateLineData from '../chart/line-data.js'

export default {
  name: 'LineChart',
  props: ['data'],
  mounted() {
    const ctx = document.getElementById('line-chart');
    const labels = this.getLabels();
    const dataset = this.getDataset();
    const lineData = generateLineData(labels, dataset);
    new Chart(ctx, lineData);
  },
  methods: {
    getDataset() {
      return [
        {
          label: "Chiffre d'affaires",
          data: this.data.ca,
          fill: false,
          borderColor: "#1f43f4",
          borderWidth: 3
        },
        {
          label: "Clients",
          data: this.data.customers,
          fill: false,
          borderColor: "#bac1cb",
          borderWidth: 3
        }
      ];
    },
    getLabels() {
      return [
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
      ];
    }
  }
}
</script>