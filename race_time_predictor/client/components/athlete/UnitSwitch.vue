<template>
	<div class="switch-wrapper">
		<p>km</p>
		<label class="switch">
			<input
				:checked="!useMetricSystem"
				type="checkbox"
				@change="$emit('toggle-metric-system')"
			>
			<span class="toggle" />
		</label>
		<p>mi</p>
	</div>
</template>

<script>
	export default {
		props: {
			useMetricSystem: {
				type: Boolean,
				default: null,
			},
			setUnitSystem: {
				type: Function,
				default: null,
			},
		},
	};
</script>

<style lang="scss" scoped>
	.switch-wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: $spacing-rel-small;
		font-size: $font-size-small;
	}

	.switch {
		position: relative;
		width: 36px;
		height: 24px;
		margin: 0 $spacing-abs-small / 2;

		// Hide checkbox
		input {
			opacity: 0;
			width: 0;
			height: 0;

			&:checked + .toggle:before {
				transform: translateX(12px);
			}
		}

		&:hover .toggle:before {
			background-color: $color-main-light;
		}
	}

	.toggle {
		position: absolute;
		width: 36px;
		height: 24px;
		top: 0;
		right: 0;
		bottom: 0;
		left: 0;
		background-color: $color-background-footer;
		border-radius: 34px;
		transition: 0.2s;

		&:before {
			position: absolute;
			content: "";
			width: 16px;
			height: 16px;
			left: 4px;
			bottom: 4px;
			background-color: $color-main;
			border-radius: 50%;
			transition: 0.2s;
		}
	}
</style>
