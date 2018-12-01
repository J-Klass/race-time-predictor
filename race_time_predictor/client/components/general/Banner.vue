<template>
	<div :class="`banner ${typeValidated}`">
		<icon-base
			height="25"
			view-box="0 0 24 24"
			class="error-icon"
		>
			<icon-error />
		</icon-base>
		<p>{{ message }}</p>
	</div>
</template>

<script>
	import IconBase from '../icons/IconBase.vue';
	import IconError from '../icons/svg/IconError.vue';

	export default {
		components: {
			IconBase,
			IconError,
		},
		props: {
			message: {
				type: String,
				default: 'An error occurred.',
			},
			type: {
				type: String,
				default: 'error',
			},
		},
		computed: {
			typeValidated() {
				if (this.type === 'error' || this.type === 'warning') {
					return this.type;
				}
				throw Error('Banner type prop must be one of "error" and "warning"');
			},
		},
	};
</script>

<style lang="scss" scoped>
	.banner {
		display: flex;
		align-items: center;
		padding: $spacing-abs-small;
		border-radius: 10px;

		svg {
			margin-right: $spacing-abs-small / 2;
		}

		p {
			flex: 1;
		}
	}

	.error {
		background: #F17272;
	}

	.warning {
		background: #FFD050;
	}
</style>
