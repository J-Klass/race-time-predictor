<template>
	<div class="error">
		<icon-base
			height="50"
			view-box="0 0 24 24"
			class="error-icon"
		>
			<icon-error />
		</icon-base>
		<p>{{ message }}</p>
		<router-link
			v-if="displayHomeLink"
			to="/"
		>
			Return to start page
		</router-link>
	</div>
</template>

<script>
	import IconBase from './icons/IconBase.vue';
	import IconError from './icons/svg/IconError.vue';

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
			displayHomeLink: {
				type: Boolean,
				default: false,
			},
		},
	};
</script>

<style scoped>
	.error {
		text-align: center;
	}

	.error-icon {
		color: var(--color-error);
	}
</style>
