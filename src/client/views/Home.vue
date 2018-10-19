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
		}
	};
</script>
