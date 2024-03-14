from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool

from cms.utils.urlutils import admin_reverse

class MyappTopBar(CMSToolbar):

    def populate(self):
        menu= self.toolbar.get_or_create_menu(
            'myapp_cms_integration-app',  # a unique key for this menu
            'myapp',                        # the text that should appear in the menu
            )

        # menu.add_sideframe_item(
        #     name='myapp list',                              # name of the new menu item
        #     url=admin_reverse('en/contact'),    # the URL it should open with
        # )


# register the toolbar
toolbar_pool.register(MyappTopBar)