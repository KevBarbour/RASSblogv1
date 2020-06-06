from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),

    path('About/', views.AboutPageView.as_view(), name='about'),
    path('Projects/', views.ProjectsPageView.as_view(), name='projects'),
    path('Contact/', views.ContactPageView.as_view(), name='contact'),
    path('Terms/', views.TermsPageView.as_view(), name='terms'),
    path('Privacy/', views.PrivacyPageView.as_view(), name='privacy'),
    path('Disclaimer/', views.DisclaimerPageView.as_view(), name='disclaimer'),

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
