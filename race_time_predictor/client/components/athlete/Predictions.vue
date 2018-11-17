<template>
	<div class="predictions">
		<div class="predictions-numbers">
			<template
				v-for="prediction in predictions.distances"
			>
				<p
					:key="prediction.distance"
					class="distance"
				>
					{{ prediction.distance }}
				</p>
				<h2
					:key="prediction.distance"
					class="time"
				>
					{{ secondsToString(prediction.time) }}
				</h2>
			</template>
		</div>
		<div class="predictions-graph">
			<p>TODO graph</p>
		</div>
	</div>
</template>

<script>
	export default {
		props: {
			predictions: {
				type: Object,
				default: () => {},
			},
		},
		methods: {
			secondsToString(seconds) {
				return new Date(seconds * 1000).toISOString().substr(11, 8);
			},
		},
	};
</script>

<style scoped>
	.predictions-numbers {
		display: grid;
		grid-column-gap: var(--spacing-abs-small);
		grid-template-columns: fit-content(0) fit-content(0);
		align-items: center;
		justify-content: center;
	}

	.distance {
		text-align: right;
		white-space: nowrap;
	}
</style>
