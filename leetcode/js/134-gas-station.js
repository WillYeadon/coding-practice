/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */

var canCompleteCircuit = function(gas, cost) {
    let totalGas = 0;
    let totalCost = 0;
    let start = 0;
    let tank = 0;

    for(let i = 0; i < gas.length; i++) {
        totalGas += gas[i];
        totalCost += cost[i];
        tank += gas[i] - cost[i];

        // If tank is negative, the circuit is broken
        // thus the start should be atleast at the
        // next station
        if(tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }

    // There exists a solution if totalGas >= totalCost
    // guaranteed unique from question.
    if(totalGas >= totalCost) {
        return start;
    } else {
        return -1;
    }
};
