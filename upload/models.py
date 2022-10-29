from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtailautocomplete.edit_handlers import AutocompletePanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from article.models import Article
from core.models import CommonControlField
from issue.models import Issue

from . import choices
from .forms import UploadPackageForm
from .permission_helper import ACCESS_ALL_PACKAGES, ASSIGN_PACKAGE, ANALYSE_VALIDATION_ERROR_RESOLUTION, FINISH_DEPOSIT, SEND_VALIDATION_ERROR_RESOLUTION
from .utils import file_utils


User = get_user_model()


class Package(CommonControlField):
    file = models.FileField(_('Package File'), null=False, blank=False)
    signature = models.CharField(_('Signature'), max_length=32, null=True, blank=True)
    category = models.CharField(_('Category'), max_length=32, choices=choices.PACKAGE_CATEGORY, null=False, blank=False)
    status = models.CharField(_('Status'), max_length=32, choices=choices.PACKAGE_STATUS, default=choices.PS_ENQUEUED_FOR_VALIDATION)
    article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.SET_NULL)
    issue = models.ForeignKey(Issue, blank=True, null=True, on_delete=models.SET_NULL)
    assignee = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    stat_disagree_n = models.IntegerField(_('Disagree (n)'), null=True, blank=True)
    stat_disagree_p = models.FloatField(_('Disagree (%)'), null=True, blank=True)
    stat_incapable_to_fix_n = models.IntegerField(_('Incapable to fix (n)'), null=True, blank=True)
    stat_incapable_to_fix_p = models.FloatField(_('Incapable fo fix (%)'), null=True, blank=True)

    panels = [
        FieldPanel('file'),
        FieldPanel('category'),
        AutocompletePanel('article'),
        AutocompletePanel('issue'),
    ]

    def __str__(self):
        return self.file.name

    def files_list(self):
        files = {'files': []}

        try:
            files.update({'files': file_utils.get_file_list_from_zip(self.file.path)})
        except file_utils.BadPackageFileError:
            # É preciso capturar esta exceção para garantir que aqueles que 
            #  usam files_list obtenham, na pior das hipóteses, um dicionário do tipo {'files': []}.
            # Isto pode ocorrer quando o zip for inválido, por exemplo.
            ...

        return files

    base_form_class = UploadPackageForm

    class Meta:
        permissions = (
            (FINISH_DEPOSIT, _("Can finish deposit")),
            (ACCESS_ALL_PACKAGES, _("Can access all packages from all users")),
            (ASSIGN_PACKAGE, _("Can assign package")),
        )


class QAPackage(Package):
    class Meta:
        proxy = True


class ValidationResult(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(_('Error category'), max_length=64, choices=choices.VALIDATION_ERROR_CATEGORY, null=False, blank=False)
    data = models.JSONField(_('Error data'), default=dict, null=True, blank=True)
    message = models.CharField(_('Error message'), max_length=512, null=True, blank=True)
    status = models.CharField(_('Status'), max_length=16, choices=choices.VALIDATION_STATUS, null=True, blank=True)

    package = models.ForeignKey('Package', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return '-'.join([
            str(self.id),
            self.package.file.name,
            self.category,
            self.status,
        ])

    def report_name(self):
        return choices.VALIDATION_DICT_ERROR_CATEGORY_TO_REPORT[self.category]
    
    panels = [
        MultiFieldPanel(
            [
                FieldPanel('package'),
                FieldPanel('category'),
            ],
            heading=_('Identification'),
            classname='collapsible'
        ),
        MultiFieldPanel(
            [
                FieldPanel('data'),
            ],
            heading=_('Content'),
            classname='collapsible'
        )
    ]

    class Meta:
        permissions = (
            (SEND_VALIDATION_ERROR_RESOLUTION, _("Can send error resolution")),
            (ANALYSE_VALIDATION_ERROR_RESOLUTION, _("Can analyse error resolution")),
        )


class ErrorResolution(CommonControlField):
    validation_result = models.OneToOneField('ValidationResult', to_field='id', primary_key=True, related_name='resolution', on_delete=models.CASCADE)
    action = models.CharField(_('Action'), max_length=32, choices=choices.ERROR_RESOLUTION_ACTION, null=True, blank=True)
    comment = models.TextField(_('Comment'), max_length=512, null=True, blank=True)
    
    panels = [
        FieldPanel('action'),
        FieldPanel('comment'),
    ]


class ErrorResolutionOpinion(CommonControlField):
    validation_result = models.OneToOneField('ValidationResult', to_field='id', primary_key=True, related_name='analysis', on_delete=models.CASCADE)
    opinion = models.CharField(_('Opinion'), max_length=32, choices=choices.ERROR_RESOLUTION_OPINION, null=True, blank=True)
    comment = models.TextField(_('Comment'), max_length=512, null=True, blank=True)

    panels = [
        FieldPanel('opinion'),
        FieldPanel('comment'),
    ]
