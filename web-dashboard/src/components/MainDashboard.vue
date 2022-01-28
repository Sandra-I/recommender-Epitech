<template>
    <div class="main-dashboard">
        <div class="section row justify-content-around" v-if="dataLoaded && globalMetrics">
            <Kpi title="Panier moyen" :value="globalMetrics.basket" sufix="€"/>
            <Kpi title="Nombre total de client" :value="globalMetrics.totalCustomers"/>
            <Kpi title="Chiffre d'affaire total" :value="globalMetrics.totalCa" sufix="€"/>
        </div>
        <div class="section row">
            <div class="col-4 chart" v-if="dataLoaded">
                <div class="card">
                <div class="card-header">
                    <h3>Univers les plus vendues</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="univers" :data="topCategories.univers" type="doughnut" legend="Nombre de ventes"/>
                </div>
                </div>
            </div>
            <div class="col-4 chart" v-if="dataLoaded">
                <div class="card">
                <div class="card-header">
                    <h3>Familles les plus vendues</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="famille" :data="topCategories.famille" type="doughnut" legend="Nombre de ventes"/>
                </div>
                </div>
            </div>
            <div class="col-4 chart" v-if="dataLoaded">
                <div class="card">
                <div class="card-header">
                    <h3>Mailles les plus vendues</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="maille" :data="topCategories.maille" type="doughnut" legend="Nombre de ventes"/>
                </div>
                </div>
            </div>
        </div>
        <div class="section row" v-if="dataLoaded">
            <div class="col-4 chart" v-if="recencyGroupData">
                <div class="card">
                <div class="card-header">
                    <h3>Répartition de la récence d'achat</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="recency" :data="recencyGroupData" type="pie" legend="Part des achats"/>
                </div>
                </div>
            </div>
            <div class="col-4 chart" v-if="frequencyGroupData">
                <div class="card">
                <div class="card-header">
                    <h3>Répartition de la fréquence d'achat</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="frequency" :data="frequencyGroupData" type="pie" legend="Part des achats"/>
                </div>
                </div>
            </div>
        </div>
        <div class="section row" v-if="dataLoaded">
            <div class="col-12 chart">
                <div class="card">
                <div class="card-header">
                    <h3>Evolution du chiffre d'affaire par rapport au nombre de client</h3>
                </div>
                <div class="card-body">
                    <BarChart :data="saleEvolution"/>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Kpi from './Kpi.vue'
// import LineChart from './LineChart.vue'
import BarChart from './BarChart.vue'
import PieChart from './PieChart.vue'
import { getGlobalMetrics, getTopBy, getCustomerEvolution, getCAEvolution } from '../../api/dashboard.js'


export default {
  name: 'MainDashboard',
  components: {
    Kpi,
    // LineChart,
    BarChart,
    PieChart
  },
  data: () => ({
    globalMetrics: {},
    topCategories: {},
    saleEvolution: {},
    frequencyGroupData: {},
    dataLoaded: false
  }),
  mounted: async function () {
    this.globalMetrics = await getGlobalMetrics();
    this.topCategories.famille = await getTopBy("famille");
    this.topCategories.univers = await getTopBy("univers");
    this.topCategories.maille = await getTopBy("maille");
    
    this.globalMetrics.frequency_group = JSON.parse(this.globalMetrics.frequency_group);
    this.globalMetrics.recency = JSON.parse(this.globalMetrics.recency);
    this.globalMetrics.totalCustomers = parseInt(this.globalMetrics.frequency_group['OCCASIONNEL']['frequency_counts']);
        + parseInt(this.globalMetrics.frequency_group['REGULIER']['frequency_counts']);
    this.globalMetrics.totalCa = this.globalMetrics.totalCustomers * this.globalMetrics.basket;

    this.recencyGroupData = this.getRecencyCharData(this.globalMetrics.recency);
    this.frequencyGroupData = this.getFrequencyCharData(this.globalMetrics.frequency_group);

    this.saleEvolution.customers = await getCustomerEvolution();
    this.saleEvolution.ca = await getCAEvolution();

    this.dataLoaded = true;
  },
  methods: {
    getRecencyCharData(recencyGroup) {
        return {
            'Clients actifs': recencyGroup['ACTIVE']['recency_percent'].toFixed(2),
            'Clients inactifs': recencyGroup['INACTIVE']['recency_percent'].toFixed(2),
            'Clients occasionnels': recencyGroup['OCCASIONNEL']['recency_percent'].toFixed(2)
        }
    },
    getFrequencyCharData(frequencyGroup) {
        return {
            'Clients occasionnels': frequencyGroup['OCCASIONNEL']['frequency_percent'].toFixed(2),
            'Clients réguliers': frequencyGroup['REGULIER']['frequency_percent'].toFixed(2)
        }
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@300;400&display=swap');

.main-dashboard {
    z-index: 999;

    .chart {
        margin-bottom: 2rem;
        .card {
            border: 0;
            border-radius: 0.3rem;
            background-color: #fff;
            box-shadow: 0 0.75rem 1.875rem 0 rgb(90 97 105 / 5%) !important;

            .card-header {
                padding: 1.5rem;
                background-color: #fff !important;
                border-bottom: 0;

                h3 {
                font-size: 1rem;
                margin-bottom: 0 !important;
                }
            }

            .card-body {
                padding: 1rem;
            }
        }
    }
}
</style>