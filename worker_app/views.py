from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import os
from mimetypes import guess_type
from PIL import Image
from django.views.decorators.clickjacking import xframe_options_exempt

DRAWINGS_DIR = os.path.join(settings.BASE_DIR, 'drawings')

@xframe_options_exempt
def index(request):
    return render(request, 'worker_app/index.html')

def list_files(request):
    files = os.listdir(DRAWINGS_DIR)
    files = [f for f in files if f.endswith(('.pdf', '.jpeg', '.jpg', '.png', '.tiff', '.tif'))]
    return JsonResponse(files, safe=False)


def get_file(request, filename):
    file_path = os.path.join(DRAWINGS_DIR, filename)
    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)

    if filename.lower().endswith(('.tif', '.tiff')):
        with Image.open(file_path) as img:
            img = img.convert("RGB")
            response = HttpResponse(content_type="image/jpeg")
            img.save(response, "JPEG")
            response['Content-Disposition'] = f'inline; filename="{filename}.jpg"'
            return response
    else:
        with open(file_path, 'rb') as file:
            file_type, _ = guess_type(file_path)
            response = HttpResponse(file.read(), content_type=file_type)
            response['Content-Disposition'] = f'inline; filename="{filename}"'
            return response

