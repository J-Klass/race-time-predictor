<template>
	<div class="home">
		<Hero />
		<main>
			<Feature
				icon-position="left"
				text="Get time estimates for your next run. Race Time Predictor predicts the time for 5Ks,
					10Ks, half marathons, marathons, or any distance you choose."
			>
				<icon-base
					:height="iconHeight"
					view-box="0 0 48 48"
				>
					<icon-clock />
				</icon-base>
			</Feature>

			<Feature
				icon-position="right"
				text="Using your past activities and machine learning, Race Time Predictor learns about your
					fitness level and predicts times for future races."
			>
				<icon-base
					:height="iconHeight"
					view-box="0 0 48 48"
				>
					<icon-m-l />
				</icon-base>
			</Feature>

			<Feature
				icon-position="left"
				text="Race Time Predictor is powered by Strava. It lets you easily import your past runs for
					its calculations."
			>
				<icon-base
					:height="iconHeight"
					view-box="0 0 48 48"
				>
					<icon-scatter-plot />
				</icon-base>
			</Feature>

			<Feature
				icon-position="right"
				text="We care about your privacy and don't store your activity data."
			>
				<icon-base
					:height="iconHeight"
					view-box="0 0 48 48"
				>
					<icon-lock />
				</icon-base>
			</Feature>
		</main>
		<LoginLink />
		<Footer />
	</div>
</template>

<script>
	import Footer from '../components/Footer.vue';
	import Hero from '../components/home/Hero.vue';
	import LoginLink from '../components/home/LoginBox.vue';
	import Feature from '../components/home/Feature.vue';
	import IconBase from '../components/icons/IconBase.vue';
	import IconClock from '../components/icons/svg/IconClock.vue';
	import IconLock from '../components/icons/svg/IconLock.vue';
	import IconML from '../components/icons/svg/IconML.vue';
	import IconScatterPlot from '../components/icons/svg/IconScatterPlot.vue';

	export default {
		components: {
			IconBase,
			IconClock,
			IconLock,
			IconML,
			IconScatterPlot,
			Feature,
			Footer,
			Hero,
			LoginLink,
		},
		data() {
			return {
				iconHeight: 100,
			};
		},
		created() {
			// If OAuth code is found in LocalStorage, redirect to athlete page
			if (localStorage.getItem('oauthCode')) {
				this.$router.push('/athlete');
			}
		},
	};
</script>
