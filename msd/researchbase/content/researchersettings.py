"""

    Definition of the ResearcherSettings content type.
    
    This is most used to store all kind of vocabulary related to the researchers.
    
    Vocabularies can be defined in two ways:
    
        * One entry per line. This entry is both id and name at the same time.
        
        * Two entries per line, separated by | character. In this case first half is id, the second half is name.
          This allows painless rename of entries later, without need to migrate content data.


"""

import logging
from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.CMFCore.utils import getToolByName

# from Products.CMFCore.utils import UniqueObject
from Products.Archetypes.public import DisplayList
from Products.Archetypes.utils import OrderedDict
from Products.Archetypes.Schema import getSchemata


from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn
from Products.DataGridField.CheckboxColumn import CheckboxColumn

# -*- Message Factory Imported Here -*-

from msd.researchbase.interfaces import IResearcherSettings
from msd.researchbase.config import PROJECTNAME

import defaultlists

COLLEGE_VOCABULARY_NAME = "collegeVocabulary"

logger = logging.getLogger("msg.researchbase")

ResearcherSettingsSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    
# 

    # atapi.LinesField(
    #     name='unitVocabulary',
    #     default=['Senior Management','Senior Research Staff','Administrative Officers'],
    #     widget=atapi.LinesWidget(
    #         label="Unit Categories",
    #         description="Roles or staff groupings within your department or unit.",
    #     ),
    #     searchable=0,
    #     schemata="default"
    # ),
    
# we list all the Divisional departments, but sometimes they need to mention a department
# outside the Division, so this list needs to be added to the department/unit vocab

    atapi.LinesField(
        name='departmentVocabulary',
        widget=atapi.LinesWidget(
            label="Additional Departments in the Division",
            description="The default list contains top level departments and units. \
                        You can augment this list here.",
        ),
       defaultList=defaultlists.getDepartmentList,
       searchable=0,
       schemata="General Lists"
    ),
    

     atapi.LinesField(
         name='collegeVocabulary',
         widget=atapi.LinesWidget(
             label="Additional Colleges",
             description="The default list contains all colleges. \
                         You can augment this list here. Give one per line with id|title|url or id|title formatting",
         ),
        defaultList=defaultlists.getCollegeList,
        searchable=0,
        schemata="General Lists"
     ),
    
    atapi.LinesField(
        name='honorificTitlesVocabulary',
        widget=atapi.LinesWidget(
            label="Additional honorific titles",
        ),
       defaultList=defaultlists.getTitlesList,
       searchable=0,
       schemata="General Lists"
    ),    
        
    
# eliminating the possibility of additional divisional themes, they are either set by the Division
# or they don't exist
    # 
    # atapi.LinesField(
    #     name='divthemes',
    #     widget=atapi.LinesWidget(
    #         label="Additional Divisional Themes",
    #         description="Enter Additional Divisional Themes here",
    #     ),
    #     schemata="Keyword Lists",
    #     searchable=0
    # ),
    
