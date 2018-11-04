<template>
	<div id="app">
		<Header />
		<main>
			<router-view />
		</main>
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

	body {
		/* Variables */
		--color-background-header: #E4EDF4;
		--color-background: #FFFFFF;
		--color-background-footer: #303030;
		--color-text-faded: #838383;
		--color-text-faded-dark: #5B5B5B;
		--color-strava: #FC4C02;
		--color-strava-dark: #DD4302;
		--color-text: #1D1D1D;
		--color-text-underline: #CACACA;
		--color-white: #EFEFEF;
		--font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial,
			sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
		--font-size-small: 80%;
		--font-size-normal: 19px;
		--font-weight-normal: 400;
		--font-weight-semibold: 700;
		--font-weight-bold: 900;
		--line-height: 1.7;
		--spacing-abs-small: 20px;
		--spacing-abs-large: 40px;
		--spacing-rel-small: 4vw;
		--spacing-rel-large: 8vw;
		--transition: 0.15s;

		/* Global styles */
		font-family: var(--font-family);
		font-size: var(--font-size-normal);
		font-weight: var(--font-weight-normal);
		line-height: var(--line-height);
		color: var(--color-text);
		background: var(--color-background-footer);
	}

	main {
		background: var(--color-background);
	}

	.centered {
		width: 100%;
		max-width: 1000px;
		margin: 0 auto;
		padding: var(--spacing-rel-large);
	}

	h2 {
		font-size: 160%;
		font-weight: var(--font-weight-semibold);
	}

	a {
		color: inherit;
		text-underline-position: under;
	}

	hr {
		margin: var(--spacing-rel-small) 0;
		border: 0;
		border-bottom: 1px solid var(--color-text-underline);
	}
</style>
