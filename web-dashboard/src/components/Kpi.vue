<template>
  <div class="kpi">
    <h3 class="title">{{ title }}</h3>
    <span class="value">{{ value }}</span>
  </div>
</template>

<script>
export default {
  name: 'Kpi',
  props: {
      'title': String,
      'value': String
  }
}
</script>

<style scoped lang="scss">
.kpi {
    display: flex;
    flex-direction: column;
    max-width: 20rem;
    border-radius: 0.3rem;
    border: 1px solid #e2e2e2;
    border-left: 0.5rem solid rgba(31, 67, 244, 0.3) !important;
    box-shadow: 0 2px 4px 0 rgb(90 97 105 / 20%);
    padding: 1.2rem;
    margin: 0.7rem;

    h3 {
        font-weight: 400;
        font-size: 1rem;
    }

    .value {
        color: #1f43f4;
        font-weight: 600;
        margin-top: 0.5rem;
    }

}
</style>
