from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/',views.UserSignup,name='signup'),
    path('log_in/',views.UserLogin,name='login'),
    path('log_out_confirm/',views.ConfirmLogout,name='logoutconfirm'),
    path('log_out_/',views.UserLogout,name='logout'),
]
