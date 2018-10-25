import Vue from 'vue';
import App from './client/App.vue';
import router from './client/router';

Vue.config.productionTip = false;

new Vue({
	router,
	render: h => h(App),
}).$mount('#app');
