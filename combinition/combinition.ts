import { strict as assert } from 'assert';

/** 要組合的對象 */
export interface Item {
	/** 種類，不得重複 */
	type: string;
	/** 數量，需為正整數 */
	amount: number;
}

export interface PickedItem extends Item {
	picked: number
}

function backTracking(items: Array<PickedItem>, pick: number, res: Array<Array<Item>>, startIndex: number) {
	if (pick === 0) {
		let currList: Array<Item> = items
			.filter(item => item.picked > 0)
			.map(item => ({ type: item.type, amount: item.picked }));
		res.push(currList);
		return;
	}

	for (let i = startIndex; i < items.length; i++) {
		let item = items[i];
		if (item.amount > 0) {
			items[i].amount -= 1;
			items[i].picked += 1;
			backTracking(items, pick - 1, res, i);
			items[i].amount += 1;
			items[i].picked -= 1;
		}
	}
}

function combination<T extends Item = Item>(items: Array<T>, pick: number): Array<Array<T>> {
	let res: Array<Array<T>> = [];
	let pickedItems = items.map(item => ({
		type: item.type,
		amount: item.amount,
		picked: 0,
	}));
	backTracking(pickedItems, pick, res, 0);
	return res;
}



let result = combination([
	{ type: 'Apple', amount: 2 },
	{ type: 'Banana', amount: 3 },
	{ type: 'Cat', amount: 2 },
	{ type: 'Dog', amount: 4 },
	{ type: 'Egg', amount: 1 },
], 12);
assert(result.length === 1);

result = combination([
	{ type: 'Apple', amount: 2 },
	{ type: 'Banana', amount: 3 },
	{ type: 'Cat', amount: 2 },
	{ type: 'Dog', amount: 4 },
	{ type: 'Egg', amount: 1 },
], 7);
result.forEach(ans => {
	const sum = ans.reduce((prev, curr) => {
		return prev + curr.amount;
	}, 0);
	assert(sum === 7);
});

result = combination([
	{ type: 'Apple', amount: 2 },
	{ type: 'Banana', amount: 3 },
	{ type: 'Cat', amount: 2 },
	{ type: 'Dog', amount: 4 },
	{ type: 'Egg', amount: 1 },
], 13);
assert(result.length === 0);

result = combination([
	{ type: 'Apple', amount: 1 },
	{ type: 'Banana', amount: 2 },
	{ type: 'Cat', amount: 3 },
], 2);
/** A1B1 A1C1 B1C1 B2 C2 */
assert(result.length === 5);