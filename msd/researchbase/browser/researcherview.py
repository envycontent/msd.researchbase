from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from msd.researchertemplates import researchertemplatesMessageFactory as _
from Products.validation import validation as validationService


class IBaseView(Interface):
    def isValidEmail(email):
        """ Uses Products.validation to validate email
        
            @return: Boolean value is given email valid or not
        """
        
    def isValidURL(url):
        """ Uses Products.validation to validate url
        
            @return: Boolean value is given url valid or not
        """

class BaseView(BrowserView):
    def isValidEmail(self, email):
    
        validator = validationService.validatorFor('isEmail')
        return validator(email) == 1
    
    def isValidURL(self, url):
        
        validator = validationService.validatorFor('isURL')
        return validator(url) == 1

class IResearcherView(IBaseView):
        
    # methods for core information about a researcher
    #
    def getFullName():
        """
        return fame name as string
        in ORA - foaf_name
        """

    def getLettersAfterName():
        """
        return post-nominals string
        in ORA - res_postNominals
        """

    def getJobTitle():
        """
        return comma-separated string of job-titles
        in ORA res_statusString (which is just a string anyway)
        """
        
    # methods for person_description

    def getGroupName():
        """
        returns the name of the PI's group if they have one
        in ORA - no equivalent?
        """

    def Description():
        """
        returns the short description of the researcher's work
        in ORA - dc_description
        """
        
    def getBiography():
        """
        """
        
    def getAcademicBackground():
        """ """

    def getFundingSources():
        """ """

    def getThemes():
        """ Returns research themes """
        
    def getImageURL():
        """ Returns the url of the researcher image """
        
    def getImageURLMini():
        """ Returns the url of the researcher image scaled if possible"""

    def getImageURLThumb():
        """ Returns the url of the researcher image scaled if possible"""
        
    def getImageCaption():
        """ Returns caption of the researcher image """
        
    def getSummary():
        """ Reserach summary as string """
        
    def getKeywords():
        """ Returns dictionary with keywords assigned to this researcher """

        
from msd.researchtheme.utilities import getResearcherThemes 

from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions

class BaseResearcherView(BaseView):
    """ Base view for ORA and MSD research views """
    implements(IResearcherView)
    security = ClassSecurityInfo()
    
    def getFullName(self):
       
        return self.context.Title()

    def getLettersAfterName(self):
        
        raise NotImplementedError
    
    def getJobTitle(self):
       
        return self.context.getJobTitle() or ""
    
    def getGroupName(self):
       
        raise NotImplementedError
    
    def getImageURL(self):
        raise NotImplementedError
        
    def getImageURLThumb(self):
        raise NotImplementedError

    def getImageURLMini(self):
        raise NotImplementedError
    
    def getImageCaption(self):
        
        return ""
    
    def Description(self):
       
        return self.context.Description()
           

    def getBiography(self):
        """
        """
        
        return self.context.getBiography()
        
    def getAcademicBackground(self):
        """ """
        
        return self.context.getAcademicBackground()

    def getThemes(self):
        
        return getResearcherThemes(self.context)
    
    def getSummary(self):
        
        return self.context.getSummary()
    
    def getKeywords(self):
        
        keywords = []
        settings = self.context.getResearchSettings()        

        customizations = settings.getFieldCustomizations()
        
        for customization in customizations:
            if customization["visible"]:
                values = getattr(self.context, customization["fieldName"], ())
                if len(values) > 0:
                    keywords.append({"label": customization["label"],
                                     "description": customization["description"],
                                     "values": values})
                    
                
        return keywords
    
