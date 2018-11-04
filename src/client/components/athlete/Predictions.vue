<template>
	<div class="predictions">
		<template
			v-for="(time, distance) in predictions"
		>
			<p
				:key="distance"
				class="distance"
			>
				{{ distance }}
			</p>
			<h2
				:key="distance"
				class="time"
			>
				{{ secondsToString(time) }}
			</h2>
		</template>
	</div>
</template>

<script>
	export default {
		props: {
			predictions: {
				type: Array,
				default: () => [],
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
	.predictions {
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
