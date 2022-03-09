methods {
		getCurrentManager(uint256 fundId) returns (address) envfree
		getPendingManager(uint256 fundId) returns (address) envfree
		isActiveManager(address a) returns (bool) envfree
}



rule uniqueManager(uint256 fundId1, uint256 fundId2, method f) {
	require fundId1 != fundId2;
	require getCurrentManager(fundId1) != 0 && isActiveManager(getCurrentManager(fundId1));
	require getCurrentManager(fundId2) != 0 && isActiveManager(getCurrentManager(fundId2));

	// this condition is too strict. funds could be created with the same manager (bug1) and this 
	// precondition doesn't catch the bug (under-approximation)
	// require getCurrentManager(fundId1) != getCurrentManager(fundId2);
				
	env e;


	// if we don't use this, then the following error happens:
	// another fund management is claimed, where pending was manager of fund 1.
	// so that manager of fund1 becomes inactive and assert fails.
	if (f.selector == claimManagement(uint256).selector)
	{
		uint256 id;
		require id == fundId1 || id == fundId2;
		claimManagement(e, id);  
	}
	else {
		calldataarg args;
		f(e,args);
	}

	assert getCurrentManager(fundId1) != getCurrentManager(fundId2), "managers not different";
	assert getCurrentManager(fundId1) != 0 && isActiveManager(getCurrentManager(fundId1)), "manager of fund1 is not active";
	assert getCurrentManager(fundId2) != 0 && isActiveManager(getCurrentManager(fundId2)), "manager of fund2 is not active";
}



		
	
