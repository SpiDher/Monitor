import logging
from datetime import datetime
from django.http import JsonResponse

# Configure logging
logger = logging.getLogger(__name__)
handler = logging.FileHandler('request_logs.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Keep request count
request_count = 0

def log_request(request):
    global request_count
    request_count += 1
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the information
    logger.info(f"Request #{request_count} at {current_time}")

    return JsonResponse({
        'message': 'Request logged successfully.',
        'request_count': request_count,
        'time_logged': current_time,
    })