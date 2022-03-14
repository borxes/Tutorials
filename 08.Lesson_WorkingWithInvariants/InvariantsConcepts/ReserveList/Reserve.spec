// Try to prove the following list of properties:

//  Both lists are correlated - If we use the id of a token in reserves to retrieve a token in underlyingList, we get the same toke.
//  There should not be a token saved at an index greater or equal to reserve counter.
//  Id of assets is injective (i.e. different tokens should have distinct ids).
//  Independency of tokens in list - removing one token from the list doesn't affect other tokens.
//  Each non-view function changes reservesCount by 1.

//  If you're able to think of additional interesting properties implement them as well.

methods {

    getTokenAtIndex(uint256) returns (address) envfree

    // Gets the ID saved in reserved mapping according to input token id
    getIdOfToken(address)  returns (uint256) envfree

    // Gets the count of underlying assets in the list
    getReserveCount() returns (uint256) envfree

    // Adds a reserve to the list and updates its details
    addReserve(address, address, address, uint256) 

    // Removes a specified reserve from the list.
    removeReserve(address)
}

invariant listsAreCorrelated(address token)
    getIdOfToken(token) != 0 && getTokenAtIndex(getIdOfToken(token)) == token

invariant tokenIndex_LE_count(address token)
    getReserveCount() > 0 && getIdOfToken(token) < getReserveCount()

invariant injectiveIdOfAssets(address tokenA, address tokenB)
    (tokenA != tokenB && !(getIdOfToken(tokenA) == 0 && getIdOfToken(tokenB) == 0)) => getIdOfToken(tokenA) != getIdOfToken(tokenB)

