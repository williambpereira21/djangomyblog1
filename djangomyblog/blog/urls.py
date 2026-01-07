from django.urls import include, path
from .views import about, delete_post, edit_post, home, new_post, post_detail, signup, profile

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),  # <- aqui está a correção
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('new/', new_post, name='new_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),
    path('edit/<int:id>/', edit_post, name='edit_post'),
]
