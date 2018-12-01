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
						class="distance-col"
					>
						{{ prediction.title }}
					</p>
					<p
						:key="`time-${prediction.distance}`"
						class="time-col"
					>
						<span class="time large-text">{{ prediction.time }}</span>({{ prediction.speed }})
					</p>
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

<style lang="scss" scoped>
	.prediction-numbers {
		display: grid;
		grid-column-gap: $spacing-abs-small;
		grid-template-columns: fit-content(0) fit-content(0);
		align-items: baseline;
		justify-content: center;
	}

	.banner {
		margin-bottom: $spacing-rel-small;
	}

	.distance-col,
	.time-col {
		white-space: nowrap;
	}

	.distance-col {
		text-align: right;
	}

	.time {
		margin-right: $spacing-abs-small / 2;
	}
</style>
