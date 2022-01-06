<template>
  <div class="recommendations row">
    <div class="recommendation row" v-for="recommendation in recommendations" :key="recommendation">
      <div class="col-3 text-center">
        <font-awesome-icon class="icon" icon="box-open" title="product" size="2x"/>
      </div>
      <div class="col-9">
        <span>{{ recommendation }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Recommendations',
  props: {
    'recommendations': Array
  }
}
</script>

<style scoped lang="scss">
.recommendations {

  .recommendation {
    align-items: center;
    max-width: 20rem;
    border-radius: 0.3rem;
    box-shadow: 0 2px 4px 0 rgb(90 97 105 / 20%);
    padding: 1.2rem 0;
    margin: 0.7rem;

    h3 {
      font-weight: 400;
      font-size: 1rem;
    }

    .value {
      color: #1f43f4;
      font-weight: 600;
      margin-top: 0.5rem;
      text-transform: lowercase;
    }
  }
}
</style>
