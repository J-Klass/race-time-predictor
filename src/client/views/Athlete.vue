<template>
	<div class="athlete centered">
		<!-- Error -->
		<template v-if="error">
			TODO error
		</template>
		<!-- Loading -->
		<template v-else-if="isLoading">
			TODO loading spinner
		</template>
		<!-- Finished loading -->
		<template v-else>
			<Profile
				:first-name="data.profile.firstName"
				:last-name="data.profile.lastName"
				:img-url="data.profile.imgUrl"
				:profile-url="data.profile.profileUrl"
			/>
			<Stats />
			<hr>
			<Predictions :predictions="data.predictions" />
			<p>TODO graph</p>
		</template>
	</div>
</template>

<script>
	import Header from '../components/Header.vue';
	import Predictions from '../components/athlete/Predictions.vue';
	import Profile from '../components/athlete/Profile.vue';
	import Stats from '../components/athlete/Stats.vue';

	export default {
		components: {
			Header,
			Predictions,
			Profile,
			Stats,
		},
		data() {
			return {
				data: {},
				error: false,
				isLoading: true,
				oauthCode: '',
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
						if (json && json.success) {
							this.data = json.data;
							this.error = false;
						} else {
							console.error('Error in JSON response');
							this.error = true;
						}
					})
					.catch((err) => {
						console.error(err);
						this.error = true;
						this.isLoading = false;
				});
			},
		},
	};
</script>
