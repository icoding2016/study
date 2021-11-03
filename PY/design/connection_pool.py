"""
Design a thread-safe connection pool

ref:
https://leetcode.com/discuss/interview-question/990739/design-connection-pool-multithreaded
https://leetcode.com/discuss/general-discussion/1059859/design-a-thread-safe-connection-pool-ii-java
https://leetcode.com/discuss/general-discussion/1050178/design-a-thread-safe-connection-pool-java


"""

from threading import Semaphore
from typing import Any


# the connector is the object with connect() method

class ConnectionPool(object):
    def __init__(self, connector:Any, max_size:int=0) -> None:
        super().__init__()
        self.max_size = max_size if max_size>0 else 10  # default to 10
        self.pool = {}    # {<conn>:<busy>), }
        self.sem = Semaphore(value=1)
        self.connector = connector

    def getConnection(self) -> Any:
        """Get an available connection from the connection pool.

        Returns:
          The connection or None if no connection is available.
        """
        conn = None
        if self.sem.acquire(blocking=True, timeout=10):
            if self.isEmpty():
                newConn = self.openConnection()
                if newConn:
                    self.pool[newConn] = True
                    conn = newConn
            else:
                c = self.findFreeConnection()
                if c:
                    self.pool[c] = True
                elif not self.isFull():
                    newConn = self.openConnetion()
                    if newConn:
                        self.pool[newConn] = True
                        conn = newConn
            self.sem.release()
        return conn

    def releaseConnection(self, conn) -> None:
        if conn in self.pool:
            if self.sem.acquire(blocking=True):
                self.pool[conn] = False
                self.sem.release()

    def openConnection(self) -> Any:
        if not self.connector:
            return None
        return self.connector.connect()

    def findFreeConnection(self) -> Any:
        for c in self.pool:
            if not self.pool[c]:
                return c
        return None

    def isEmpt(self) -> bool:
        return len(self.pool) == 0
    
    def isFull(self) -> bool:
        return len(self.pool) == self.max_size