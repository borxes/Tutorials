certoraRun ERC20Bug1.sol:ERC20 --verify ERC20:Sanity.spec \
--solc solc8.0 \
--staging \
--optimistic_loop \
--msg "$1"