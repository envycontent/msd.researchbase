"""


"""

from Products.CMFCore.interfaces import ISiteRoot

from five import grok

class ResearcherSettings(grok.CodeView):
    """ 
    Access researcher setting through Plone Control Panel.
    
    Simply create settings objects (if not exist) and redirect to it.
    """
    grok.context(ISiteRoot)
    
    def render(self):
        from msd.researchbase.utilities import getResearcherSettings
        obj = getResearcherSettings(self.context)
        
        # Redirect to AT edit view
        self.request.response.redirect(obj.absolute_url() + "/edit")
        
        return ""
        
    