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
		<div>
			<icon-base
				height="24"
				view-box="0 0 24 24"
				class="terminal-icon"
			>
				<icon-terminal />
			</icon-base>
			<p>
				Created by
				<a href="https://github.com/J-Klass">Jonas Klass</a>
				and
				<a href="https://samuelmeuli.com">Samuel Meuli</a>
			</p>
		</div>
		<br>
		<div>
			<icon-base
				height="20"
				view-box="0 0 1024 999"
				class="github-icon"
			>
				<icon-github />
			</icon-base>
			<a href="https://github.com/J-Klass/race-time-predictor">
				Source code on GitHub
			</a>
		</div>
	</footer>
</template>

<script>
	import IconBase from './icons/IconBase.vue';
	import IconGithub from './icons/svg/IconGithub.vue';
	import IconPoweredByStrava from './icons/svg/IconPoweredByStrava.vue';
	import IconTerminal from './icons/svg/IconTerminal.vue';


	export default {
		components: {
			IconBase,
			IconGithub,
			IconPoweredByStrava,
			IconTerminal,
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

	footer > * {
		display: inline-flex;
		align-items: center;
	}

	a {
		transition: var(--transition);
	}

	a:hover {
		color: var(--color-text-faded-dark);
	}

	.terminal-icon, .github-icon {
		margin-right: var(--spacing-icon);
	}

	.github-icon {
		margin-bottom: 2px;
	}
</style>
