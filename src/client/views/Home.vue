<template>
	<div class="home">
		<LoginLink />
	</div>
</template>

<script>
	import LoginLink from '@/client/components/LoginLink.vue';

	export default {
		name: 'Home',
		components: {
			LoginLink
		},
		created() {
			// If OAuth code is found in LocalStorage, redirect to athlete page
			if (localStorage.getItem('oauthCode')) {
				this.$router.push('/athlete');
			}
		}
	};
</script>
