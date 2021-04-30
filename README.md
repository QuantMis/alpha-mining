# FOR LOOP TESTING

- declare trading variable
  - start capital
  - usdt spent per trade (100%) for 1:1 leverage
  - update capital 

- compute indicator (moving)

- loop through all the data

# alpha 1.0.0

BULLISH INDICATOR
- closing higher 3 candle before (exclude current bar)


EXIT LOGIC
SL(pnl) -> 5% capital  
TP(pnl) -> 10% capital

CONTINGENCY 
- None 

# code structure
  main method (queue)
  entry method (to check entry logic)
  exit method (to check exit logic)
  calculate pnl (to compute at every bar)
  update equity method (to update after exited)
  
