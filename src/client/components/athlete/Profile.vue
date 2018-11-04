<template>
	<div class="profile">
		<img
			:src="imgUrlWithDefault"
			alt="Profile picture"
			class="profile-image"
		>
		<div>
			<h2>{{ firstName }} {{ lastName }}</h2>
			<a
				href=""
				class="sign-out-link"
				@click="signOut"
			>
				Sign out
			</a>
		</div>
	</div>
</template>

<script>
	import placeholderImg from '../../assets/profile-img-placeholder.png';

	const DEFAULT_IMG_URL = 'avatar/athlete/medium.png';

	export default {
		props: {
			firstName: {
				type: String,
				default: '',
			},
			lastName: {
				type: String,
				default: '',
			},
			imgUrl: {
				type: String,
				default: '',
			},
			profileUrl: {
				type: String,
				default: 'https://www.strava.com',
			},
		},
		computed: {
			imgUrlWithDefault() {
				if (this.imgUrl === DEFAULT_IMG_URL) {
					return placeholderImg;
				}
				return this.imgUrl;
			},
		},
		methods: {
			signOut() {
				localStorage.clear();
				this.$router.push('/');
			},
		},
	};
</script>

<style scoped>
	.profile {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.profile-image {
		margin-right: var(--spacing-abs-large);
		border-radius: 50%;
	}

	.sign-out-link {
		font-size: var(--font-size-small);
		color: var(--color-text-faded);
		transition: var(--transition);
	}

	.sign-out-link:hover {
		color: var(--color-text-faded-dark);
	}
</style>
