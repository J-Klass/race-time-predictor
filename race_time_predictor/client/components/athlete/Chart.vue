<script>
	/* eslint-disable camelcase */

	import Chart from 'chart.js';
	import { Scatter } from 'vue-chartjs';
	import { dateToStr, getSpeedString, mToKmOrMi, mToMOrFt, msToString } from '../../utils';

	Chart.defaults.global.defaultFontFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"';

	export default {
		extends: Scatter,
		props: {
			chartData: {
				type: Array,
				default: () => [],
			},
			// Width and height need to be set to null to override the defaults (400) set by vue-chartjs.
			// These defaults break the aspectRatio option
			width: {
				type: Number,
				default: null,
			},
			height: {
				type: Number,
				default: null,
			},
			useMetricSystem: {
				type: Boolean,
				default: null,
			},
		},
		computed: {
			series() {
				return this.chartData.map(({ distance, moving_time }) => ({
					x: distance,
					y: moving_time * 1000,
				}));
			},
		},
		watch: {
			useMetricSystem() {
				this.render();
			},
		},
		mounted() {
			this.render();
		},
		methods: {
			render() {
				this.renderChart({
					datasets: [{
						data: this.series,
					}],
				}, {
					animation: false,
					aspectRatio: 2,
					elements: {
						point: {
							backgroundColor: 'rgba(107, 129, 218, 0.6)',
							hoverRadius: 10,
							radius: 6,
						},
					},
					legend: {
						display: false,
					},
					scales: {
						xAxes: [{
							ticks: {
								beginAtZero: true,
								callback: m => mToKmOrMi(m, this.useMetricSystem),
							},
						}],
						yAxes: [{
							ticks: {
								beginAtZero: true,
								callback: ms => msToString(ms, false),
							},
						}],
					},
					tooltips: {
						callbacks: {
							title: tooltipItem => mToKmOrMi(tooltipItem[0].xLabel, this.useMetricSystem),
							label: () => null,
							afterLabel: (tooltipItem) => {
								const dataEntry = this.chartData[tooltipItem.index];
								const distance = tooltipItem.xLabel;
								const time = tooltipItem.yLabel;

								const timeStr = msToString(time, true);
								const speedStr = getSpeedString(distance, time, this.useMetricSystem);
								const elevationStr = mToMOrFt(dataEntry.total_elevation_gain, this.useMetricSystem);
								const dateStr = dateToStr(dataEntry.start_date);
								return `Time: ${timeStr}\nSpeed: ${speedStr}\nElevation gain: ${elevationStr}\nDate: ${dateStr}`;
							},
						},
						displayColors: false,
						backgroundColor: '#ECECEC',
						titleFontSize: 16,
						titleFontColor: '#1D1D1D',
						bodyFontColor: '#1D1D1D',
						bodyFontSize: 13,
						xPadding: 15,
						yPadding: 15,
					},
				});
			},
		},
	};
</script>
