var inorderTraversal = function(root) {
    let ans = [];
    // Want to pass in ans
    traverse(root, ans);
    return ans;
};

// Function hoisted here so defined after declared
function traverse(node, ans) {
    if (node != null) {
        traverse(node.left, ans);
        ans.push(node.val);
        traverse(node.right, ans);
    }
}