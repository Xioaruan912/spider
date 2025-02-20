from loguru import  logger
def open_file():
    file_path = "url.txt"
    with open(file_path,'r') as file:
        file_content = file.read()
        logger.info(file_content)