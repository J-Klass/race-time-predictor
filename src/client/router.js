import Vue from 'vue';
import Router from 'vue-router';

import Athlete from './views/Athlete.vue';
import Home from './views/Home.vue';
import LoginRedirect from './views/LoginRedirect.vue';
import NotFound from './views/NotFound.vue';

Vue.use(Router);


export default new Router({
	mode: 'history',
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/',
			name: 'home',
			component: Home,
		},
		{
			path: '/athlete',
			name: 'athlete',
			component: Athlete,
		},
		{
			path: '/login-redirect',
			name: 'login-redirect',
			component: LoginRedirect,
		},
		{
			path: '*',
			name: 'not-found',
			component: NotFound,
		},
	],
});
