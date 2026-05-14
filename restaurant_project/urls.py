from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>АИС Общепит</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
            h1 { font-size: 48px; }
            .container { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; display: inline-block; }
            .status { color: #4CAF50; font-weight: bold; }
            a { color: white; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>АИС Общепит</h1>
            <p>Система автоматизации для ресторана</p>
            <p class="status">Сервер работает успешно</p>
            <p>База данных подключена</p>
            <hr>
            <p>Доступные API:</p>
            <ul style="text-align: left;">
                <li>GET /api/dishes</li>
                <li>GET /api/tables</li>
                <li>GET /api/categories</li>
                <li>GET /api/orders/active</li>
                <li>POST /api/orders</li>
                <li>PUT /api/orders/&lt;id&gt;/status</li>
                <li>GET /admin</li>
            </ul>
        </div>
    </body>
    </html>
    """)

# Временные заглушки для API
def api_dishes(request):
    return JsonResponse({"success": True, "data": [{"id": 1, "name": "Цезарь", "price": 450}]})

def api_tables(request):
    return JsonResponse({"success": True, "data": [{"id": 1, "number": 1, "seats": 4, "is_free": True}]})

def api_categories(request):
    return JsonResponse({"success": True, "data": [{"id": 1, "name": "Салаты"}]})

def api_active_orders(request):
    return JsonResponse({"success": True, "data": []})

@csrf_exempt
def api_create_order(request):
    return JsonResponse({"success": True, "order_id": 1, "total": 0})

@csrf_exempt
def api_update_order_status(request, order_id):
    return JsonResponse({"success": True})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/dishes', api_dishes),
    path('api/tables', api_tables),
    path('api/categories', api_categories),
    path('api/orders/active', api_active_orders),
    path('api/orders', api_create_order),
    path('api/orders/<int:order_id>/status', api_update_order_status),
]
