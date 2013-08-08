"""


"""

from Products.Five import BrowserView


class ResearcherSettings(BrowserView):
    """ 
    Access researcher setting through Plone Control Panel.
    
    Simply create settings objects (if not exist) and redirect to it.
    """
    
    def render(self):
        from msd.researchbase.utilities import getResearcherSettings
        obj = getResearcherSettings(self.context)
        
        # Redirect to AT edit view
        self.request.response.redirect(obj.absolute_url() + "/edit")
        
        return ""
        
    def __call__(self):
        self.render() 
        
        
    