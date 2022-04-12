# gnucash-nordea
This is a simple CLI tool that parses exported CSV files from Nordea Bank into a CSV format that is easy for GNUCash to digest.

There are two main problems with the Nordea CSV file.
1. Reversed transaction order
Transactions are ascending from new to old, when they should instead be descending from old to new.

2. Deposits and withdrawals are in the same column.
In the original file a withdrawal is prefixed with a '-' before the amount. While a deposit is not prefixed with a char.
