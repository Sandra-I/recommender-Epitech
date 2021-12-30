<template>
  <div>
    <canvas id="planet-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import lineData from '../chart/line-data.js'

export default {
  name: 'LineChart',
  data() {
    return {
      lineData: lineData
    }
  },
  mounted() {
    const ctx = document.getElementById('planet-chart');
    new Chart(ctx, this.lineData);
  }
}
</script>