<template>
	<div class="predictions">
		<template
			v-for="prediction in predictionsFormatted"
		>
			<p
				:key="`distance-${prediction.distance}`"
				class="distance"
			>
				{{ prediction.distance }}
			</p>
			<h2
				:key="`time-${prediction.distance}`"
				class="time"
			>
				{{ prediction.time }}
			</h2>
		</template>
	</div>
</template>

<script>
	import { msToString } from '../../utils';

	export default {
		props: {
			predictions: {
				type: Object,
				default: () => {},
			},
		},
		computed: {
			predictionsFormatted() {
				return this.predictions.predictionData.map(({ distance, time }) => ({
					distance,
					time: msToString(time * 1000),
				}));
			},
		},
	};
</script>

<style scoped>
	.predictions {
		display: grid;
		grid-column-gap: var(--spacing-abs-small);
		grid-template-columns: fit-content(0) fit-content(0);
		align-items: center;
		justify-content: center;
	}

	.distance,
	.time {
		white-space: nowrap;
	}

	.distance {
		text-align: right;
	}
</style>
