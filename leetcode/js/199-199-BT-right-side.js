    /**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    if (root === null) {return [];}

    // Initialize the result list and the queue for BFS.
    const vals = [];
    const queue = [root];

    while (queue.length > 0) {
        // get nodes at current level
        let size = queue.length;

        // run through current level
        for (let i = 0; i < size; i++) {
            let node = queue.shift(); // pop off first node.
            // If you're at the last node of the level then
            // this is the val need for the result
            if (i === size - 1) {
                vals.push(node.val);
            }

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }

    return vals;
};