<template>
	<div class="predictions">
		<div
			v-for="(time, distance) in predictions"
			:key="distance"
		>
			<p>{{ distance }}</p>
			<h2>{{ secondsToString(time) }}</h2>
		</div>
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
