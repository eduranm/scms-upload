from django.http import HttpResponseRedirect
from django.urls import include, path
from django.utils.translation import gettext as _

from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from wagtail.contrib.modeladmin.views import CreateView

from .button_helper import UploadButtonHelper
from .permission_helper import UploadPermissionHelper
from .groups import QUALITY_ANALYST
from .models import Package


class UploadPackageCreateView(CreateView):
    def form_valid(self, form):
        self.object = form.save_all(self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class PackageAdmin(ModelAdmin):
    model = Package
    button_helper_class = UploadButtonHelper
    permission_helper_class = UploadPermissionHelper
    create_view_class = UploadPackageCreateView
    inspect_view_enabled=True
    inspect_template_name='/app/upload/templates/modeladmin/upload/package/detail.html'
    menu_label = _('Package')
    menu_icon = 'folder'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'file',
        'current_status',
        'creator',
        'created',
        'updated',
        'updated_by',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'file',
        'creator',
        'updated_by',
    )
    inspect_view_fields = (
        'file', 
        'created', 
        'updated',
        'files_list',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        user_groups = [g.name for g in request.user.groups.all()]

        if request.user.is_superuser or request.user.is_staff or QUALITY_ANALYST in user_groups:
            return qs

        return qs.filter(creator=request.user)


modeladmin_register(PackageAdmin)


@hooks.register('register_admin_urls')
def register_disclosure_url():
    return [
        path('upload/package/',
        include('upload.urls', namespace='upload')),
    ]
