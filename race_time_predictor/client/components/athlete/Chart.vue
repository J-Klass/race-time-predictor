<script>
	import { Scatter } from 'vue-chartjs';
	import { mToLocaleUnit, msToString } from '../../utils';

	const fontFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"';

	export default {
		extends: Scatter,
		props: {
			chartData: {
				type: Object,
				default: () => {},
			},
		},
		computed: {
			series() {
				const data = [];
				const { distances, times } = this.chartData;
				distances.forEach((distance, index) => {
					const time = times[index] * 1000;
					data.push({
						x: distance,
						y: time,
					});
				});
				return data;
			},
		},
		mounted() {
			this.renderChart({
				datasets: [{
					data: this.series,
				}],
			}, {
				// TODO aspect ratio
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
							callback: mToLocaleUnit,
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
						label(tooltipItem) {
							return mToLocaleUnit(tooltipItem.xLabel);
						},
						afterLabel(tooltipItem) {
							return msToString(tooltipItem.yLabel, true);
						},
					},
				},
			});
		},
	};
</script>
