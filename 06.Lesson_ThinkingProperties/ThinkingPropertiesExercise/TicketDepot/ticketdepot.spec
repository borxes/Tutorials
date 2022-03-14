methods {
    owner() envfree
    getOwnerBalance() returns (uint) envfree
    getEvent(uint16)  returns (address, uint64, uint16)
    createEvent(uint64 , uint16)  returns (uint16)
}

// fails without requiring owner to be different from 0
// new owner in ticket Depot might be 0

rule depotOwnerIsNotZero(method f) {
    env e;
    address ownerBefore = owner();
    require ownerBefore != 0;
    f(e);
    address owner = owner();
    assert owner == 0 => f.selector == ticketDepot(uint64).selector;
}

// each created event has an owner. how to get event?
// this rule doesn't work because certora treats address 0 as normal
rule eachEventHasOwner(uint64 ticketPrice, uint16 ticketsAvailable) {
    env e;
    require e.msg.sender != 0;
    uint16 eventId = createEvent(e, ticketPrice, ticketsAvailable);
    address ownerAfter; uint64 priceAfter; uint16 ticketsAfter;
    ownerAfter, priceAfter, ticketsAfter = getEvent(e, eventId);
    assert ownerAfter != 0;
}


// owner balance only goes up (ignoring external events)
rule ownerBalanceOnlyGoesUp(method f) {
    env e;
    uint balanceBefore = getOwnerBalance();
    calldataarg args;
    f(e, args);
    uint balanceAfter = getOwnerBalance();
    assert balanceAfter >= balanceBefore;
}

rule ticketsRemainingDecreases(method f, uint64 ticketPrice, uint16 ticketsAvailable) {
    env e;
    uint16 eventId = createEvent(e, ticketPrice, ticketsAvailable);
    calldataarg args;
    f(e, args);
    address ownerAfter; uint64 priceAfter; uint16 ticketsAfter;
    ownerAfter, priceAfter, ticketsAfter = getEvent(e, eventId);
    assert ticketsAfter <= ticketsAvailable;
}