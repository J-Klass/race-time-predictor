<template>
	<div class="athlete centered">
		<!-- Error -->
		<Error
			v-if="error"
			message="Error loading athlete profile/predictions"
			display-home-link
		/>

		<!-- Loading -->
		<Spinner v-else-if="isLoading" />

		<!-- Finished loading -->
		<template v-else>
			<Profile
				:first-name="data.profile.firstName"
				:last-name="data.profile.lastName"
				:img-url="data.profile.imgUrl"
				:profile-url="data.profile.profileUrl"
			/>
			<UnitSwitch
				:use-metric-system="useMetricSystem"
				@toggle-metric-system="toggleMetricSystem"
			/>

			<Separator title="Predictions" />
			<Predictions
				:predictions="data.predictions"
				:use-metric-system="useMetricSystem"
			/>
			<PredictionsChart
				:chart-data="data.predictions_graph"
				:use-metric-system="useMetricSystem"
			/>

			<Separator title="Stats" />
			<Stats :stats="data.stats" />
			<StatsChart
				:chart-data="data.chart"
				:use-metric-system="useMetricSystem"
			/>
		</template>
	</div>
</template>

<script>
	import Error from '../components/general/Error.vue';
	import Header from '../components/Header.vue';
	import Predictions from '../components/athlete/Predictions.vue';
	import PredictionsChart from '../components/athlete/PredictionsChart';
	import Profile from '../components/athlete/Profile.vue';
	import Separator from '../components/general/Separator.vue';
	import Spinner from '../components/general/Spinner.vue';
	import Stats from '../components/athlete/Stats.vue';
	import StatsChart from '../components/athlete/StatsChart.vue';
	import UnitSwitch from '../components/athlete/UnitSwitch.vue';

	export default {
		components: {
			Error,
			Header,
			Predictions,
			PredictionsChart,
			Profile,
			Separator,
			Spinner,
			Stats,
			StatsChart,
			UnitSwitch,
		},
		data() {
			return {
				data: {},
				error: false,
				isLoading: true,
				oauthCode: '',
				useMetricSystem: window.navigator.language !== 'en-US',
			};
		},
		created() {
			this.checkOauthCode();
			this.fetchData();
		},
		methods: {
			checkOauthCode() {
				// Load OAuth code from LocalStorage, redirect to start page if it doesn't exist
				this.oauthCode = localStorage.getItem('oauthCode');
				if (!this.oauthCode) {
					this.$router.push('/');
				}
			},
			fetchData() {
				// Fetch athlete profile, stats, and predictions
				return window.fetch(`/api/athlete?code=${this.oauthCode}`)
					.then(res => res.json())
					.then((json) => {
						this.isLoading = false;
						if (json.success) {
							this.data = json.data;
							this.error = false;
						} else {
							console.error(json.errorType);
							this.error = true;
						}
					})
					.catch((err) => {
						console.error(err);
						this.error = true;
						this.isLoading = false;
				});
			},
			toggleMetricSystem() {
				this.useMetricSystem = !this.useMetricSystem;
			},
		},
	};
</script>
