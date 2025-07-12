import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Quantum Function Triggered.')
    name = req.params.get('name')
    return func.HttpResponse(f"Hello, {name or 'Quantum World'}!")
