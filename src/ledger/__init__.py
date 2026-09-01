"""Ledger: the event-sourced double-entry core. The source of truth the other contexts consume. JournalEntry guards debit-equals-credit; each LedgerAccount keeps its own event stream."""
