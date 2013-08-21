from modeltranslation.translator import translator, TranslationOptions
from base_page.models import OrganizationSetting

#base_page
class OrganizationSettingTranslationOptions(TranslationOptions):
    fields = ('organization_name',
              'title',
              'blurb',
              'provider',
              )

translator.register(OrganizationSetting, OrganizationSettingTranslationOptions)

