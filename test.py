'''
## FLOW ##
    <Before Runtime>
    Read CFG -> Test Ambiguity -> Create NFA -> Convert to DFA -> Create parsing table

    <During Runtime>
    Receive input string -> Parse input string -> Apply parsing table -> Accept or Reject

## Additional Requirements ##
    - Print parse tree for accepted strings
    - Print error report(ex. error location) for rejected strings
'''

import pandas as pd

action_df = pd.read_csv("./action.csv")
# goto_df = pd.read_csv("./goto.csv")

print(action_df.head())
print(action_df.iloc[4, 2])