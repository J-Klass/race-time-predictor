<template>
	<div class="hero">
		<div class="hero-inner">
			<h1>Race Time Predictor</h1>
			<p class="tagline">Running time predictions using machine learning</p>
		</div>
	</div>
</template>

<script>
	import IconBase from '../icons/IconBase.vue';

	export default {
		components: {
			IconBase,
		},
	};
</script>

<style scoped>
	.hero {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 500px;
		max-height: 100vh;
		padding: var(--spacing-rel-large);
		background: var(--color-background-hero) url("../../assets/hero-background.jpg") no-repeat
			center;
		background-size: cover;
	}

	.hero-inner {
		text-align: center;
	}

	h1,
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
