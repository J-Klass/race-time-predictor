<script>
	/* eslint-disable camelcase */

	import { Line } from 'vue-chartjs';
	import { dateToStr, getSpeedString, mToKmOrMi, mToMOrFt, msToString } from '../../utils';

	export default {
		extends: Line,
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
				this.renderChart(
					{
						labels: this.chartData.map(({ distance }) => distance),
						datasets: [
							{
								label: 'Data One',
								backgroundColor: 'rgba(107, 129, 218, 0.6)',
								data: this.chartData.map(({ time }) => time * 1000),
							},
						],
					},
					{
						animation: false,
						aspectRatio: 2,
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
								title: tooltipItem => tooltipItem[0].xLabel,
								label: () => null,
								afterLabel: (tooltipItem) => {
									const time = tooltipItem.yLabel;
									const timeStr = msToString(time);
									return `Time: ${timeStr}`;
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
