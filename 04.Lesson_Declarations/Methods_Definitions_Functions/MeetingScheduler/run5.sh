certoraRun MeetingSchedulerFixed.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--rule checkPendingToCancelledOrStarted \
--method "startMeeting(uint256)" \
--solc solc8.7 \
--msg "short test"