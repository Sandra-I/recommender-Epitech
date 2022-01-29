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
  props: ['data','slug','type','legend'],
  mounted() {
    const ctx = document.getElementById(`pie-chart-${this.slug}`);
    const labels = this.getLabels();
    const dataset = this.getDataset();
    const pieData = generatePieData(labels, dataset, this.type, this.legend);
    new Chart(ctx, pieData);
  },
  methods: {
    getDataset() {
      const colors = ["#1f43f4", "#d7ddfd", "#e0e0e0"];
      return [
        {
          label: "Clients",
          data: Object.values(this.data),
          backgroundColor: colors.slice(this.data.length),
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