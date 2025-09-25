## Company Details
[Carelon](https://www.carelon.com)

## Required Experience
- System Design & Architect
- Debugging Tools and Techniques
- Python Programming
    - Multithreading
    - Multiprocessing
    - Asyncio/wait
    - GIL
    - Memory Management in Python (Garbage collection and reference counting)
- Caching (LRU Caching)
- Database
- Cloud

## Interiview Question

You are the engineer responsible for a production claims-processing pipeline that ingests ~2 million claims per day. As volume grows, the primary database table is becoming a performance bottleneck. Business rules require:
The main (hot) table must contain only the most recent 7 days of claims for fast lookups.
Claims older than 7 days must be retained in a different store (archive) due to a retention policy.
Backups are critical — you must guarantee no data loss while moving data from the main table to the archive.
The system must continue to support reads for analytics and occasional restores from archived data.
Design an approach to meet these requirements. Explain your high-level design, how you would implement it (including concrete operations you would run in PostgreSQL), how you ensure zero/near-zero data loss during archival, and what monitoring/automation you would add.

## Contact details
- HR (KBheemana.Gowd@carelon.com)