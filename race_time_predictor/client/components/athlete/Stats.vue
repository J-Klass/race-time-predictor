<template>
	<div class="stats">
		<div>
			<h2>{{ stats.allRuns.count }}</h2>
			<p>Runs</p>
		</div>
		<div>
			<h2>{{ Math.round(stats.allRuns.distance / 1000) }} km</h2>
			<p>Distance</p>
		</div>
		<div>
			<h2>{{ stats.allRuns.elevation_gain }} m</h2>
			<p>Elevation gain</p>
		</div>
	</div>
</template>

<script>
	export default {
		props: {
			stats: {
				type: Object,
				default: () => {},
			},
		},
	};
</script>

<style scoped>
	.stats {
		display: grid;
		grid-column-gap: var(--spacing-abs-large);
		grid-template-columns: fit-content(0) fit-content(0) fit-content(0);
		align-items: center;
		justify-content: center;
		margin-bottom: var(--spacing-rel-small);
		text-align: center;
		white-space: nowrap;
	}
</style>
