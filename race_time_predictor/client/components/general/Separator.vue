<template>
	<div
		v-if="title"
		class="separator small-text"
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

<style lang="scss" scoped>
	hr,
	.separator::before,
	.separator::after {
		border: 0;
		border-bottom: 1px solid $color-text-underline;
	}

	hr {
		@include small-screen {
			margin: $spacing-rel-large 0;
		}
		@include large-screen {
			margin: $spacing-rel-small 0;
		}
	}

	.separator {
		display: flex;
		align-items: center;
		text-align: center;
		color: $color-text-faded;
		text-transform: uppercase;
		margin: $spacing-rel-large 0 $spacing-rel-small 0;

		&::before,
		&::after {
			content: '';
			flex: 1;
		}

		&::before {
			margin-right: 1em;
		}

		&::after {
			margin-left: 1em;
		}
	}
</style>
