/**
 * Round to 2 decimals
 */
function round(number) {
	return Math.round(number * 100) / 100;
}


/**
 * Convert meters to kilometers
 */
function mToKm(m) {
	return m / 1000;
}


/**
 * Convert meters to miles
 */
function mToMiles(m) {
	return m * 0.000621371192;
}


/**
 * Convert meters to kilometers or miles
 */
export function mToString(m, useMetricSystem) {
	if (useMetricSystem) {
		// Convert to km
		const km = mToKm(m);
		return `${round(km)} km`; // Round to 2 decimals
	}
	// Convert to miles
	const mi = mToMiles(m);
	return `${round(mi)} mi`;
}


/**
 * Convert milliseconds to a readable time string
 */
export function msToString(ms, includeSeconds) {
	const date = new Date(ms);
	const s = date.getSeconds();
	const min = date.getMinutes();
	const h = date.getUTCHours();
	let dateStr = '';
	if (includeSeconds) {
		dateStr = `${s}s`;
	}
	if (min > 0) {
		dateStr = `${min}m ${dateStr}`;
		if (h > 0) {
			dateStr = `${h}h ${dateStr}`;
		}
	}
	return dateStr;
}


/**
 * Convert to speed per km/mi
 */
export function getSpeedString(m, ms, useMetricSystem) {
	// Calculate ms per distance unit (km or mi)
	const distUnit = useMetricSystem ? mToKm(m) : mToMiles(m);
	const msPerDistUnit = ms / distUnit;

	// Convert to speed string
	const date = new Date(msPerDistUnit);
	const s = date.getSeconds();
	const min = date.getMinutes();
	return `${min}:${s}/${useMetricSystem ? 'km' : 'mi'}`;
}
