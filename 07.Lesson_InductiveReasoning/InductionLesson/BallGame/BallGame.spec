
methods {
	ballAt() returns uint256 envfree
}

rule neverPlayer4(method f) {
	env e;
	uint256 ballBefore = ballAt();
	require ballBefore != 3 && ballBefore != 4;
	f(e);
	uint256 ballAfter = ballAt();
	assert ballAfter != 4;
}

invariant neverReachPlayer4() 
	ballAt() != 4 