class IResearcherContactView(IBaseView):

    # methods for person_contact
    
    def getUnits():
        """
        returns a list of units
        - in ORA - foaf_member_pair
        """
    
    def getUnitsWithURLs():
        """
        returns a list of units with URLs (dicts?)
        - we will need to look up the URL from defaultlists.py
        - I think Mikko is going to provide a helper method for this in researchbase 
        """
    # methods to provide ready formatted lists of units (save templating work)
        
    def getUnitsFormatted():
        """
        returns a string of each unit separated by a comma
        """ 
        
    def getUnitsLinked():
        """
        returns a string of each unit tagged with <a>, separated by a comma
        """ 
    #   methods to return the college, we only expect one, if at all
        
    def getCollege():
        """
        returns the name of the PI's college as a string
        in ORA - at this stage it looks as if college isn't included in the json output
        """
        
    def getCollegeWithURL():
        """
        returns the name of the PI's college and a URL
        - the URL will probably need to be looked up in defaultlists.py
        - I think Mikko is going to provide a helper method for this in researchbase 
        
        """
    
    def hasCollege():
        """
        returns true if there is a valid college
        false if the college entry is blank or 'none'
        """
    
    def getUrl():
        """
        returns personal webpages in a list
        in ORA - foaf_homepage
        (we expect valid url)
        """
    
    def getEmail():
        """
        returns email
        in ORA - foaf_mbox
        (we expect valid email)
        """
    
    def getPhone():
        """
        returns phone
        in ORA - con_phone
        (string, no validation required)
        """
    
    def getFax():
        """
        returns fax
        in ORA - con_fax
        (string, no validation required)
        """
    
    def getContactAddress():
        """
        returns contact address, as a string, each line separated by a comma
        in ORA - con_address
        """

        
# it doesn't look as if ORA has the PA name or details
    
    def getPaName():
        """
        returns name of PA
        in ORA?
        (string)
        """
    
    def getPaFax():
        """
        returns PA fax
        in ORA?
        (string)
        """
    
    def getPaEmail():
        """
        returns PA email
        in ORA?
        (valid email address)
        """
        
class BaseResearcherContactView(BaseView):
    implements(IResearcherContactView)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        
        
        #TODO: Not sure if these should be in the init
        self.settings = self.context.getResearchSettings()        
        self.unitData = self.settings.getVocabularyAsDictionary("departmentVocabulary")
        self.collegeData = self.settings.getVocabularyAsDictionary("collegeVocabulary")

    
    def getUnits(self):
        """
        returns a list of units
        - in ORA - foaf_member_pair
        """
        raise NotImplementedError

    def getUnitsWithURLs(self):
        """
        returns a list of units with URLs (dicts?)
        
        @return:[{"name":"..", "url":"http..."},...]
        """
        
        units = self.context.getUnits()
        
        unitsWithURLs = []
        
        for unit in units:
            data = self.unitData.get(unit, None)
            if data:
                unitsWithURLs.append(data)
                
        return unitsWithURLs
        
    def getUnitsFormatted(self):
        """
        returns a string of each unit separated by a comma
        """
        
        units = self.getUnitsWithURLs()
        
        return ", ".join( [unit["name"] for unit in units] )
        
         
        
    def getUnitsLinked(self):
        """
        returns a string of each unit tagged with <a>, separated by a comma

        TODO: Should units without url be skipped or return without <a>?
        """ 

        units = self.getUnitsWithURLs()

        return [ "<a href='%(url)s'>%(name)s</a>" % unit for unit in units]

    def getCollege(self):
        """
        returns the name of the PI's college as a string
        in ORA - at this stage it looks as if college isn't included in the json output
        """
        raise NotImplementedError        
        
        
    def getCollegeWithURL(self):
        """
        returns the name of the PI's college and a URL
        
        """
        
        pass
        
    
    def hasCollege(self):
        """
        returns true if there is a valid college
        false if the college entry is blank or 'none'
        """
        
        return self.getCollege() != ""
    
    def getUrl(self):
        """
        returns personal webpage
        in ORA - foaf_homepage
        (we expect valid url)
        """
        
        raise NotImplementedError
        
    
    def getEmail(self):
        """
        returns email
        in ORA - foaf_mbox
        (we expect valid email)
        """
        
        return self.context.getEmail()
    
    def getPhone(self):
        """
        returns phone
        in ORA - con_phone
        (string, no validation required)
        """
        
        return self.context.getPhone()
    
    def getFax(self):
        """
        returns fax
        in ORA - con_fax
        (string, no validation required)
        """
        
        return self.context.getFax()
    
    def getContactAddress(self):
        """
        returns contact address, as a string, each line separated by a comma
        in ORA - con_address
        """
        
        return self.context.getContact_address()

        
