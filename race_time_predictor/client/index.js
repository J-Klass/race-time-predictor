import Vue from 'vue';
import VueApexCharts from 'vue-apexcharts';

import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;
Vue.use(VueApexCharts);

new Vue({
	router,
	render: h => h(App),
}).$mount('#app');
