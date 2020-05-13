from django.urls import path
from .views import ReviewList, CreateReviewFBV, CreateReviewCBV, CreateReviewGBV

app_name = 'reviews' #with include

urlpatterns = [
    path('', ReviewList.as_view(), name='review-list'),
    path('create-review-fbv/', CreateReviewFBV, name='create-review-fbv'),
    path('create-review-cbv/', CreateReviewCBV.as_view(), name='create-review-cbv'),
    path('create-review-gbv/', CreateReviewGBV.as_view(), name='create-review-gbv'),


]
