<template>
	<div class="chart">
		<apexcharts
			:options="chartOptions"
			:series="series"
			class="chart-wrapper"
			width="100%"
			type="scatter"
		/>
	</div>
</template>

<script>
	import VueApexCharts from 'vue-apexcharts';
	import { mToLocaleUnit, msToString } from '../../utils';

	export default {
		components: {
			apexcharts: VueApexCharts,
		},
		props: {
			chartData: {
				type: Object,
				default: () => {},
			},
		},
		data() {
			return {
				chartOptions: {
					chart: {
						fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"',
						toolbar: {
							show: false,
						},
						zoom: {
							enabled: false,
						},
					},
					colors: ['#6B81DA'],
					tooltip: {
						x: {
							formatter: s => msToString(s, true),
						},
					},
					xaxis: {
						type: 'datetime',
						min: 0,
						tickAmount: 7,
						labels: {
							formatter: s => msToString(s, false),
						},
					},
					yaxis: {
						type: 'numeric',
						labels: {
							formatter: mToLocaleUnit,
						},
					},
				},
			};
		},
		computed: {
			series() {
				const data = [];
				const { distances, times } = this.chartData;
				distances.forEach((distance, index) => {
					const time = times[index] * 1000;
					data.push({
						x: time,
						y: distance,
					});
				});
				return [{
					name: 'Distance',
					data,
				}];
			},
		},
	};
</script>

<style scoped>
	.chart-wrapper {
		width: 100%;
		max-width: 600px;
		margin: 0 auto;
	}
</style>
