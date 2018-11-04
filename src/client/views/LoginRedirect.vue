<template>
	<div class="login-redirect centered">
		<Error
			v-if="err"
			message="An error occurred while logging in."
			display-home-link
		/>
		<div v-else>
			<p>Logging in...</p>
		</div>
	</div>
</template>

<script>
	import Error from '../components/Error.vue';

	export default {
		components: {
			Error,
		},
		data() {
			return {
				err: false,
			};
		},
		created() {
			// Read query parameters from URL
			const url = new URL(window.location.href);
			const oauthCode = url.searchParams.get('code');
			const oauthState = url.searchParams.get('state');

			// Verify OAuth state
			const oauthStateStored = localStorage.getItem('oauthState');
			if (!oauthStateStored) {
				this.err = true;
				console.error('Could not retrieve OAuth 2 state parameter from LocalStorage');
				return;
			}
			if (oauthState !== oauthStateStored) {
				this.err = true;
				console.error('Incorrect OAuth 2 state parameter');
				return;
			}
			localStorage.removeItem('oauthState');

			// Save code and redirect to Athlete page
			localStorage.setItem('oauthCode', oauthCode);
			this.$router.push('/athlete');
		},
	};
</script>
