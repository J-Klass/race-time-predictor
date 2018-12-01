<script>
	/* eslint-disable camelcase */

	import { Scatter } from 'vue-chartjs';
	import { mToString, msToString } from '../../utils';

	const fontFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"';

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
								callback: m => mToString(m, this.useMetricSystem),
								fontFamily,
							},
						}],
						yAxes: [{
							ticks: {
								beginAtZero: true,
								callback: ms => msToString(ms, false),
								fontFamily,
							},
						}],
					},
					tooltips: {
						callbacks: {
							label: tooltipItem => mToString(tooltipItem.xLabel, this.useMetricSystem),
							afterLabel: tooltipItem => msToString(tooltipItem.yLabel, true),
						},
					},
				});
			},
		},
	};
</script>
