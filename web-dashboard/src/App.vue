<template>
  <div id="app">
    <div class="container">
      <h1>Recommender Explorer</h1>
      <div class="row justify-content-center">
        <Search class="col-6 p-0"/>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Search from './components/Search.vue'

export default {
  name: 'App',
  components: {
    Search
  },
  data: () => ({
    selectedUserId: null
  })
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@300;400&display=swap');

body {
  background-color: #fafafa !important;

  #app {
    font-family: 'M PLUS Rounded 1c', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #3d5170;
    margin-top: 60px;

    h1 {
      text-align: center;
      font-weight: 600;
      font-size: 1.5rem;
      margin-bottom: 3rem;
    }

    .section {
      margin-bottom: 5rem;
    }
  }
}
</style>
