<template>
    <div class="user-dashboard">
        <span class="go-back" @click="$router.push({ name: 'Home'})">
            <b-icon-arrow-left></b-icon-arrow-left>
            Go back to main dashboard
        </span>
        <div class="section flex-table">
            <div class="row flex-row">
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
            </div>
            <div class="row flex-row">
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
            </div>
            <div class="row flex-row">
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
                <div class="flex-cell col-2">Test</div>
            </div>
        </div>
        <div class="section row justify-content-around">
            <Kpi title="Panier moyen" value="EEEEEEEEEEEEEEEEEE"/>
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
            <div class="col-6 chart">
                <div class="card">
                <div class="card-header">
                    <h3>Line data</h3>
                </div>
                <div class="card-body">
                    <LineChart/>
                </div>
                </div>
            </div>
            <div class="col-6 chart">
                <div class="card">
                <div class="card-header">
                    <h3>Bar data</h3>
                </div>
                <div class="card-body">
                    <BarChart/>
                </div>
                </div>
            </div>
            <div class="col-6 chart">
                <div class="card">
                <div class="card-header">
                    <h3>Pie data</h3>
                </div>
                <div class="card-body">
                    <PieChart/>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Kpi from './Kpi.vue'
import LineChart from './LineChart.vue'
import BarChart from './BarChart.vue'
import PieChart from './PieChart.vue'

export default {
  name: 'UserDashboard',
  components: {
    Kpi,
    LineChart,
    BarChart,
    PieChart
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@300;400&display=swap');

.user-dashboard {
    .go-back {
        display: block;
        margin-bottom: 2rem;
        cursor: pointer;
        font-weight: 600;
        text-align: right;
    }

    .flex-table {
        display: flex;
        flex-direction: column;
        border: 0;
        border-radius: 0.3rem;
        background-color: #fff;
        box-shadow: 0 0.75rem 1.875rem 0 rgb(90 97 105 / 5%) !important;
        padding: 2rem;

        .flex-row {
            width: 100%;
            margin: auto;
            padding: 0.8rem 0;

            &:not(:last-child) {
                border-bottom: 1px solid #e2e2e2;
            }

            .flex-cell {
                margin: 0;
                padding: 0 1rem;
            }
        }
    }

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