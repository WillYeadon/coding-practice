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
 * @return {number}
 */

function dfs(node, current) { 
    if (!node) { return current;}
    let left = current;
    let right = current;

    if (node.left) {
        left = dfs(node.left, current + 1);
    }
    if (node.right) {
        right = dfs(node.right, current + 1);
    }
    
    if (left > right) {
        return left;
    }
    else {
        return right;
    }
}

var maxDepth = function(root) {
    if (!root) {return 0;}      
    return dfs(root, 1);
};