/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let max_profit=0;
    let min_price=prices[0];
    for (let  price of prices){
        if (price<min_price){
            min_price=price;
        }
        else {
            let profit=price-min_price;
            max_profit=Math.max(max_profit,profit);
        }

    }
    return max_profit;
    
};