<template>
	<div class="stats">
		<div class="stats-entry">
			<h2>{{ stats.allRuns.count }}</h2>
			<p>Runs</p>
		</div>
		<div class="stats-entry">
			<h2>{{ Math.round(stats.allRuns.distance / 1000) }} km</h2>
			<p>Distance</p>
		</div>
		<div class="stats-entry">
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

<style lang="scss" scoped>
	.stats {
		display: grid;
		align-items: center;
		justify-content: center;
		margin-bottom: $spacing-rel-small;
		text-align: center;
		white-space: nowrap;

		@include small-screen {
			line-height: $line-height-small;

			.stats-entry {
				margin-bottom: $spacing-rel-small;
			}
		}
		@include large-screen {
			grid-template-columns: fit-content(0) fit-content(0) fit-content(0);
			grid-column-gap: $spacing-abs-large;
		}
	}
</style>
