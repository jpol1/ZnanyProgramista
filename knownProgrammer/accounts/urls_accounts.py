from django.urls import path

from accounts.views import (
    programmer_detail,
    programmers_list,
    programmer_create_form,
    programmer_update_model_form,
    programmer_delete_confirm,
)

urlpatterns = [
    path('list', programmers_list, name="programmers_list"),
    path('detail/<int:id>', programmer_detail, name="programmer_detail"),
    path('create', programmer_create_form, name="programmer_create_form"),
    path('update/<int:id>', programmer_update_model_form, name="programmer_update_model_form"),
    path('delete/<int:id>', programmer_delete_confirm, name="programmer_delete_confirm"),
]