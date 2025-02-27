methods {
	getCurrentManager(uint256 fundId) returns (address) envfree
	getPendingManager(uint256 fundId) returns (address) envfree
	isActiveManager(address a) returns (bool) envfree
}



rule uniqueManagerAsRule(uint256 fundId1, uint256 fundId2, method f) {
	// assume different IDs
	require fundId1 != fundId2;

	// assume different managers
	address managerBefore1 = getCurrentManager(fundId1);
	require managerBefore1 != 0;

	address managerBefore2 = getCurrentManager(fundId2);
	require managerBefore2 != 0;


	// rule too strict -> doesn't catch bugs
	// require managerBefore1 != managerBefore2;
	
	// hint: add additional variables just to look at the current state
	
	bool active1 = isActiveManager(getCurrentManager(fundId1));	
	bool active2 = isActiveManager(getCurrentManager(fundId2));

	require active1 && active2;	

	env e;
	calldataarg args;
	f(e,args);

	address managerAfter1 = getCurrentManager(fundId1);
	address managerAfter2 = getCurrentManager(fundId2);
	
	// verify that the managers are still different 
	assert managerAfter1 != managerAfter2, "managers not different";
}


// /* A version of uniqueManagerAsRule as an invariant */
// invariant uniqueManagerAsInvariant(uint256 fundId1, uint256 fundId2)
// 	fundId1 != fundId2 => getCurrentManager(fundId1) != getCurrentManager(fundId2) 
