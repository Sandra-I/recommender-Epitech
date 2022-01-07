<template>
    <div class="main-dashboard">
        <div class="section row justify-content-around">
            <Kpi title="Panier moyen" value="230.12 €"/>
            <Kpi title="Nombre total de client" value="10000"/>
            <Kpi title="Nouveau client 30 derniers jours" value="329"/>
            <Kpi title="Panier moyen" value="230.12 €"/>
            <Kpi title="Nombre total de client" value="10000"/>
            <Kpi title="Nouveau client 30 derniers jours" value="329"/>
            <Kpi title="Panier moyen" value="230.12 €"/>
            <Kpi title="Nombre total de client" value="10000"/>
            <Kpi title="Nouveau client 30 derniers jours" value="329"/>
        </div>
        <div class="section row">
            <div class="col-4 chart" v-if="dataLoaded">
                <div class="card">
                <div class="card-header">
                    <h3>Univers les plus vendues</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="univers" :data="topCategories.univers"/>
                </div>
                </div>
            </div>
            <div class="col-4 chart" v-if="dataLoaded">
                <div class="card">
                <div class="card-header">
                    <h3>Familles les plus vendues</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="famille" :data="topCategories.famille"/>
                </div>
                </div>
            </div>
            <div class="col-4 chart" v-if="dataLoaded">
                <div class="card">
                <div class="card-header">
                    <h3>Mailles les plus vendues</h3>
                </div>
                <div class="card-body">
                    <PieChart slug="maille" :data="topCategories.maille"/>
                </div>
                </div>
            </div>
        </div>
        <div class="section row" v-if="dataLoaded">
            <!-- <div class="col-12 chart">
                <div class="card">
                <div class="card-header">
                    <h3>Line data</h3>
                </div>
                <div class="card-body">
                    <LineChart :data="saleEvolution"/>
                </div>
                </div>
            </div> -->
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
import { getTopBy, getCustomerEvolution, getCAEvolution } from '../../api/dashboard.js'


export default {
  name: 'MainDashboard',
  components: {
    Kpi,
    // LineChart,
    BarChart,
    PieChart
  },
  data: () => ({
    topCategories: {},
    saleEvolution: {},
    dataLoaded: false
  }),
  mounted: async function () {
    this.topCategories.famille = await getTopBy("famille");
    this.topCategories.univers = await getTopBy("univers");
    this.topCategories.maille = await getTopBy("maille");

    this.saleEvolution.customers = await getCustomerEvolution();
    this.saleEvolution.ca = await getCAEvolution();

    this.dataLoaded = true;
  },
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@300;400&display=swap');

.main-dashboard {
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