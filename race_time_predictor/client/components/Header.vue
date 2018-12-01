<template>
	<header>
		<h1 class="centered">
			<router-link
				to="/"
				class="logo-link"
			>
				<icon-base
					title="Race Time Predictor"
					view-box="0 0 1123 362"
					class="logo"
				>
					<logo />
				</icon-base>
			</router-link>
		</h1>
	</header>
</template>

<script>
	import IconBase from './icons/IconBase.vue';
	import Logo from './icons/svg/Logo.vue';

	export default {
		components: {
			IconBase,
			Logo,
		},
	};
</script>

<style lang="scss" scoped>
	header {
		display: flex;
		align-items: center;
		width: 100%;
		height: 500px;
		max-height: 60vh;
		background: $color-background-header url("../assets/header-background.jpg") no-repeat center;
		background-size: cover;
	}

	h1 {
		text-align: center;
	}

	.logo-link {
		display: inline-block;
		width: 450px;
		max-width: 100%;
	}
</style>
