import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import MainDashboard from './components/MainDashboard.vue'
import UserDashboard from './components/UserDashboard.vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faBoxOpen } from '@fortawesome/free-solid-svg-icons'

// Upload FontAwesome Icons
library.add(faBoxOpen)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)

Vue.directive('click-outside', {
  bind: function (el, binding, vnode) {
    el.clickOutsideEvent = function (event) {
      // here I check that click was outside the el and his children
      if (!(el == event.target || el.contains(event.target))) {
        // and if it did, call method provided in attribute value
        vnode.context[binding.expression](event);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent)
  },
  unbind: function (el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  },
});

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { name: 'Home', path: '/', component: MainDashboard },
    { name: 'User', path: '/user/:id', component: UserDashboard }
  ]
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')