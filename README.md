# gnucash-nordea
This is a simple CLI tool that parses exported CSV files from Nordea Bank into a CSV format that is easy for GNUCash to digest.

It removes some fields that are of no use and splits up the deposits and withdrawals into two separate fields. In the original file withdrawals are prefixed with '-' before the amount, while deposits are free from any prefix.
