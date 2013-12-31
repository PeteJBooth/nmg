from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class PortfolioApphook(CMSApp):
    name = "Portfolio Application"
    urls = ["casestudy.urls"]

apphook_pool.register(PortfolioApphook)
