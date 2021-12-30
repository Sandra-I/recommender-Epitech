<template>
  <div>
    <canvas id="pie-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import pieData from '../chart/pie-data.js'

export default {
  name: 'PieChart',
  data() {
    return {
      pieData: pieData
    }
  },
  mounted() {
    const ctx = document.getElementById('pie-chart');
    new Chart(ctx, this.pieData);
  }
}
</script>