# I've renamed all these fields to vocabbox[number]

   atapi.LinesField(
        name='vocabbox1',
        widget=atapi.LinesWidget(
            label="Vocab Box 1",
            description="Enter vocabulary for vocab box 1",
        ),
        schemata="Keyword Lists",
        searchable=0
    ),

   atapi.LinesField(
        name='vocabbox2',
        # name='unitthemes',
        default=["Unit Category A", "Unit Category B"],
        widget=atapi.LinesWidget(
            label="Vocab Box 2",
            description="Enter vocabulary for vocab box 2",
        ),
        schemata="Keyword Lists",
        searchable=0
    ),

    
    atapi.LinesField(
        name='vocabbox3',
        widget=atapi.LinesWidget(
            label="Vocab Box 3",
            description="Enter vocabulary for vocab box 3",
        ),
        schemata="Keyword Lists",
        searchable=0
    ),

    atapi.LinesField(
        name='vocabbox4',
        widget=atapi.LinesWidget(
            label="Vocab Box 4",
            description="Enter vocabulary for vocab box 4",
            # description="Provide a list of diseases and disorders, one per line",
        ),
        schemata="Keyword Lists",
        searchable=0
    ),
    
    atapi.LinesField(
        name='vocabbox5',
        widget=atapi.LinesWidget(
            label="Vocab Box 5",
            description="Enter vocabulary for vocab box 5",
            # description="Provide a list of resources and equipment, one per line",
        ),
        schemata="Keyword Lists",
        searchable=0
    ),

    # atapi.LinesField(
    #     name='countries',
    #     widget=atapi.LinesWidget(
    #         label="Countries",
    #         description="A list of countries (used for the Contact fields).",
    #         label_msgid='RDSLocal_label_countries',
    #         description_msgid='RDSLocal_help_countries',
    #         i18n_domain='RDSLocal',
    #     ),
    #     schemata="Other Vocabularies",
    #     default=['United Kingdom',],
    # ),
    # 
    # atapi.LinesField(
    #     name='funding_bodies',
    #     widget=atapi.LinesWidget(
    #         label="Funding Bodies",
    #         description="A temporary list of funding bodies",
    #         label_msgid='RDSLocal_label_funding_bodies',
    #         description_msgid='RDSLocal_help_funding_bodies',
    #         i18n_domain='RDSLocal',
    #     ),
    #     schemata="Other Vocabularies"
    # ),
    # 
    # 
    # 
    # atapi.BooleanField(
    #     name='publicationsDisplay',
    #     default=0,
    #     widget=atapi.BooleanWidget(
    #         label="Display Publications section?",
    #         description="Tick the box if you wish to gather information from the user about publications",
    #         label_msgid='RDSLocal_label_publicationsDisplay',
    #         description_msgid='RDSLocal_help_publicationsDisplay',
    #         i18n_domain='RDSLocal',
    #     ),
    #     schemata="Publications"
    # ),
    
