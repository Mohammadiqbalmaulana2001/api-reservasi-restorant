from django.http import JsonResponse

class ServerErrorMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
  
  def __call__(self, request):
    response = self.get_response(request)
    if response.status_code == 500:
      return JsonResponse({
          "success": False,
          "message": "periksa kembali code anda",
          "errors": "Terjadi kesalahan pada server"
      }, status=500)
    return response
    
class NotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
  
    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return JsonResponse({
                    "success": False,
                    "message": "Periksa kembali URL yang Anda gunakan",
                    "errors": "Halaman tidak ditemukan"
                }, status=404)
        return response