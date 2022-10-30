from src.infrastructure.logger import Logger

logger = Logger(__name__)

if __name__ == "__main__":
    logger.log("Log message")
    logger.warn("Warning message without long message")
    logger.warn("Warning title", "Warning message without long message")
    logger.error("Error message without operation")
    logger.error("Error message with operation", operation="main")
