<template>
	<div class="home">
		<div class="centered">
			<Feature
				icon-position="left"
				text="Get time estimates for your next run. Race Time Predictor predicts the time for 5Ks,
					10Ks, half marathons, marathons, or any distance you choose."
			>
				<icon-base
					view-box="0 0 48 48"
				>
					<icon-clock />
				</icon-base>
			</Feature>
			<Separator />
			<Feature
				icon-position="right"
				text="Using your past activities and machine learning, Race Time Predictor learns about your
					fitness level and predicts times for future races."
			>
				<icon-base
					view-box="0 0 48 48"
				>
					<icon-m-l />
				</icon-base>
			</Feature>
			<Separator />
			<Feature
				icon-position="left"
				text="Race Time Predictor is powered by Strava. It lets you easily import your past runs for
					its calculations."
			>
				<icon-base
					view-box="0 0 48 48"
				>
					<icon-scatter-plot />
				</icon-base>
			</Feature>
			<Separator />
			<Feature
				icon-position="right"
				text="We care about your privacy and don't store your activity data."
			>
				<icon-base
					view-box="0 0 48 48"
				>
					<icon-lock />
				</icon-base>
			</Feature>
		</div>
		<LoginBox />
	</div>
</template>

<script>
	import Footer from '../components/Footer.vue';
	import Hero from '../components/Header.vue';
	import LoginBox from '../components/home/LoginBox.vue';
	import Feature from '../components/home/Feature.vue';
	import IconBase from '../components/icons/IconBase.vue';
	import IconClock from '../components/icons/svg/IconClock.vue';
	import IconLock from '../components/icons/svg/IconLock.vue';
	import IconML from '../components/icons/svg/IconML.vue';
	import IconScatterPlot from '../components/icons/svg/IconScatterPlot.vue';
	import Separator from '../components/general/Separator.vue';

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
			LoginBox,
			Separator,
		},
	};
</script>
