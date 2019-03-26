import Chart from 'chart.js';
import Vue from 'vue';

import App from './App.vue';
import router from './router';


Chart.defaults.global.defaultFontFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", ' +
	'Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"';
Vue.config.productionTip = false;

new Vue({
	router,
	render: h => h(App),
}).$mount('#app');
