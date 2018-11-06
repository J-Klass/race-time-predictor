<template>
	<div class="login-box">
		<p>Get your predictions now – it's completely free!</p>
		<a
			:href="loginUrl"
			class="login-link"
		>
			<icon-base
				title="Connect with Strava"
				height="60"
				view-box="0 0 193 48"
			>
				<icon-connect />
			</icon-base>
		</a>
	</div>
</template>

<script>
	import IconBase from '../icons/IconBase.vue';
	import IconConnect from '../icons/svg/IconConnect.vue';

	const apiUrl = 'https://www.strava.com/oauth/authorize';
	const baseUrl = document.location.origin;
	const clientId = process.env.VUE_APP_CLIENT_ID;
	const randomString = Math.random().toString().substring(2);

	export default {
		components: {
			IconBase,
			IconConnect,
		},
		data() {
			return {
				oauthState: randomString,
			};
		},
		computed: {
			loginUrl() {
				// If OAuth code is found in LocalStorage, point to athlete page
				if (localStorage.getItem('oauthCode')) {
					return '/athlete';
				}

				// Generate URL to Strava login site
				const loginUrl = new URL(apiUrl);
				const urlParams = {
					approval_prompt: 'auto',
					client_id: clientId,
					redirect_uri: `${baseUrl}/login-redirect`,
					response_type: 'code',
					scope: 'activity:read_all,profile:read_all',
					state: this.oauthState,
				};
				Object.entries(urlParams).forEach(([key, value]) => {
					loginUrl.searchParams.append(key, value);
				});
				return loginUrl.toString();
			},
		},
		created() {
			// Save OAuth code in LocalStorage
			localStorage.setItem('oauthState', this.oauthState);
		},
	};
</script>

<style scoped>
	.login-box {
		padding: var(--spacing-rel-large);
		background: var(--color-background-header);
		font-weight: var(--font-weight-semibold);
		text-align: center;
	}

	.login-link {
		display: inline-block;
		margin-top: var(--spacing-abs-small);
		color: var(--color-strava);
	}

	.login-link:hover {
		color: var(--color-strava-dark);
	}
</style>
