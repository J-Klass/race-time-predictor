<template>
	<svg
		:width="width"
		:height="height"
		:aria-labelledby="title"
		:viewBox="viewBox"
		xmlns="http://www.w3.org/2000/svg"
		role="presentation"
	>
		<title v-if="title">{{ title }}</title>
		<g :fill="fill">
			<slot />
		</g>
	</svg>
</template>

<script>
	export default {
		props: {
			title: {
				type: String,
				default: null,
			},
			width: {
				type: [Number, String],
				default: null,
			},
			height: {
				type: [Number, String],
				default: null,
			},
			viewBox: {
				type: String,
				default: null,
			},
			fill: {
				type: String,
				default: 'currentColor',
			},
		},
	};
</script>

<style scoped>
	svg {
		display: inline-block;
	}

	g {
		transition: var(--transition);
	}
</style>
