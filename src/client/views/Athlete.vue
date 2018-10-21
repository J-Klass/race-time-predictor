<template>
	<div class="athlete">
		<h1>Athlete</h1>
		<p>{{ profile }}</p>
	</div>
</template>

<script>
	export default {
		name: 'Athlete',
		data() {
			return {
				profile: {},
				predictions: {}
			};
		},
		created() {
			// Load oAuth code from LocalStorage, redirect to start page if it doesn't exist
			const oauthCode = localStorage.getItem('oauthCode');
			if (!oauthCode) {
				this.$router.push('/');
			}

			// Fetch athlete profile
			window.fetch(`/api/profile?code=${oauthCode}`)
				.then(res => res.json())
				.then((json) => {
					if (json && json.success) {
						this.profile = json.data;
					} else {
						// TODO: Error handling
					}
				})
				.catch((err) => {
					// TODO: Error handling
					console.error(err);
			});
		}
	};
</script>
