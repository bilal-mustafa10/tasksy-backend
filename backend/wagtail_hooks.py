from wagtail import hooks


@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels[:] = [item for item in panels if item.name != 'site_summary']


@hooks.register('construct_main_menu')
def hide_explorer_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'explorer']
    menu_items[:] = [item for item in menu_items if item.name != 'images']
    menu_items[:] = [item for item in menu_items if item.name != 'videos']
    menu_items[:] = [item for item in menu_items if item.name != 'reports']
    menu_items[:] = [item for item in menu_items if item.name != 'help']