import logging

import azure.functions as func


def main(req: func.HttpRequest, inputBlob: func.InputStream) -> func.InputStream:

    logging.info('Python HTTP trigger function processed a request.')

    return inputBlob
