### Valid States

- Max end_time is 1 day from now
- auction expiry <= end_time (?)

### State Transitions

- If price decreased, it was the result of bid()

- If auction is closed, its expiry or end_time have passed

### Variable Transitions

- Prize is only decreasing for each bid

- For each auction, payment doesn't change

### High Level Properties

No two different auctions with same id? hmm

### Unit Tests

- bid() reduced the prize