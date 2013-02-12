from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


from urllib2 import *
import simplejson

class IoxpointsView(Interface):
    """
    oxpoints view interface
    """

    def getColleges():
        """ test method"""
        
    def listColleges():
        """ test method"""


class oxpointsView(BrowserView):
    """
    oxpoints browser view
    """
    implements(IoxpointsView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        
    def getColleges(self):
                
        request_string = 'http://oxpoints.oucs.ox.ac.uk/type/College.json'
        
        conn = urlopen(request_string)
        rsp = simplejson.load(conn)
        
        
        return rsp

    def getMSDUnits(self):

        request_string = 'http://oxpoints.oucs.ox.ac.uk/isPartOf/oucs:medsci.json'

        conn = urlopen(request_string)
        rsp = simplejson.load(conn)


        return rsp
     

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def listColleges(self):
        """
        test method
        """
        
        results_set = self.getColleges()
        
        collegelist = []
        
        for x in results_set:
            Title = x.get('dc_title')
            uri = x.get('uri')
            homepage = x.get('foaf_homepage')
            
            collegelist.append ({'Title': Title,
                'uri': uri,
                'homepage': homepage,
                })
                
        return collegelist
        
    def listUnits(self):
        """
        test method
        """

        results_set = self.getMSDUnits()

        collegelist = []

        for x in results_set:
            Title = x.get('dc_title')
            uri = x.get('uri')
            homepage = x.get('foaf_homepage')

            collegelist.append ({'Title': Title,
                'uri': uri,
                'homepage': homepage,
                })

        return collegelist
    
