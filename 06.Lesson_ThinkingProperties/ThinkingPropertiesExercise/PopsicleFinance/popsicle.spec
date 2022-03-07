methods {
    balanceOf(address account) envfree
    deposit()
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