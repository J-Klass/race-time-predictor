<template>
	<div class="profile">
		<a
			:href="profileUrl"
			target="_blank"
			rel="noopener noreferrer"
		>
			<img
				:src="imgUrlWithDefault"
				alt="Profile picture"
				class="profile-image"
			>
		</a>
		<div>
			<h2>{{ firstName }} {{ lastName }}</h2>
			<a
				href=""
				class="sign-out-link small-text"
				@click="signOut"
			>
				Sign out
			</a>
		</div>
	</div>
</template>

<script>
	import placeholderImg from '../../assets/profile-img-placeholder.png';

	const DEFAULT_IMG_URL = 'avatar/athlete/large.png';

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

<style lang="scss" scoped>
	.profile {
		@include small-screen {
			text-align: center;
		}
		@include large-screen {
			display: flex;
			align-items: center;
			justify-content: center;
		}
	}

	.profile-image {
		width: 140px;
		border-radius: 50%;

		@include large-screen {
			margin-right: $spacing-abs-large;
		}
	}

	.sign-out-link {
		color: $color-text-faded;
		transition: $transition;

		&:hover {
			color: $color-text-faded-dark;
		}
	}
</style>
