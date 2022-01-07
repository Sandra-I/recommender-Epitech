<template>
  <div>
    <canvas id="bar-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import generateBarData from '../chart/bar-data.js'

export default {
  name: 'BarChart',
  props: ['data'],
  mounted() {
    const ctx = document.getElementById('bar-chart');
    const labels = this.getLabels();
    const dataset = this.getDataset();
    const barData = generateBarData(labels, dataset);
    new Chart(ctx, barData);
  },
  methods: {
    getDataset() {
      return [
        {
          label: "Clients",
          backgroundColor: "#1f43f4",
          borderColor: "#1f43f4",
          borderWidth: 1,
          data: this.data.customers
        },
        {
          label: "Chiffre d'affaire",
          backgroundColor: "#d7ddfd",
          borderColor: "#1f43f4",
          borderWidth: 1,
          data: this.data.ca
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