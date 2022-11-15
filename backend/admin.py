from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from home.models import Application, Document



class ApplicationModel(ModelAdmin):
    model = Application
    menu_label = "Application"
    menu_icon = "tasks"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("userId", "companyName", "position", "deadline")
    empty_value_display = 'N/A'
    search_fields = ("companyName",)


modeladmin_register(ApplicationModel)
