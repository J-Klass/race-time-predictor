<template>
	<div
		v-if="title"
		class="separator"
	>
		{{ title }}
	</div>
	<hr v-else>
</template>

<script>
	export default {
		props: {
			title: {
				type: String,
				default: '',
			},
		},
	};
</script>

<style>
	hr,
	.separator::before,
	.separator::after {
		border: 0;
		border-bottom: 1px solid var(--color-text-underline);
	}

	hr {
		margin: var(--spacing-rel-small) 0;
	}

	.separator {
		display: flex;
		align-items: center;
		margin: var(--spacing-rel-large) 0 var(--spacing-rel-small) 0;
		font-size: var(--font-size-small);
		text-align: center;
		color: var(--color-text-faded);
		text-transform: uppercase;
	}

	.separator::before,
	.separator::after {
		content: '';
		flex: 1;
	}

	.separator::before {
		margin-right: 1em;
	}

	.separator::after {
		margin-left: 1em;
	}
</style>
