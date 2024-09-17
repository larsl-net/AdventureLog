import inspirationalQuotes from './json/quotes.json';
import type { Adventure, Checklist, Collection, Note, Transportation, User } from './types';

export function getRandomQuote() {
	const quotes = inspirationalQuotes.quotes;
	const randomIndex = Math.floor(Math.random() * quotes.length);
	let quoteString = quotes[randomIndex].quote;
	let authorString = quotes[randomIndex].author;
	return '"' + quoteString + '" - ' + authorString;
}

export function getFlag(size: number, country: string) {
	return `https://flagcdn.com/h${size}/${country}.png`;
}

export function checkLink(link: string) {
	if (link.startsWith('http://') || (link.startsWith('https://') && link.indexOf('.') !== -1)) {
		return link;
	} else {
		return 'http://' + link + '.com';
	}
}

export async function exportData() {
	let res = await fetch('/api/adventures/all');
	let adventures = (await res.json()) as Adventure[];

	res = await fetch('/api/collections/all');
	let collections = (await res.json()) as Collection[];

	res = await fetch('/api/visitedregion');
	let visitedRegions = await res.json();

	const data = {
		adventures,
		collections,
		visitedRegions
	};

	const blob = new Blob([JSON.stringify(data)], { type: 'application/json' });
	return URL.createObjectURL(blob);
}

export function isValidUrl(url: string) {
	try {
		new URL(url);
		return true;
	} catch (err) {
		return false;
	}
}

export function groupAdventuresByDate(
	adventures: Adventure[],
	startDate: Date,
	numberOfDays: number
): Record<string, Adventure[]> {
	const groupedAdventures: Record<string, Adventure[]> = {};

	// Initialize all days in the range
	for (let i = 0; i < numberOfDays; i++) {
		const currentDate = new Date(startDate);
		currentDate.setUTCDate(startDate.getUTCDate() + i);
		const dateString = currentDate.toISOString().split('T')[0];
		groupedAdventures[dateString] = [];
	}

	adventures.forEach((adventure) => {
		if (adventure.date) {
			const adventureDate = new Date(adventure.date).toISOString().split('T')[0];
			if (adventure.end_date) {
				const endDate = new Date(adventure.end_date).toISOString().split('T')[0];

				// Loop through all days and include adventure if it falls within the range
				for (let i = 0; i < numberOfDays; i++) {
					const currentDate = new Date(startDate);
					currentDate.setUTCDate(startDate.getUTCDate() + i);
					const dateString = currentDate.toISOString().split('T')[0];

					// Include the current day if it falls within the adventure date range
					if (dateString >= adventureDate && dateString <= endDate) {
						if (groupedAdventures[dateString]) {
							groupedAdventures[dateString].push(adventure);
						}
					}
				}
			} else if (groupedAdventures[adventureDate]) {
				// If there's no end date, add adventure to the start date only
				groupedAdventures[adventureDate].push(adventure);
			}
		}
	});

	return groupedAdventures;
}

export function groupTransportationsByDate(
	transportations: Transportation[],
	startDate: Date,
	numberOfDays: number
): Record<string, Transportation[]> {
	const groupedTransportations: Record<string, Transportation[]> = {};

	// Initialize all days in the range
	for (let i = 0; i < numberOfDays; i++) {
		const currentDate = new Date(startDate);
		currentDate.setUTCDate(startDate.getUTCDate() + i);
		const dateString = currentDate.toISOString().split('T')[0];
		groupedTransportations[dateString] = [];
	}

	transportations.forEach((transportation) => {
		if (transportation.date) {
			const transportationDate = new Date(transportation.date).toISOString().split('T')[0];
			if (transportation.end_date) {
				const endDate = new Date(transportation.end_date).toISOString().split('T')[0];

				// Loop through all days and include transportation if it falls within the range
				for (let i = 0; i < numberOfDays; i++) {
					const currentDate = new Date(startDate);
					currentDate.setUTCDate(startDate.getUTCDate() + i);
					const dateString = currentDate.toISOString().split('T')[0];

					// Include the current day if it falls within the transportation date range
					if (dateString >= transportationDate && dateString <= endDate) {
						if (groupedTransportations[dateString]) {
							groupedTransportations[dateString].push(transportation);
						}
					}
				}
			} else if (groupedTransportations[transportationDate]) {
				// If there's no end date, add transportation to the start date only
				groupedTransportations[transportationDate].push(transportation);
			}
		}
	});

	return groupedTransportations;
}

export function groupNotesByDate(
	notes: Note[],
	startDate: Date,
	numberOfDays: number
): Record<string, Note[]> {
	const groupedNotes: Record<string, Note[]> = {};

	// Initialize all days in the range
	for (let i = 0; i < numberOfDays; i++) {
		const currentDate = new Date(startDate);
		currentDate.setUTCDate(startDate.getUTCDate() + i);
		const dateString = currentDate.toISOString().split('T')[0];
		groupedNotes[dateString] = [];
	}

	notes.forEach((note) => {
		if (note.date) {
			const noteDate = new Date(note.date).toISOString().split('T')[0];

			// Add note to the appropriate date group if it exists
			if (groupedNotes[noteDate]) {
				groupedNotes[noteDate].push(note);
			}
		}
	});

	return groupedNotes;
}

export function groupChecklistsByDate(
	checklists: Checklist[],
	startDate: Date,
	numberOfDays: number
): Record<string, Checklist[]> {
	const groupedChecklists: Record<string, Checklist[]> = {};

	// Initialize all days in the range
	for (let i = 0; i < numberOfDays; i++) {
		const currentDate = new Date(startDate);
		currentDate.setUTCDate(startDate.getUTCDate() + i);
		const dateString = currentDate.toISOString().split('T')[0];
		groupedChecklists[dateString] = [];
	}

	checklists.forEach((checklist) => {
		if (checklist.date) {
			const checklistDate = new Date(checklist.date).toISOString().split('T')[0];

			// Add checklist to the appropriate date group if it exists
			if (groupedChecklists[checklistDate]) {
				groupedChecklists[checklistDate].push(checklist);
			}
		}
	});

	return groupedChecklists;
}

export function continentCodeToString(code: string) {
	switch (code) {
		case 'AF':
			return 'Africa';
		case 'AN':
			return 'Antarctica';
		case 'AS':
			return 'Asia';
		case 'EU':
			return 'Europe';
		case 'NA':
			return 'North America';
		case 'OC':
			return 'Oceania';
		case 'SA':
			return 'South America';
		default:
			return 'Unknown';
	}
}
