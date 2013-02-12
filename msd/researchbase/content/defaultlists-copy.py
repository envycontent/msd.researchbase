"""

    Shared list content on all sites.
    
    Sites can declare additional items to these lists in researcher settings.

"""

def getCollegeList():
    collegelist = [ 
    "http://oxpoints.oucs.ox.ac.uk/id/23232387|Lincoln College|http://www.linc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232483|Wolfson College|http://www.wolfson.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232449|St Edmund Hall|http://www.seh.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232464|St John's College|http://www.sjc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232485|Worcester College|http://www.worc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232466|Somerville College|http://www.some.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232383|Lady Margaret Hall|http://www.lmh.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232427|St Antony's College|http://www.sant.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232385|Linacre College|http://www.linacre.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232425|St Anne's College|http://www.st-annes.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232405|New College|http://www.new.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232366|Green Templeton College|http://www.gtc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232368|Hertford College|http://www.hertford.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232400|Merton College|http://www.merton.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232348|Brasenose College|http://www.bnc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232441|St Cross College|http://www.stx.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232468|St Peter's College|http://www.spc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232398|Mansfield College|http://www.mansfield.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232476|University College|http://www.univ.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232474|Trinity College|http://www.trinity.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232371|Jesus College|http://www.jesus.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232437|St Catherine's College|http://www.stcatz.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232395|Harris Manchester College|http://www.hmc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232392|Magdalen College|http://www.magd.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232357|Exeter College|http://www.exeter.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232414|Pembroke College|http://www.pmb.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232373|Keble College|http://www.keble.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232355|Corpus Christi College|http://www.ccc.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232339|Balliol College|http://www.balliol.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232416|The Queen's College|http://www.queens.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232379|Kellogg College|http://www.kellogg.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232352|Christ Church|http://www.chch.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232410|Nuffield College|http://www.nuff.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232412|Oriel College|http://www.oriel.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232335|All Souls College|http://www.all-souls.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232454|St Hilda's College|http://www.sthildas.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232479|Wadham College|http://www.wadham.ox.ac.uk/",
    "http://oxpoints.oucs.ox.ac.uk/id/23232456|St Hugh's College|http://www.st-hughs.ox.ac.uk/",
    ]
    
    
    return collegelist
    
def getDivThemesList():
    
    themeslist = [
     "cancer|Cancer and Haematology|http://www.medsci.ox.ac.uk/research/themes/cancer",
     "cardioscience|Cardiovascular Science|http://www.medsci.ox.ac.uk/research/themes/cardioscience",
     "diabetes|Diabetes, Endocrinology and Metabolism|http://www.medsci.ox.ac.uk/research/themes/diabetes",
     "infection|Infection and Immunology|http://www.medsci.ox.ac.uk/research/themes/infection",
     "musculoskeletal|Musculoskeletal Science|http://www.medsci.ox.ac.uk/research/themes/musculoskeletal",
     "neuroscience|Neuroscience|http://www.medsci.ox.ac.uk/research/themes/neuroscience",
     "reproduction|Reproduction, Development and Genetics|http://www.medsci.ox.ac.uk/research/themes/reproduction",
     "behaviour|Behavioural Science|http://www.medsci.ox.ac.uk/research/themes/behaviour",
     "bioinformatics|Bioinformatics and Statistics|http://www.medsci.ox.ac.uk/research/themes/bioinformatics",
     "cellbiology|Cell and Molecular Biology|http://www.medsci.ox.ac.uk/research/themes/cellbiology",
     "epidemiology|Clinical Epidemiology|http://www.medsci.ox.ac.uk/research/themes/epidemiology",
     "genetics|Genetics and Genomics|http://www.medsci.ox.ac.uk/research/themes/genetics",
     "health|Health Evaluative Methodologies|http://www.medsci.ox.ac.uk/research/themes/health",
     "imaging|Imaging|http://www.medsci.ox.ac.uk/research/themes/imaging",
     "immunology|Immunology|http://www.medsci.ox.ac.uk/research/themes/immunology",
     "physiology|Integrative Physiology|http://www.medsci.ox.ac.uk/research/themes/physiology",
     "structuralbiology|Protein Science and Structural Biology|http://www.medsci.ox.ac.uk/research/themes/structuralbiology",
     "transcriptionbiology|Transcription Biology|http://www.medsci.ox.ac.uk/research/themes/transcriptionbiology",
     "stemcellbiology|Developmental and Stem Cell Biology|http://www.medsci.ox.ac.uk/research/themes/stemcellbiology",
     "microbiology|Microbiology|http://www.medsci.ox.ac.uk/research/themes/microbiology",
     "drugdiscovery|Drug Discovery|http://www.medsci.ox.ac.uk/research/themes/drugdiscovery",
     "globalhealth|Global Health|http://www.medsci.ox.ac.uk/research/themes/globalhealth",
     "ionchannels|Ion Channels and Transporters|http://www.medsci.ox.ac.uk/research/themes/ionchannels",]
       
    return themeslist
       
def getStatusList():
    
    statuslist = [
        "Other",
        "Professor",
        "Reader",
        "University Lecturer",
        "Clinical Lecturer",
        "Departmental Lecturer",
        "Senior Research Staff",
        "Retired Staff",
        "Graduate Student",
       ]
        
    return statuslist
    
def getTitlesList():
    
    titleslist = [
        "None",
        "Prof.",
        "Dr",
        "Mr",
        "Mrs",
        "Ms",
        "Miss",
        "Rev.",]
        
    return titleslist
    
def getPubInstructionsList():
    
    publist = [
        "Select your option",
        "Take from web (URL provided below)",
        "Take the 10 latest from PubMed",
        "Use the list below",
        "I will email my publications to you",
        ]
        
    return publist
    
def getDepartmentList():
    
    deptlist = ["Peter Medawar Building for Pathogen Research",
                "Weatherall Institute of Molecular Medicine",
                "Wellcome Trust Centre for Human Genetics",
                "BHF Molecular Cardiology Laboratory",
                "Oxford Centre for Gene Function",
                "Oxford Centre for Functional Magnetic Resonance Imaging of the Brain",
                "Oxford Institute for Musculoskeletal Sciences",
                "Department of Biochemistry",
                "Department of Cardiovascular Medicine",
                "Department of Clinical Neurology",
                "Department of Clinical Pharmacology",
                "Department of Experimental Psychology",
                "Department of Medical Oncology",
                "Department of Ophthalmology",
                "Department of Paediatrics",
                "Department of Pharmacology",
                "Department of Physiology, Anatomy and Genetics",
                "Department of Primary Health Care",
                "Department of Psychiatry",
                "Department of Public Health",
                "Nuffield Department of Anaesthetics",
                "Nuffield Department of Clinical Laboratory Sciences",
                "Nuffield Department of Clinical Medicine",
                "Nuffield Department of Obstetrics and Gynaecology",
                "Nuffield Department of Orthopaedic Surgery",
                "Nuffield Department of Surgery",
                "Sir William Dunn School of Pathology",]
                
    return deptlist
 