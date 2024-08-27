import { strict as assert } from 'assert';

/** 要組合的對象 */
export interface Item {
	/** 種類，不得重複 */
	type: string;
	/** 數量，需為正整數 */
	amount: number;
}

/**
 * 列出所有組合
 * @param items 要撿的東西
 * @param pick 要挑幾個
 */
function combination<T extends Item = Item> (items: Array<T>, pick: number): Array<Array<T>> {
	const n = items.length;
    // create dp array to store combinition
    const dp: Array<Array<Array<T>>> = Array.from({ length: pick + 1 }, () => []);
    
    dp[0] = [[]]; // 0 pick up will have empty array
    for (let i = 0; i < n; i++) {
        const item = items[i];
        for (let p = pick; p >= 1; p--) {
            for (let k = 1; k <= item.amount && k <= p; k++) {
                const previousCombinations = dp[p - k]; // p - k will get combinitions exclude curr pickup
                const newCombinations = previousCombinations.map(comb => {
                    return [...comb, { ...item, amount: k }]; // add curr picku into prev combinition
                });
                dp[p].push(...newCombinations);
            }
        }
    }
    return dp[pick];
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