<template>
	<footer>
		<a href="https://www.strava.com/">
			<icon-base
				title="Powered by Strava"
				height="50"
				view-box="0 0 95.3 41.39"
				class="powered-by-strava"
			>
				<icon-powered-by-strava />
			</icon-base>
		</a>
		<br>
		<a href="https://github.com/J-Klass/marathon-time-predictor">
			<icon-base
				height="20"
				view-box="0 0 1024 999"
				class="icon-github"
			>
				<icon-github />
			</icon-base>
			Source code on GitHub
		</a>
	</footer>
</template>

<script>
	import IconBase from './icons/IconBase.vue';
	import IconGithub from './icons/svg/IconGithub.vue';
	import IconPoweredByStrava from './icons/svg/IconPoweredByStrava.vue';


	export default {
		components: {
			IconBase,
			IconGithub,
			IconPoweredByStrava,
		},
	};
</script>

<style scoped>
	footer {
		margin: var(--spacing-rel-small) var(--spacing-rel-large);
		font-size: var(--font-size-small);
		color: var(--color-text-faded);
		text-align: center;
	}

	a {
		display: inline-flex;
		align-items: center;
		transition: var(--transition);
	}

	a:hover {
		color: var(--color-text-faded-dark);
	}

	.powered-by-strava {
		margin-bottom: var(--spacing-abs-small);
	}

	.icon-github {
		margin: 0 6px 2px 0;
	}
</style>
