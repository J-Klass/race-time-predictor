<template>
	<header :class="expanded ? 'expanded' : ''">
		<div class="header-inner">
			<h1>Race Time Predictor</h1>
			<p class="tagline">Running time predictions using machine learning</p>
		</div>
	</header>
</template>

<script>
	import IconBase from './icons/IconBase.vue';

	export default {
		components: {
			IconBase,
		},
		computed: {
			expanded() {
				// Expand header on Home page (route '/')
				return this.$router.currentRoute.path === '/';
			},
		},
	};
</script>

<style scoped>
	header {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 250px;
		max-height: 100vh;
		padding: var(--spacing-rel-large);
		background: var(--color-background-header) url("../assets/header-background.jpg") no-repeat
			center;
		background-size: cover;
	}

	header.expanded {
		height: 500px;
	}

	.header-inner {
		text-align: center;
	}

	.tagline {
		text-transform: uppercase;
	}

	h1 {
		letter-spacing: 0.05em;
		font-weight: var(--font-weight-bold);
		color: var(--color-strava);
	}

	.tagline {
		font-weight: var(--font-weight-semibold);
		letter-spacing: 0.025em;
	}

	@media (max-width: 850px) {
		h1 {
			font-size: 200%;
		}
	}

	@media (min-width: 851px) {
		h1 {
			font-size: 4vw;
		}
	}

	.tagline {
		font-size: 120%;
	}
</style>
