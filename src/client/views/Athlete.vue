<template>
	<div class="athlete">
		<!-- Error -->
		<main v-if="error">
			TODO error
		</main>
		<!-- Loading -->
		<main v-else-if="isLoading">
			TODO loading spinner
		</main>
		<!-- Finished loading -->
		<main v-else>
			TODO profile, stats, and predictions
		</main>
	</div>
</template>

<script>
	import Header from '../components/Header.vue';

	export default {
		components: {
			Header,
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