# it would be nice to keep this, but not essential - what I would like to do is hide some of the schemata
# that come as 'standard' with the Plone interface, because they get confusing for the editor in this context
    
    # DataGridField('researcherSchemata',
    #     columns=("schemataName", "schemataDescription",),
    #     widget = DataGridWidget(
    #         label='Researcher Schemata',
    #         description='Organize the field categories for the researcher content type',
    #         columns={
    #             'schemataName' : SelectColumn("Name", vocabulary="listPersonSchemata"),
    #             'schemataDescription' : Column("Description"),
    #         },
    #      ),
    #     schemata = "Researcher Setup",
    #     default = ({'schemataName':'default','schemataDescription':'Name, title and qualifications'},
    #                {'schemataName':'Research Summary','schemataDescription':'Description of research interests, methods and funding'},
    #                {'schemataName':'Collaboration','schemataDescription':'Group Members and other collaborators'},
    #                {'schemataName':'Biography','schemataDescription':'Biographical details and qualifications'},
    #                {'schemataName':'Themes','schemataDescription':'Research themes and keywords'},
    #                {'schemataName':'Affiliations','schemataDescription':'University and department affiliations'},
    #                {'schemataName':'Contact','schemataDescription':'Contact information'},
    #                {'schemataName':'Image','schemataDescription':'A representative image or portrait'},
    #                ),
    # ),
    
    DataGridField('fieldCustomizations',
        columns=("fieldName", "visible", "label", "description","vocabToUse"),
        widget = DataGridWidget(
            label='Researcher field customization',
            description='Show or hide keyword fields, assign labels and vocabulary lists',
            columns={
                'fieldName' : Column("Field Name"),
                'visible' : CheckboxColumn("Visible"),
                'label' : Column("Label"),
                'description' : Column("Description"),
                'vocabToUse': SelectColumn("Choose a Vocabulary", vocabulary="listVocabSources"),
            },
         ),
        default =  ({'fieldName':'keywords1','visible': '1', 'label':'MSD Themes', 'description':'Themes and Platform Technologies defined by the Medical Sciences Division', 'vocabToUse':'getDivThemesList' },
           {'fieldName':'keywords2','visible': '1', 'label':'Unit Categories', 'description':'Categories of research defined by the Unit', 'vocabToUse':'vocabbox2' },
         {'fieldName':'keywords3','visible': '0', 'label':'Keywords', 'description':'Keywords', 'vocabToUse':'vocabbox3' },
         {'fieldName':'keywords4','visible': '0', 'label':'Keywords', 'description':'Keywords', 'vocabToUse':'vocabbox4' },
         {'fieldName':'keywords5','visible': '0', 'label':'Keywords', 'description':'Keywords', 'vocabToUse':'vocabbox5' },
                    ),
        schemata = "Researcher Setup",
    ),
    
    
    
    DataGridField('schemataCustomizations',
        columns=("schemataName", "visible"),
        widget = DataGridWidget(
            label='Schemata customization',
            description='Decide which schemas should be displayed',
            columns={
                'schemataName' : SelectColumn("Name", vocabulary="listResearcherSchemata"),
                'visible' : CheckboxColumn("Visible"),
            },
         ),
        default = (
                   {'schemataName':'categorization','visible': '0'},
                   {'schemataName':'dates','visible': '0'},
                   {'schemataName':'ownership','visible': '0'},
                   {'schemataName':'settings','visible': '0'},
                   ),
        schemata = "Researcher Setup",
    ),    
    
    # not bothering with these any longer - I believe I've removed all of these from the researcher schemata
    
    # DataGridField('researcherOptFieldSelector',
    #     columns=("fieldName", "display", "labelText", "descriptionText",),
    #     widget = DataGridWidget(
    #         label='Researcher Optional Fields',
    #         description='Decide which of the optional researcher fields should be displayed',
    #         columns={
    #             'fieldName' : SelectColumn("Field Name", vocabulary="listResearcherOptFields"),
    #             'display' : CheckboxColumn("Display?"),
    #             'labelText' : Column("Label"),
    #             'descriptionText' : Column("Description"),
    #         },
    #      ),
    #     default=({'fieldName':'isPI','display':'1', 'labelText':'Principal Investigator?', 'descriptionText':'Tick this box if you are a PI'},
    #              {'fieldName':'status','display':'1', 'labelText':'University Status', 'descriptionText':'Your University Status'},
    #              {'fieldName':'localstatus','display':'1', 'labelText':'Department/Unit Status', 'descriptionText':'Your Department or Unit Status'},
    #              {'fieldName':'nativeLanguage','display':'', 'labelText':'Languages', 'descriptionText':'Languages'},
    #              {'fieldName':'location','display':'', 'labelText':'Location', 'descriptionText':'Your geographic location'},
    #              {'fieldName':'institution','display':'', 'labelText':'Institution', 'descriptionText':'Your Institution'},
    #              {'fieldName':'country_of_research','display':'', 'labelText':'Country of Research', 'descriptionText':'Country of Research'},
    #              {'fieldName':'interests','display':'', 'labelText':'Interests', 'descriptionText':'Your Interests'},
    #              {'fieldName':'additional_info','display':'', 'labelText':'Additional Information', 'descriptionText':'Additional Information'},
    #              {'fieldName':'pubInstructions','display':'', 'labelText':'Publication Instructions', 'descriptionText':'Tell us where to find your publications'},
    #              {'fieldName':'publicationsText','display':'', 'labelText':'Publications', 'descriptionText':'Provide a list of your publications'},
    #              {'fieldName':'includeAbstracts','display':'', 'labelText':'Include Abstracts', 'descriptionText':'If you would prefer us NOT to include your abstracts, clear this box'},
    #             ),
    #     schemata = "Researcher Setup",
    # ),
    # 
    # DataGridField('projectFieldSelector',
    #     columns=("fieldName", "display", "labelText", "descriptionText",),
    #     widget = DataGridWidget(
    #         label='Project Fields',
    #         description='Decide which fields should be displayed',
    #         columns={
    #             'fieldName' : SelectColumn("Field Name", vocabulary="listProjectFields"),
    #             'display' : CheckboxColumn("Display?"),
    #             'labelText' : Column("Label"),
    #             'descriptionText' : Column("Description"),
    #         },
    #      ),
    #     schemata = "Project Setup",
    # ),
    # 
    # DataGridField('projectSchemata',
    #     columns=("schemataName", "schemataDescription",),
    #     widget = DataGridWidget(
    #         label='Project Schemata',
    #         description='Organize the field categories for the project content type',
    #         columns={
    #             'schemataName' : SelectColumn("Name", vocabulary="listProjectSchemata"),
    #             'schemataDescription' : Column("Description"),
    #         },
    #      ),
    #     schemata = "Project Setup",
    # ),
    # 
    # atapi.LinesField(
    #     name='projectStatusList',
    #     default=["completed","in progress"],
    #     widget=atapi.LinesWidget(
    #         label="Project Status",
    #         description="Provide a list of project statuses, one per line",
    #         label_msgid='RDSLocal_label_resourcesList',
    #         description_msgid='RDSLocal_help_resourcesList',
    #         i18n_domain='RDSLocal',
    #     ),
    #     schemata="Other Vocabularies",
    #     searchable=0
    # ),


))

