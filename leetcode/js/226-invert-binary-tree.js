function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

const node7 = new TreeNode(7);
const node6 = new TreeNode(6);
const node5 = new TreeNode(5);
const node4 = new TreeNode(4);

const node3 = new TreeNode(3, node6, node7);
const node2 = new TreeNode(2, node4, node5);

const root = new TreeNode(1, node2, node3);

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */

var switcharoo = (root) => {
    right = root.right;
    left = root.left;
    root.right = left;
    root.left = right;
    return root
}

var invertTree = function(root) {
    if (root === null) {
        return root
    }

    invertTree(root.left);
    invertTree(root.right);

    return switcharoo(root);
}