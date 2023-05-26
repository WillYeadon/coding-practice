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

function helper(node, values) {
    if (node === null) {
        return values;
    }
    if (node.val !== undefined) {
        values.push(node.val);
    }

    if (node.left) { helper(node.left, values); }
    if (node.right) { helper(node.right, values); }

    return values;   
}

var preorderTraversal = function(root) {   
    let values = [];
    if (root === null) {
        return values;
    }

    return helper(root, values);
};