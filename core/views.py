import io
import uuid
import time
import requests
import zipfile
from concurrent.futures import ThreadPoolExecutor
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ProcessImagesView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        urls = request.POST.get('image_urls', '')
        if not urls:
            return HttpResponse("No image URLs provided.", status=400)
        
        url_list = [u.strip() for u in urls.split(',') if u.strip()]
        zip_bytes = self.process_download(url_list)

        response = HttpResponse(zip_bytes.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename=downloaded_images_{int(time.time())}.zip'
        return response


    def process_download(self, url_list):
        zip_buffer = io.BytesIO()

        def fetch_and_add(url):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                filename = f"{uuid.uuid4()}.jpg"
                with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED) as zip_file:
                    zip_file.writestr(filename, response.content)
            except Exception as e:
                print(f"Failed to download {url}: {e}")

        with ThreadPoolExecutor(max_workers=min(10, len(url_list))) as executor:
            executor.map(fetch_and_add, url_list)

        zip_buffer.seek(0)
        return zip_buffer
