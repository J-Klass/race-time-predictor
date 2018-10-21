<template>
	<a
		:href="loginUrl"
		class="button"
	>
		Log in with Strava
	</a>
</template>

<script>
	const apiUrl = 'https://www.strava.com/oauth/authorize';
	const baseUrl = document.location.origin;
	const clientId = process.env.VUE_APP_CLIENT_ID;
	const randomString = Math.random().toString().substring(2);

	export default {
		name: 'LoginLink',
		data() {
			return {
				oauthState: randomString
			};
		},
		computed: {
			loginUrl() {
				// Generate URL to Strava login site
				const loginUrl = new URL(apiUrl);
				const urlParams = {
					approval_prompt: 'auto',
					client_id: clientId,
					redirect_uri: `${baseUrl}/login-redirect`,
					response_type: 'code',
					scope: 'read_all',
					state: this.oauthState
				};
				Object.entries(urlParams).forEach(([key, value]) => {
					loginUrl.searchParams.append(key, value);
				});
				return loginUrl.toString();
			}
		},
		created() {
			// Save OAuth code in LocalStorage
			localStorage.setItem('oauthState', this.oauthState);
		}
	};
</script>
