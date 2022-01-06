<template>
    <div class="user-dashboard">
        <span class="go-back" @click="$router.push({ name: 'Home'})">
            <b-icon-arrow-left></b-icon-arrow-left>
            Go back to main dashboard
        </span>
        <div class="section" v-if="customerDetails">
          <div class="row justify-content-between" v-if="customerDetails.average && customerDetails.frequency && customerDetails.recency">
            <Kpi title="Panier moyen" :value="formatPrice(customerDetails.average)"/>
            <Kpi title="Nombre total d'achat" :value="customerDetails.frequency"/>
            <Kpi title="Dernier achat" :value="`Il y a ${customerDetails.recency} mois`"/>
          </div>
          <div class="row justify-content-start" v-if="customerDetails.frequency_group">
              <Kpi title="Catégorie d'acheteur" :value="customerDetails.frequency_group.toLowerCase()"/>
          </div>
        </div>
        <div class="section" v-if="lastOrder">
          <LastOrder :lastOrder="lastOrder"/>
        </div>
        <div class="section-recommendations" v-if="recommendations">
          <h2>Produit le plus acheté sur le site</h2>
          <Recommendations :recommendations="[recommendations.most_buyed_article]"/>
        </div>
        <div class="section-recommendations" v-if="recommendations">
          <h2>Produits souvent achetés ensemble</h2>
          <Recommendations :recommendations="recommendations.paired_articles"/>
        </div>
        <div class="section-recommendations" v-if="recommendations">
          <h2>Produits qui pourraient intéresser ce client</h2>
          <Recommendations :recommendations="recommendations.similar_product"/>
        </div>
        <div class="section-recommendations" v-if="recommendations">
          <h2>Des utilisateurs similaires ont aussi acheté</h2>
          <Recommendations :recommendations="recommendations.similar_user_product"/>
        </div>
        <!-- <div class="section row">
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
        </div> -->
    </div>
</template>

<script>
import Kpi from './Kpi.vue'
// import LineChart from './LineChart.vue'
// import BarChart from './BarChart.vue'
// import PieChart from './PieChart.vue'
import { getCustomerDetails, getRecommendations, getLastOrder } from '../../api/customer.js'
import LastOrder from './LastOrder.vue'
import Recommendations from './Recommendations.vue'

export default {
  name: 'UserDashboard',
  components: {
    Kpi,
    LastOrder,
    Recommendations
    // LineChart,
    // BarChart,
    // PieChart
  },
  data: () => ({
    customerDetails: null,
    recommendations: null,
    lastOrder: null
  }),
  mounted: async function () {
    this.customerDetails = await getCustomerDetails(1490281);
    this.recommendations = await getRecommendations(1490281);
    this.lastOrder = await getLastOrder(1490281);
    this.lastOrder = Object.values(this.lastOrder);
  },
  methods: {
    formatPrice(price) {
      if (price) return `${this.formatNumber(price.toFixed(2))} €`;
    },
    formatNumber(value) {
      if (value) return parseFloat(value).toFixed(2);
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@300;400&display=swap');

.user-dashboard {

  h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }

  .section-recommendations {
    margin: 3rem 0;
  }

  .go-back {
    display: block;
    margin-bottom: 2rem;
    cursor: pointer;
    font-weight: 600;
    text-align: right;
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