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


export function mToKm(m) {
	const km = m / 1000;
	return Math.round(km * 100) / 100; // Round to 2 decimals
}
