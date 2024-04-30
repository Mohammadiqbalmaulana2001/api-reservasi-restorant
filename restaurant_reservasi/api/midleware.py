from django.http import JsonResponse

class ServerErrorMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
  
  def __call__(self, request):
    try:
      return self.get_response(request)
    except Exception as e:
      return JsonResponse({
          "success": False,
          "message": "Terjadi kesalahan pada server",
          "errors": str(e)
      }, status=500)
    
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