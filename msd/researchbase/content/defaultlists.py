"""

    Shared list content on all sites.
    
    Sites can declare additional items to these lists in researcher settings.

"""

#uid|name|url
def getCollegeList():
    collegelist = [ 
    "http://oxpoints.oucs.ox.ac.uk/id/00000000|No College|None",
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
    
    deptlist = ["medawar|Peter Medawar Building for Pathogen Research|http://www.medawar.ox.ac.uk",
                "imm|Weatherall Institute of Molecular Medicine|http://www.imm.ox.ac.uk",
                "wtchg|Wellcome Trust Centre for Human Genetics|http://www.wellcome.ox.ac.uk",
                "bhfmcl|BHF Molecular Cardiology Laboratory|http://www.bhfmcl.ox.ac.uk",
                "ocgf|Oxford Centre for Gene Function|http://www.ocfg.ox.ac.uk",
                "fmrib|Oxford Centre for Functional Magnetic Resonance Imaging of the Brain|http://www.fmrib.ox.ac.uk",
                "oims|Oxford Institute for Musculoskeletal Sciences|http://www.oims.ox.ac.uk",
                "bioch|Department of Biochemistry|http://www.bioch.ox.ac.uk",
                "cardiov|Department of Cardiovascular Medicine|http://www.cardiov.ox.ac.uk",
                "clneuro|Department of Clinical Neurology|http://wwww.clneuro.ox.ac.uk",
                "clinpharm|Department of Clinical Pharmacology|http://www.clinpharm.ox.ac.uk",
                "psy|Department of Experimental Psychology|http://www.psy.ox.ac.uk",
                "medonc|Department of Medical Oncology|http://www.medonc.ox.ac.uk",
                "eye|Department of Ophthalmology|http://www.eye.ox.ac.uk",
                "paeds|Department of Paediatrics|http://www.paediatrics.ox.ac.uk",
                "pharm|Department of Pharmacology|http://www.pharm.ox.ac.uk",
                "dpag|Department of Physiology, Anatomy and Genetics|http://www.dpag.ox.ac.uk",
                "ndcn|Nuffield Department of Clinical Neurosciences|http://www.ndcn.ox.ac.uk",
                "oncology|Department of Oncology|http://www.oncology.ox.ac.uk",
                "phc|Department of Primary Care Health Sciences|http://www.phc.ox.ac.uk",
                "psych|Department of Psychiatry|http://www.psych.ox.ac.uk",
                "dph|Department of Public Health|http://www.dph.ox.ac.uk",
                "nda|Nuffield Department of Anaesthetics|http://www.nda.ox.ac.uk",
                "ndcls|Nuffield Department of Clinical Laboratory Sciences|http://www.ndcls.ox.ac.uk",
                "ndm|Nuffield Department of Clinical Medicine|http://www.ndm.ox.ac.uk",
                "ndog|Nuffield Department of Obstetrics and Gynaecology|http://www.ndog.ox.ac.uk",
                "ndorms|Nuffield Department of Orthopaedics, Rheumatology and Musculoskeletal Sciences|http://www.ndorms.ox.ac.uk",
                "nds|Nuffield Department of Surgical Sciences|http://www.nds.ox.ac.uk",
                "path|Sir William Dunn School of Pathology|http://www.path.ox.ac.uk",]
                
    return deptlist
 