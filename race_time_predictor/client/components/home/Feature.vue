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

<style lang="scss" scoped>
	.feature {
		display: flex;
		align-items: center;
	}

	.feature-description {
		flex: 1;
	}

	.feature-left {
		text-align: left;

		.feature-icon {
			margin-right: $spacing-abs-small;
		}
	}

	.feature-right {
		flex-direction: row-reverse;
		text-align: right;

		.feature-icon {
			margin-left: $spacing-abs-small;
		}
	}

	.feature-icon {
		@include small-screen {
			width: 80px;
		}
		@include large-screen {
			width: 100px;
		}
	}
</style>