ResearcherSettingsSchema["title"].widget.visible = {"edit": "invisible", "view" : "invisible" } 
ResearcherSettingsSchema["description"].widget.visible = {"edit": "invisible", "view" : "invisible" }

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

schemata.finalizeATCTSchema(ResearcherSettingsSchema, moveDiscussion=False)


class ResearcherSettings(base.ATCTContent):
    """This tool supplies site-wide settings for Research content types"""
    implements(IResearcherSettings)

    meta_type = "ResearcherSettings"
    schema = ResearcherSettingsSchema

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

   # tool should not appear in portal_catalog
    def at_post_edit_script(self):
        self.unindexObject()
        

    # Methods
    
    def listResearcherSchemata(self):
        ##returns a list of person schemata ##

       at_tool = getToolByName(self, 'archetype_tool')
       contenttype = at_tool.lookupType('msd.researcher','Researcher')

       vocablist = contenttype['schema'].getSchemataNames()
       
       results = []
       
       for x in vocablist:
           results.append([x,x])
           
       vocablisttuple = tuple(results)
       return atapi.DisplayList(vocablisttuple)
        
#     def listProjectSchemata(self):
#         ##returns a list of project schemata ##
#         return atapi.DisplayList([])
#         
# #        at_tool = getToolByName(self, 'archetype_tool')
# #        type = at_tool.lookupType('RDSLocal','Project')
# #
# #        vocablist = type['schema'].getSchemataNames()
# #        
# #        results = []
# #        
# #        for x in vocablist:
# #            results.append([x,x])
# #        vocablisttuple = tuple(results)
# #        return atapi.DisplayList(vocablisttuple)
#         
#     
#     def listProjectFields(self):
#         """returns a list of project fields"""
#         
#         #at_tool = getToolByName(self, 'archetype_tool')
#         #type = at_tool.lookupType('RDSLocal','Person')
# 
#         vocablist = ['themes1','themes2','themes3','themes4','themes5']
#         
#         results = []
#         
#         for x in vocablist:
#             results.append([x,x])
#         vocablisttuple = tuple(results)
#         return atapi.DisplayList(vocablisttuple)



        
    def listResearcherFields(self):
        """returns a list of researcher theme fields"""
        
        #at_tool = getToolByName(self, 'archetype_tool')
        #type = at_tool.lookupType('RDSLocal','Person')

        vocablist = ['themes1','themes2','themes3','themes4','themes5']
        
        results = []
        
        for x in vocablist:
            results.append([x,x])
        vocablisttuple = tuple(results)
        return atapi.DisplayList(vocablisttuple)
        
    # def listResearcherOptFields(self):
    #     """returns a list of researcher optional fields"""
    #     
    #     #at_tool = getToolByName(self, 'archetype_tool')
    #     #type = at_tool.lookupType('RDSLocal','Person')
    # 
    #     vocablist = ['isPI',
    #                  'status',
    #                  'localstatus',
    #                  'nativeLanguage',
    #                  'location',
    #                  'institution',
    #                  'country_of_research',
    #                  'interests',
    #                  'additional_info',
    #                  'pubInstructions',
    #                  'publicationsText',
    #                  'includeAbstracts',]
    #     
    #     results = []
    #     
    #     for x in vocablist:
    #         results.append([x,x])
    #     vocablisttuple = tuple(results)
    #     return atapi.DisplayList(vocablisttuple)

    def listVocabSources(self):
        """returns a list of possible vocab sources"""

        
