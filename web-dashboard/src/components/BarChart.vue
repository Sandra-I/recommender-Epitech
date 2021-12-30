<template>
  <div>
    <canvas id="bar-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import barData from '../chart/bar-data.js'

export default {
  name: 'BarChart',
  data() {
    return {
      barData: barData
    }
  },
  mounted() {
    const ctx = document.getElementById('bar-chart');
    new Chart(ctx, this.barData);
  }
}
</script>