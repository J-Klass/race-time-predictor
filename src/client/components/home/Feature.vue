<template>
	<div :class="`feature feature-${iconPosition}`">
		<div class="feature-icon">
			<slot />
		</div>
		<p class="feature-description">{{ text }}</p>
	</div>
</template>

<script>
	export default {
		props: {
			iconPosition: {
				type: String,
				default: 'left',
			},
			text: {
				type: String,
				default: '',
			},
		},
	};
</script>

<style scoped>
	.feature {
		display: flex;
		align-items: center;
	}

	.feature + .feature {
		margin-top: var(--spacing-rel-small);
	}

	.feature-description {
		flex: 1;
	}

	.feature-left {
		text-align: left;
	}

	.feature-left .feature-icon {
		margin-right: var(--spacing-abs-small);
	}

	.feature-right {
		flex-direction: row-reverse;
		text-align: right;
	}

	.feature-right .feature-icon {
		margin-left: var(--spacing-abs-small);
	}
</style>
