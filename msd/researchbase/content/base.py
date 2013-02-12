"""

    Resarcher content type helpers.

"""

from cStringIO import StringIO

from Acquisition import ImplicitAcquisitionWrapper

from Products.Archetypes import atapi
from Products.Archetypes.interfaces import ISchema
from Products.Archetypes.Schema import getSchemata


from Products.CMFCore.utils import getToolByName


from msd.researchbase.utilities import getResearcherSettings
from msd.researchbase.content import defaultlists

from msd.researchbase import researchbaseMessageFactory as _

class ResearcherMixin(object):
    """
    Add shared methods to ORA researcher and msd.researcher both.
    
    Mainly used for filling up vocabularies.    
    """
    
    def getCachedValue(self, name):

        # Cache the result of this method in HTTP request object
        request = getattr(self, 'REQUEST', None)
        
        if isinstance(request, str):
            # XXX: Don't know what this case is? Related to TinyMCE
            return None
        
        if request is not None:
            cached = getattr(request, name, None)        
            return cached
            
        return None
    
    def setCachedValue(self, name, value):
        """
        """
        # Cache the result of this method in HTTP request object
        request = getattr(self, 'REQUEST', None)
        
        if isinstance(request, str):
            # XXX: Don't know what this case is? Related to TinyMCE
            return 
            
        setattr(request, name, value)
        
    def getResearchSettings(self):
        """
        Get access to settings object.
        """
        
        key = "researcher_settings"
        
        cached = self.getCachedValue(key)
        if cached is not None:
            return cached
        
        settings = getResearcherSettings(self)
        
        #self.setCachedValue(key, settings)
        
        return settings

    def getResearchSettingsVocabulary(self, name):
        """
        Get a named vocabulary from the settings.
        """
        settings = self.getResearchSettings()
        return settings.getVocabulary(name)

    def getDepartmentVocabulary(self):
        """ """
        return self.getResearchSettingsVocabulary("departmentVocabulary")

    def getCollegeVocabulary(self):
        """"""
        return self.getResearchSettingsVocabulary("collegeVocabulary")

    def getHonorificTitlesVocabulary(self):
        """ """
        return self.getResearchSettingsVocabulary("honorificTitlesVocabulary")
                
    def Schema(self):
        """ Overrides field definitions in fly.
        
        Note that you want to cache the result of this method as it is called 
        many times when rendering view / edit for the content item.
        """        
                            
        schema = self.getCachedValue("researcher_schema")
        if schema is not None:
            return schema

        #print "Re-creating schema"
                
        # Create modifiable copy of schema
        # See Products.Archetypes.BaseObject1
        schema = ISchema(self)
        schema = schema.copy()
        schema = ImplicitAcquisitionWrapper(schema, self)
        
        settings = self.getResearchSettings()
        
        for row in settings.getFieldCustomizations():
            name = row.get("fieldName", None)
            vocab = row.get("vocabToUse", None)
            
            field = schema.get(name, None)
                
            if field and vocab and hasattr(field, "vocabulary"):
                # Modify field copy ion 
                
                displayList = settings.getVocabulary(vocab)
                if displayList is not None:
                    field.vocabulary = displayList
        
        self.setCachedValue("researcher_schema", schema)
        
        return schema
    

    def listCollabTypes(self):
        """ Vocabulary list to populate collaborator column in collaborators datagrid field
            I choose to set this in stone.
        """
        return atapi.DisplayList(
            (("member", _(u"Group Member"),),
             ("past", _(u"Past Group Member"),),
             ("collaborator", _(u"Collaborator"),),
             
             ))    
        
        
    def getCollegeSearchableText(self):
        """ Convert stored college data to searchable text """
        raise NotImplementedError("Subclass must implement")

    def getUnitsSearchableText(self):
        """ Convert stored unit data to searchable text """
        raise NotImplementedError("Subclass must implement")

    def SearchableText(self):
        """
        Override searchable text logic based on the requirements.
        
        This method constructs a text blob which contains all full-text
        searchable text for this content item. 
        
        This method is called by portal_catalog to populate its SearchableText index.
        
        Title
        Description
        getSummary (HTML)
        getBiography (HTML)
        getUnits
        getCollege
        getKeywords1
        getKeywords2
        getKeywords3
        getKeywords4
        getKeywords5
        """
        
        # Test this by enable pdb here and run catalog rebuild in ZMI
        # import pdb ; pdb.set_trace()
        
        # Speed up string concatenation ops by using a buffer
        entries = []
        
        # plain text fields we index from ourself,
        # a list of accessor methods of the class
        plain_text_fields = ("Title", "Description")
        
        # HTML fields we index from ourself
        # a list of accessor methods of the class
        html_fields = ("getSummary", "getBiography")
        
        
        def read(accessor):
            """
            Call a class accessor method to give a value for certain Archetypes field.
            """
            try:
                value = accessor()
            except:
                value = ""

            if value is None:
                value = ""
                                        
            return value
            
        
        # Concatenate plain text fields as is 
        for f in plain_text_fields:
            accessor = getattr(self, f)
            value = read(accessor)            
            entries.append(value)
        
        transforms = getToolByName(self, 'portal_transforms')

        # Run HTML valued fields through text/plain conversion
        for f in html_fields:
            accessor = getattr(self, f)            
            value = read(accessor)     
            
            if value != "":                 
                stream = transforms.convertTo('text/plain', value, mimetype='text/html')
                value = stream.getData()
            
            entries.append(value)

        # Plone accessor methods assume utf-8
        def convertToUTF8(text):
            if type(text) == unicode:
                return text.encode("utf-8")
            return text

        # Then some special entries which differ between ORA and normal Plone researcher
        entries.append(self.getCollegeSearchableText())
        entries.append(self.getUnitsSearchableText())
        
        # Then the custom keyword fields
        
        for i in range(1, 5):
            fieldname = "keywords" + str(i)
            field = self.Schema()[fieldname]
            value = field.get(self)
            vocab = field.vocabulary
            # field value is list of vocabulary keys
            # translate each of them to vocab value and add to searchable 
            # text 
            for key in value:
                text = vocab.getValue(key, "")
                entries.append(text)   

                                
        entries = [ convertToUTF8(entry) for entry in entries ]
        
        # Concatenate all strings to one text blob
        return " ".join(entries)
        