#        results = [['listDivThemes', 'MSD Themes'],
#                   ['vocabbox1','Box 1'],
#                   ['unitthemes','Box 2'],
#                   ['subthemes', 'Box 3'],
#                   ['disordersList', 'Box 4'],
#                   ['resourcesList', 'Box 5'],]
        
        results = [("getDivThemesList", "MSD Themes"),
                   ("vocabbox1", "Vocabulary Box 1"),
                   ("vocabbox2", "Vocabulary Box 2"),
                   ("vocabbox3", "Vocabulary Box 3"),
                   ("vocabbox4", "Vocabulary Box 4"),
                   ("vocabbox5", "Vocabulary Box 5"),                                                         
        ]
        
        return atapi.DisplayList(results)
    
    def getCombinedVocabularyList(self, name):
        """
            This will combine vocabularies from the default list and additional 
            list to one list
            
            @param name: Name of the vocabulary
            
            @return: List of default and additional parts of the vocabulary
        """
        field = self.Schema().get(name, None)

        if field:

            # LinesField holds value in tuple() need to convert to list() for merge
            value = list(field.get(self))
            
            # Call function to get defaults
            defaultCallback = getattr(field, "defaultList", None)

        else:
            # No settings -> directly read the default list
            value = []
            
            defaultCallback = getattr(defaultlists, name, None)

        if defaultCallback:
            # Order custom values last
            value = defaultCallback() + value
            
        return value
            
    def getVocabulary(self, name):
        """
        Convert lines field to vocabulary.
        
        DisplayList to be used to populate AT edit widgets.
        
        The vocab must be in LinesField in format:
        
            idandtitle
            id|title
            id2|title2
            
        or
        
            id|title|url
        
        """

        tuples = []
        
        terms = self.getVocabularyAsDictionary(name)
        
        for id,value in terms.iteritems():
            tuples.append((id, value["name"]))
             
        return atapi.DisplayList(tuples)
        
    def parseVocabularyList(self, list):
        """ Parses list of vocabulary strings. Expects id, id|name or id|name|url formatted list elements.
            
            @param list: Vocabulary list with id, id|name or id|name|url formatted elements
            
            @return Dictionary with following style {"id" : {"name":name, "url":url} }
        """
        
        dict = {}
        
        for v in list:
            url = ""
            
            v = v.strip()
            if v == "":
                continue
        
            if "|" in v:
                # 2 entries
                try:
                    id, name = v.split("|")
                except ValueError:
                    #Atleast colleges can have also url.
                    id, name, url = v.split("|")
            else:
                # 1 entry
                id = name = v # Assume id and the name is the same
                
            dict[id] = {"name": name, "url":url}
            
        return dict
                
    
    def getVocabularyAsDictionary(self, vocabulary_name):
        """ 
        @param vocabulary_name: Name of the vocabulary wanted
        @return: Dictionary with parsed contents of the vocabulary
        """
        vocabulary_list = self.getCombinedVocabularyList(vocabulary_name)
        
        #Parse into dictionary so it is easy to get the wanted content
        return self.parseVocabularyList(vocabulary_list)
        
    def getAttributeFromVocabulary(self, vocabulary_name, id, attribute_name):
        """
        Returns attribute from from the given vocabulary and id
        
        @param vocabulary_name: Name of the vocabulary to search as a String
        @param id: String id of the vocabulary terms, which are either id, id|name or id|name|url format
        @param attribute_name: Name of the attribute you want as a String. Currently either name or url
        
        @return: String value of the found attribute. If not found an empty string. 
        """
        
        value = ""

        dict = self.getVocabularyAsDictionary(vocabulary_name)
        
        obj = dict.get(id, None)
        
        if obj:
            value = obj.get(attribute_name, "")
            
        return value
        
#Will these be in the views or here?    
#    def getName(self, id, vocabulary_name):
#        """ Returns name of the college with given id. 
#            Name is searched from the college vocabulary.
#            
#            @param id: String id of college
#            @return: Name of the found college as a string. If not found empty string
#        """
#        return self.getAttributeFromVocabulary( vocabulary_name, id, "name")
#    
#    def getCollegeUrl(self, id):
#        return self.getAttributeFromVocabulary("collegeVocabulary", id, "url",, )

    def getFieldCustomization(self, fieldName, ruleName):
        """
        Look-up customizations from the stored datagrid.
        """
        
        customizations = self.getFieldCustomizations()
        for row in customizations:
            if row.get("fieldName", None) == fieldName:
                return row.get(ruleName, None)
            
        return None
    

    def getSchemataVisibility(self, schemataName):
        """
        Look-up customizations from the stored datagrid.
        """
        
        customizations = self.getSchemataCustomizations()
        for row in customizations:
            if row.get("schemataName", None) == schemataName:
                return row.get("visible", None)
            
        return None
        
    def Schemata(self):
        """overrides the baseobject Schemata method
        """        

        namelist = ['Researcher Setup','Keyword Lists', 'General Lists']

        if namelist:

            currentSchemata = getSchemata(self)
            customSchemata = OrderedDict()

            currentkeys = currentSchemata.keys()

            for key in namelist:
                if key in currentkeys:
                    customSchemata[key] = currentSchemata[key]

            return customSchemata

        else:

            return getSchemata(self)

    
atapi.registerType(ResearcherSettings, PROJECTNAME)
