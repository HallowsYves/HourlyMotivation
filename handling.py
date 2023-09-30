from logging import Logger
class QuoteAlreadyInDatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
        return f"{self.message}"
    
    def __str__(self):
        Logger.info("Quote already in database")
        return{self.message}
