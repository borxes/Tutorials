methods {
    balanceOf(address account) envfree
    assetsOf(address account) envfree
    deposit()
    collectFees()
}

// make sure balance of user increases after deposit
rule balanceIncreaseAfterDeposit(uint amount){
    env e;
    uint balanceBefore = balanceOf(e.msg.sender);
    require e.msg.value > 0;
    deposit(e);
    uint balanceAfter = balanceOf(e.msg.sender);
    assert (balanceAfter >= balanceBefore, "Balance cannot decrease after deposit");
}

// after collectFees, user has 0 fees to collect
rule zeroFeesAfterCollect() {
    env e;
    uint assetsBefore = assetsOf(e.msg.sender);
    collectFees(e);
    uint assetsAfter = assetsOf(e.msg.sender);
    assert (assetsAfter <= assetsBefore && assetsAfter == 0);
}

// user assets decreased only after withdraw or collect
// this failed on transfer and transferFrom erc20 methods
rule assetsDecreased(method f) {
    env e;
    uint assetsBefore = assetsOf(e.msg.sender);
    f(e);
    uint assetsAfter = assetsOf(e.msg.sender);
    assert (assetsAfter < assetsBefore => f.selector == deposit().selector || f.selector == collectFees().selector);
}