# it doesn't look as if ORA has the PA name or details
    
    def getPaName(self):
        """
        returns name of PA
        in ORA?
        (string)
        """
        
        return self.context.getPa_name()
    
    def getPaFax(self):
        """
        returns PA fax
        in ORA?
        (string)
        """
        
        return self.context.getPa_phone()
    
    def getPaEmail(self):
        """
        returns PA email
        in ORA?
        (valid email address)
        """
        
        return self.context.getPa_email()
    

class IResearcherCollaborationsView(IBaseView):


    # There's a bit of an anomaly here
    # in ora: ox_collaboratesWith":["Liset Pengel","Nish Talawila","Liang Liu",]
    # so basically you don't get much. However
    # msd researcher gives you slightly more:
    # ["fullName", "url", "email", "role", "institution", "type"]
    
    def getCollaborations():
        """
        return a list of dicts?
        [{fullname:(string),role:(string),url:(valid url),institution:(string),type:(string)},]
        NOTE: we don't include email in this as we want to keep this behind the scenes as much as possible
        the idea is to use it as an identifier
        ORA will only have the fullname in each dict.
        Is there a clever way to ensure that the templates aren't tripped up by this?
        """
        
    
    def getGroupMembers():
        """
        listCollaborations but filtered for type == Group Member
        not relevant for ORA which should return an empty list
        """
    
    def getPastGroupMembers():
        """
        listCollaborations but filtered for type == Past Group Member
        not relevant for ORA which should return an empty list
        """
    
    def getCollaborators():
        """
        listCollaborations but filtered for type == Collaborator
        not relevant for ORA which should return an empty list
        """
    
class BaseResearcherCollaborationsView(BaseView):
    implements(IResearcherCollaborationsView)

    # There's a bit of an anomaly here
    # in ora: ox_collaboratesWith":["Liset Pengel","Nish Talawila","Liang Liu",]
    # so basically you don't get much. However
    # msd researcher gives you slightly more:
    # ["fullName", "url", "email", "role", "institution", "type"]
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        
        
        #TODO: Not sure if these should be in the init
        self.settings = self.context.getResearchSettings()        
        self.unitData = self.settings.getVocabularyAsDictionary("departmentVocabulary")    
    
    def getCollaborations(self):
        """
        return a list of dicts?
        [{fullname:(string),role:(string),url:(valid url),institution:(string),type:(string)},]
        NOTE: we don't include email in this as we want to keep this behind the scenes as much as possible
        the idea is to use it as an identifier
        ORA will only have the fullname in each dict.
        Is there a clever way to ensure that the templates aren't tripped up by this?
        
        TODO: add implementation
        """
        
        return []
    
    def getGroupMembers(self):
        """
        listCollaborations but filtered for type == Group Member
        not relevant for ORA which should return an empty list
        """
        #TODO: Not sure if it is better give base view logic here or raise NotImplementedError
        return []
    
    def getPastGroupMembers(self):
        """
        listCollaborations but filtered for type == Past Group Member
        not relevant for ORA which should return an empty list
        """
        #TODO: Not sure if it is better give base view logic here or raise NotImplementedError
        return []
    
    def getCollaborators(self):
        """
        listCollaborations but filtered for type == Collaborator
        not relevant for ORA which should return an empty list
        """
        #TODO: Not sure if it is better give base view logic here or raise NotImplementedError
        return []

 
        