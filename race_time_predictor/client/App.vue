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

<style lang="scss">
	// Style reset
	@import "~minireset.css/minireset.min.css";

	body {
		font-family: $font-family;
		font-size: $font-size-normal;
		font-weight: $font-weight-normal;
		line-height: $line-height;
		color: $color-text;
		background: $color-background-footer;
	}

	#app {
		@include small-screen {
			font-size: 90%;
		}
	}

	main {
		background: $color-background;
	}

	.centered {
		width: 100%;
		max-width: 1000px;
		margin: 0 auto;
		padding: $spacing-rel-large;
	}

	h1 {
		font-size: 200%;
		font-weight: $font-weight-bold;
		color: $color-strava;
		letter-spacing: 0.05em;
	}

	h2,
	.large-text {
		font-size: 160%;
		font-weight: $font-weight-semibold;
	}

	.small-text {
		font-size: $font-size-small;
	}

	a {
		color: inherit;
		text-underline-position: under;
	}
</style>
