"""
        
        Label and description customizations.


        Monkey-patch Archetypes widget base class to have a hook to ask for custom labels.
"""

from utilities import getResearcherSettings

def getCustomizedAttribute(instance, fieldName, type):
    """
    Look up database stored widget customization from the site-wide researcher content type settings.
    
    @param instance: Content item
    
    @parma fieldName: Field name as it is in AT schema
    
    @param type: One of "label", "description", "visible"
    
    Visible is boolean, others are strings.
    """
    settings = getResearcherSettings(instance)    
    customization = settings.getFieldCustomization(fieldName, type)
    return customization    

# it's a class with no capital letter!
from Products.Archetypes.Widget import TypesWidget

TypesWidget._old_Label = TypesWidget.Label
TypesWidget._old_Description = TypesWidget.Description

def getFieldName(context, widget):
    """
    Helper method to look field name for the widget from a conten item.
    
    The widget lacks reference to field so we need to look this information from the instance itself.
    """

    # Cache the field name on widget instance
    name = getattr(widget, "_field_name", None)
    if name:
        return name
    
    for field in context.Schema().values():
        if field.widget == widget:
            name = field.getName()
            widget._field_name = name
            return name
        
        
    return None
    

def Label(self, instance, **kwargs):
    """
    
    self is like <Products.Archetypes.Widget.LinesWidget object at 0x1072941d0>
    """
    name = getFieldName(instance, self)
 
    custom = getCustomizedAttribute(instance, name, "label")
    if custom is not None:
        return custom
    
    # Default action
    return self._old_Label(instance, **kwargs)
             
TypesWidget.Label =  Label


def Description(self, instance, **kwargs):
    """
    
    self is like <Products.Archetypes.Widget.LinesWidget object at 0x1072941d0>
    """
    name = getFieldName(instance, self)
 
    custom = getCustomizedAttribute(instance, name, "description")
    if custom is not None:
        return custom
    
    # Default action
    return self._old_Description(instance, **kwargs)
             
TypesWidget.Description =  Description




        
        