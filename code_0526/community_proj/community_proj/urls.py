from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from community_app.views import *
# 전체를 가져오면(*), new와 같이 이름만 써도 된다. view를 쓸 필요 없다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', new, name="new"),
    path('detail/<int:community_id>/', detail, name="detail"),
    path('', index, name="index"),
    path('comment/<int:community_id>/', comment, name="comment"),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler404 = 'community_app.views.page_not_found'