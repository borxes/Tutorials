certoraRun BankFixed.sol:Bank --verify Bank:invariant.spec \
--rule totalFunds_E_to_sum_of_all_funds \
--solc solc7.6 \
--msg "$1"