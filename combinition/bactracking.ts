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
    // Base case: if no more items to pick, add the current combination to the results
    if (pick === 0) {
        let currList: Array<Item> = items
            .filter(item => item.picked > 0)  // Filter out items that have been picked
            .map(item => ({ type: item.type, amount: item.picked })); // Create a new array with picked items
        res.push(currList);  // Add the current list to the results
        return;
    }

    // Loop through each item starting from the startIndex
    for (let i = startIndex; i < items.length; i++) {
        let item = items[i];
        // If the item has any remaining amount, continue with the recursion
        if (item.amount > 0) {
            items[i].amount -= 1; // Decrease the available amount of the item
            items[i].picked += 1; // Increase the count of picked items
            backTracking(items, pick - 1, res, i); // Recursively pick the next item
            items[i].amount += 1; // Restore the item's amount (backtrack)
            items[i].picked -= 1; // Decrease the picked count (backtrack)
        }
    }
}

function combination<T extends Item = Item>(items: Array<T>, pick: number): Array<Array<T>> {
    let res: Array<Array<T>> = []; // Initialize the result array to store all combinations
    let pickedItems = items.map(item => ({
        type: item.type,    // Copy the item type
        amount: item.amount, // Copy the available amount
        picked: 0,          // Initialize picked count to 0
    }));
    backTracking(pickedItems, pick, res, 0); // Start the backtracking process
    return res; // Return the result containing all possible combinations
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