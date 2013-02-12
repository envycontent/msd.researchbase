"""


"""

from Products.Five import BrowserView

from msd.researchbase.utilities import getResearcherSettings

def convertCheckboxValue(value):
    """ DataGridField value converter for CheckboxColumn """
    if value is None:
        return None

    if value == '':
        return False
    
    if value == '1':
        return True
    
    # XXX: Not sure if happens
    if value == '0':
        return False

    raise RuntimeError("Bad checkbox value:" + value)

class WidgetCondition(BrowserView):
    """ 
    This is referred in msd.researcher schema conditions field.
    """
    
                  
    def __call__(self, schemataName, fieldName):
        """
        
        """
        settings = getResearcherSettings(self.context)    
        
        # Schemata customizations allows us to drop schematas if set to false
        customization = convertCheckboxValue(settings.getSchemataVisibility(schemataName))
        if customization is not None:
            if customization == False:
                return False
                
        # Then check field level customization
        customization = convertCheckboxValue(settings.getFieldCustomization(fieldName, "visible"))
        if customization is not None:
            return customization
        
        # Default is visible
        return True