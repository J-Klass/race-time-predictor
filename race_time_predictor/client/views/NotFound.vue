<template>
	<div class="not-found centered">
		<Error
			message="The page you requested could not be found."
			display-home-link
		/>
	</div>
</template>

<script>
	import Error from '../components/general/Error.vue';

	export default {
		components: {
			Error,
		},
	};
</script>
