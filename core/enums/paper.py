from enum import Enum

class OpenAccessStatus(str, Enum):
    GOLD = "gold"
    GREEN = "green"
    HYBRID = "hybrid"
    BRONZE = "bronze"
    CLOSED = "closed"

class JournalTier(str, Enum):
    Q1 = "q1"
    Q2 = "q2"
    Q3 = "q3"
    Q4 = "q4"
    UNRANKED = "unranked"
