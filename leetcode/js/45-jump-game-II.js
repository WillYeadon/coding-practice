var jump = function(nums) {
    const length = nums.length;
    // early exit
    if (length < 2) return 0;
    
    // maxPosition is the farthest position that can be reached.
    // edge is the end of the current jump.
    let maxPosition = nums[0];
    let edge = nums[0];
    let jumps = 1;
    
    for (let i = 1; i < length; i++) {
        // If the current position is beyond the edge of the current jump, make another jump.
        // Here edge is the value in the array e.g. the further edge of the jump
        // e.g. you've updated i enough to get to this jump
        if (i > edge) { 
            edge = maxPosition;
            jumps++;
        }
        
        maxPosition = Math.max(maxPosition, i + nums[i]); // Update the max position.
    }
    
    return jumps;
};