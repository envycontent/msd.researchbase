from zope.component.hooks import getSite

from Products.CMFCore.utils import getToolByName 

def construct_without_permission_check(folder, type_name, id, *args, **kwargs):
    """ Construct a new content item bypassing creation and content add permissios checks.


    @param folder: Folderish content item where to place the new content item

    @param type_name: Content type id in portal_types

    @param id: Traversing id for the new content

    @param args: Optional arguments for the construction (will be passed to the creation method if the type has one)

    @param kwargs: Optional arguments for the construction (will be passed to the creation method if the type has one)

    @return: Reference to newly created content item
    """

    portal_types = getToolByName(folder, "portal_types")

    # Get this content type definition from content types registry
    type_info = portal_types.getTypeInfo(type_name)

    # _constructInstance takes optional *args, **kw parameters too
    new_content_item = type_info._constructInstance(folder, id)
    
    new_content_item.unmarkCreationFlag()

    # Return reference to justly created content
    return new_content_item


def getResearcherSettings(context, request=None):
    """
    
    @param context: Any content item
    
    @param request: HTTP request object, for cache hinting
    
    @return the site researcher settingss object.
    """
    
    if request:
        settings = getattr(request, "_v_research_setting", None)
        return settings
    
    # just removing this print as its annoying me (AB)
    # print "Get settings"
    # XXX: Does not work for some reason in all cases - parent object is missing
    try:
        root = context.portal_url.getPortalObject()
    except AttributeError, a:
        # We need to handle both special cases because of AT internal maddress
        root = getSite()

    if not "researcher-settings" in root:
        # Automatically create settings on the first access
        construct_without_permission_check(root, "ResearcherSettings", "researcher-settings")
    
    settings = root["researcher-settings"]
    
    if request:
        request._v_research_settings = settings
    
    return settings

    
