<template>
	<div id="app">
		<Header />
		<router-view />
		<Footer />
	</div>
</template>

<script>
	import Footer from './components/Footer.vue';
	import Header from './components/Header.vue';

	export default {
		components: {
			Footer,
			Header,
		},
	};
</script>

<style>
	/* Style reset */
	@import "~minireset.css/minireset.min.css";

	#app {
		/* Variables */
		--color-background-header: #E4EDF4;
		--color-text-faded: #838383;
		--color-text-faded-dark: #5B5B5B;
		--color-strava: #FC4C02;
		--color-strava-dark: #DD4302;
		--color-text: #1D1D1D;
		--color-white: #EFEFEF;
		--font-family: 'Work Sans', sans-serif;
		--font-size-small: 80%;
		--font-size-normal: 19px;
		--font-weight-normal: 400;
		--font-weight-semibold: 700;
		--font-weight-bold: 900;
		--line-height: 1.7;
		--spacing-abs-small: 20px;
		--spacing-abs-large: 40px;
		--spacing-rel-small: 5vw;
		--spacing-rel-large: 10vw;
		--transition: 0.15s;

		/* Global styles */
		font-family: var(--font-family);
		font-size: var(--font-size-normal);
		font-weight: var(--font-weight-normal);
		line-height: var(--line-height);
		color: var(--color-text);
	}

	main {
		width: 100%;
		max-width: 1000px;
		padding: var(--spacing-rel-large);
		margin: 0 auto;
	}

	h2 {
		font-size: 160%;
		font-weight: var(--font-weight-semibold);
	}

	a {
		color: inherit;
		text-decoration: none;
	}
</style>
