methods {
    deposit()
    withdraw(uint)
    collectFees()
    OwnerDoItsJobAndEarnsFeesToItsClients()
    transfer(address, uint256) returns (bool)
    assetsOf(address) returns (uint) envfree
}

// sanity
// rule sanity(method f){
//     env e;
//     calldataarg args;

//     f(e, args);
//     assert false;
// }


rule assetsOfIntegrity(address recipient, uint amount) {
    env e;

    uint256 assetsBeforeA = assetsOf(e.msg.sender);
    uint256 assetsBeforeB = assetsOf(recipient);

    transfer(e, recipient, amount);

    uint256 assetsAfterA = assetsOf(e.msg.sender);
    uint256 assetsAfterB = assetsOf(recipient);

    assert assetsBeforeA + assetsBeforeB == assetsAfterA + assetsAfterB;
}

ghost sum_of_all_assets() returns uint256{
    // for the constructor - assuming that on the constructor the value of the ghost is 0
    init_state axiom sum_of_all_assets() == 0;
}

hook Sstore assets[KEY address user] uint256 new_balance
    // the old value ↓ already there
    (uint256 old_balance) STORAGE {
    /* havoc is a reserved keyword that basically changes the state of the ghost (sumAllFunds) to any state.
     * the assuming command the havoc to take into consideration the following clause.
     * the @new and @old additions to the ghost are incarnations of the ghost
     * we basically say here create new incarnation (@new) that is equal to the old incarnation (@old)
     * plus the difference between the new value stored and the old value stored.
     * remember that the new value is the sum of the old + the an addition, so adding @old to the new will be a wrong count
     */
  havoc sum_of_all_assets assuming sum_of_all_assets@new() == sum_of_all_funds@old() + new_balance - old_balance;
}
