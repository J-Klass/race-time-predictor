const locale = window.navigator.language;


/**
 * Round to 2 decimals
 */
function round(number) {
	return Math.round(number * 100) / 100;
}


/**
 * Convert meters to km or mi (depending on locale unit)
 */
export function mToLocaleUnit(m) {
	if (locale === 'en-US') {
		const mi = m * 0.000621371192;
		return `${round(mi)} mi`;
	}
	// Convert to km
	const km = m / 1000;
	return `${round(km)} km`; // Round to 2 decimals
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
