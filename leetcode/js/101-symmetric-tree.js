function mirror(left, right) {  
    if ((left === null) && (right === null)) {
        return true;
    }
    if ((left === null) || (right === null)) {
        return false;
    }

    return ((left.val === right.val) && 
            mirror(left.left, right.right) &&
            mirror(left.right, right.left));
};

var isSymmetric = function(root) {
    return mirror(root.left, root.right);
}