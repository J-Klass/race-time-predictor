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

<style scoped>
	.switch-wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: var(--spacing-rel-small);
		font-size: var(--font-size-small);
	}

	.switch {
		position: relative;
		width: 36px;
		height: 24px;
		margin: 0 calc(var(--spacing-abs-small) / 2);
	}

	/* Hide checkbox */
	.switch input {
		opacity: 0;
		width: 0;
		height: 0;
	}

	.toggle {
		position: absolute;
		width: 36px;
		height: 24px;
		top: 0;
		right: 0;
		bottom: 0;
		left: 0;
		background-color: var(--color-background-footer);
		border-radius: 34px;
		transition: 0.2s;
	}

	.toggle:before {
		position: absolute;
		content: "";
		width: 16px;
		height: 16px;
		left: 4px;
		bottom: 4px;
		background-color: var(--color-main);
		border-radius: 50%;
		transition: 0.2s;
	}

	.switch:hover .toggle:before {
		background-color: var(--color-main-light);
	}

	input:checked + .toggle:before {
		transform: translateX(12px);
	}
</style>
