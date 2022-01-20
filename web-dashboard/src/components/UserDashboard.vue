<template>
    <div class="user-dashboard" v-if="customerDetails">
        <div class="profile">
          <div class="pp">
            <font-awesome-icon class="icon" icon="user-astronaut" size="7x"/>
          </div>
          <div class="name">
            <label>#{{ customerDetails.CLI_ID }}</label>
            <font-awesome-icon v-if="grade" v-bind:class="[grade, 'icon']" :title="`Client ${grade}`" icon="certificate"/>
          </div>
        </div>
        <span class="go-back" @click="$router.push({ name: 'Home'})">
            <b-icon-arrow-left></b-icon-arrow-left>
            Go back to main dashboard
        </span>
        <div class="section">
          <div class="row justify-content-between" v-if="customerDetails.average && customerDetails.frequency && customerDetails.recency">
            <Kpi title="Panier moyen" :value="formatPrice(customerDetails.average)"/>
            <Kpi title="Nombre total d'achat" :value="customerDetails.frequency"/>
            <Kpi title="Dernier achat" :value="`Il y a ${customerDetails.recency} mois`"/>
          </div>
          <div class="row justify-content-start" v-if="customerDetails.frequency_group">
              <Kpi title="Catégorie d'acheteur" :value="customerDetails.frequency_group"/>
          </div>
        </div>
        <div class="section" v-if="lastOrder">
          <LastOrder :lastOrder="lastOrder"/>
        </div>
        <div class="section-recommendations" v-if="recommendations && recommendations.most_buyed_article.length">
          <h2>Produit le plus acheté sur le site</h2>
          <Recommendations :recommendations="[recommendations.most_buyed_article]"/>
        </div>
        <div class="section-recommendations" v-if="recommendations && recommendations.paired_articles.length">
          <h2>Produits souvent achetés ensemble</h2>
          <Recommendations :recommendations="recommendations.paired_articles"/>
        </div>
        <div class="section-recommendations" v-if="recommendations && recommendations.paired_articles.length">
          <h2>Produits qui pourraient intéresser ce client</h2>
          <Recommendations :recommendations="recommendations.paired_articles"/>
        </div>
        <div class="section-recommendations" v-if="recommendations && recommendations.paired_articles.length">
          <h2>Des utilisateurs similaires ont aussi acheté</h2>
          <Recommendations :recommendations="recommendations.paired_articles"/>
        </div>
    </div>
</template>

<script>
import Kpi from './Kpi.vue'
import { getCustomerDetails, getRecommendations, getLastOrder } from '../../api/customer.js'
import LastOrder from './LastOrder.vue'
import Recommendations from './Recommendations.vue'

export default {
  name: 'UserDashboard',
  components: {
    Kpi,
    LastOrder,
    Recommendations
  },
  data: () => ({
    customerDetails: null,
    recommendations: null,
    lastOrder: null,
    grade : ""
  }),
  mounted: async function () {
    const customer_id = this.$route.params.id;
    this.customerDetails = await getCustomerDetails(customer_id);
    this.recommendations = await getRecommendations(customer_id);
    this.lastOrder = await getLastOrder(customer_id);
    this.setGrade();
  },
  methods: {
    formatPrice(price) {
      if (price) return `${this.formatNumber(price.toFixed(2))} €`;
    },
    formatNumber(value) {
      if (value) return parseFloat(value).toFixed(2);
    },
    setGrade() {
      if (this.customerDetails) {
        console.log("ok")
        switch (this.customerDetails.Cluster) {
          case 0:
            this.grade = "bronze";
            break;
          case 1:
            this.grade = "or";
            break;
          case 2:
            this.grade = "argent";
            break;
          default:
            this.grade = ""
        }
      }
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

  .profile {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    .pp {
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 100%;
      height: 120px;
      width: 120px;
      background-color: #1f43f4;
      color: #fff;
    }

    .name {
      font-weight: 800;
      padding: 20px 0 50px 0;

      .icon {
        margin-left: 10px;

        &.or {
          color: #f2bd00;
        }

        &.argent {
          color: #c7c7c7;
        }

        &.bronze {
          color: #b07862;
        }
      }
    }
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