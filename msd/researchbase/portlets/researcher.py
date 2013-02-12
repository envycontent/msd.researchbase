from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from zope.formlib import form
from zope.interface import implements, Interface
from zope import schema

from Acquisition import aq_inner, aq_parent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets.portlets import base

from msd.researchbase import researchbaseMessageFactory as _
from msd.researchbase.interfaces import IResearcher
from msd.researchtheme.interfaces import IResearchTheme

class IResearcherPortlet(IPortletDataProvider):
    """A portlet which can render information related to the researcher
    """
    bottom_url = schema.TextLine(
        title=_(u'Bottom link URL'),
        description=_(u'Enter URL address for bottom link of the portlet.'),
        required=False
    )

class Assignment(base.Assignment):
    implements(IResearcherPortlet)

    bottom_url = ''

    def __init__(self, bottom_url=''):
        self.bottom_url = bottom_url

    @property
    def title(self):
        return _(u'Researcher info')

class Renderer(base.Renderer):

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)
    
    @memoize
    def _data(self):
        result = {}
        context = aq_inner(self.context)
        if IResearcher.providedBy(context):
            categories = {}
            for prog in context.getBackReferences(relationship='researchers_in_programme'):
                cat_obj = prog.aq_parent
                category_id = cat_obj.getId()
                category = categories.get(category_id, {})
                prog_info = dict(
                    title = prog.title,
                    description = prog.description,
                    url = prog.absolute_url()
                    )

                if not category:
                    category['title'] = cat_obj.title
                    category['description'] = cat_obj.description
                    category['url'] = cat_obj.absolute_url()
                    category['programmes'] = [prog_info]
                else:
                    category['programmes'].append(prog_info)

                categories[category_id] = category
            if categories:
                result['programmes'] = categories

            areas = []
            included_areas = []
            for area in context.getBackReferences(relationship='researchers_in_theme'):
                parent = aq_parent(area)
                if IResearchTheme.providedBy(parent):
                    area = parent
                area_uid = area.UID()
                if area_uid not in included_areas:    
                    areas.append(dict(
                        title = area.title,
                        description = area.description,
                        url = area.absolute_url()
                    ))
                    included_areas.append(area_uid)
            if areas:
                result['areas'] = areas
        return result

    @property
    def available(self):
        return self._data()

    @property
    def programmes(self):
        return self._data().get('programmes')

    @property
    def  areas(self):
        return self._data().get('areas')

    @property
    def bottom_url(self):
        return self.data.bottom_url

    render = ViewPageTemplateFile('researcher.pt')

class AddForm(base.AddForm):
    form_fields = form.Fields(IResearcherPortlet)
    label = _(u"Add Supervisor Portlet")
    description = _(u"This portlet lists additional information related to a Supervisor.")

    def create(self, data):
        return Assignment(bottom_url=data.get('bottom_url', ''))


class EditForm(base.EditForm):
    form_fields = form.Fields(IResearcherPortlet)
    label = _(u"Edit Supervisor Portlet")
    description = _(u"This portlet lists additional information related to a Supervisor.")
