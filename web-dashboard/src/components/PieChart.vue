<template>
  <div>
    <canvas :id="`pie-chart-${slug}`"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import generatePieData from '../chart/pie-data.js'

export default {
  name: 'PieChart',
  props: ['data','slug'],
  mounted() {
    const ctx = document.getElementById(`pie-chart-${this.slug}`);
    const labels = this.getLabels();
    const dataset = this.getDataset();
    const pieData = generatePieData(labels, dataset);
    new Chart(ctx, pieData);
  },
  methods: {
    getDataset() {
      return [
        {
          label: "Clients",
          data: Object.values(this.data),
          backgroundColor: ["#d7ddfd", "#e0e0e0", "#1f43f4"],
        }
      ];
    },
    getLabels() {
      return Object.keys(this.data).map(label => this.capitalize(label))
    },
    capitalize(str) {
      str = str.toLowerCase();
      str = str.charAt(0).toUpperCase() + str.slice(1);
      str = (str.length > 20) ? str.substr(0, 19) + '...' : str;
      return str;
    }
  }
}
</script>