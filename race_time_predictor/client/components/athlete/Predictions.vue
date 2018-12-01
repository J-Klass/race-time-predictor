<template>
	<div class="predictions">
		<Banner
			v-if="predictions.error"
			type="error"
			message="You don't have enough Strava activities to generate predictions."
		/>
		<template v-else>
			<Banner
				v-if="predictions.warning"
				type="warning"
				message="You only have a small number of Strava activities. Predictions might be
					inaccurate."
			/>
			<div class="prediction-numbers">
				<template
					v-for="prediction in predictionsFormatted"
				>
					<p
						:key="`distance-${prediction.distance}`"
						class="distance"
					>
						{{ prediction.title }}
					</p>
					<h2
						:key="`time-${prediction.distance}`"
						class="time"
					>
						{{ prediction.time }} ({{ prediction.speed }})
					</h2>
				</template>
			</div>
		</template>
	</div>
</template>

<script>
	import Banner from '../general/Banner.vue';
	import { getSpeedString, msToString } from '../../utils';

	export default {
		components: {
			Banner,
		},
		props: {
			predictions: {
				type: Object,
				default: () => {},
			},
			useMetricSystem: {
				type: Boolean,
				default: null,
			},
		},
		computed: {
			predictionsFormatted() {
				return this.predictions.predictionData.map(({ title, time, distance }) => ({
					title,
					distance,
					time: msToString(time * 1000, true),
					speed: getSpeedString(distance, time * 1000, this.useMetricSystem),
				}));
			},
		},
	};
</script>

<style scoped>
	.prediction-numbers {
		display: grid;
		grid-column-gap: var(--spacing-abs-small);
		grid-template-columns: fit-content(0) fit-content(0);
		align-items: baseline;
		justify-content: center;
	}

	.banner {
		margin-bottom: var(--spacing-rel-small);
	}

	.distance,
	.time {
		white-space: nowrap;
	}

	.distance {
		text-align: right;
	}
</style>
