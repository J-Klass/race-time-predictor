const path = require('path');

module.exports = {
	css: {
		loaderOptions: {
			sass: {
				data: `
					@import "${path.resolve(__dirname)}/race_time_predictor/client/styles/_variables.scss";
					@import "${path.resolve(__dirname)}/race_time_predictor/client/styles/_mixins.scss";
				`,
			},
		},
	},
	devServer: {
		proxy: {
			'/api': {
				target: 'http://localhost:5000',
			},
		},
	},
};
