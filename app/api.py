from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cbio_py import cbio_mod as cb

from recommender import recommeder_similar_patients

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def landing():
    return {'cbio': 'gsoc_2025'}

@app.get('/similar_patients')
def get_similar_patients():
    return recommeder_similar_patients()

@app.get('/sample')
def get_all_samples(limit:int=10,offset:int=0):

    """
    Return a list of sample patients

    Args:
    none

    Returns:
    dict: list of all sample patients

    example:
    "category":,
    "description":,
    "name":,
    "sampleCount":,
    "sampleIds":,
    "sampleListId":,
    "studyId":
    """
    samples = cb.getAllSamplesList()
    length=len(samples)
    paginated=samples[offset:offset+limit]


    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }

@app.get('/specific/studyId/{study_id}')
def get_sample_list(study_id: str,limit:int=10,offset:int=0):
    """
    Return a list of samples for a given studyID.

    Args:
    StudyId: str

    Returns:
        dict: List of samples for a given studyID
    """
    samples=cb.getAllSamplesInStudy(studyId=study_id)
    length=len(samples)
    paginated=samples[offset:offset+limit]

    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }


@app.get('/samples_study/studyId/{study_id}')
def get_all_samples_in_study(study_id:str, limit:int=10,offset:int=0):
    """
    Return a list of samples for the given study id
    """
    samples=cb.getAllSamplesInStudy(study_id)
    length=len(samples)
    paginated=samples[offset:offset+limit]

    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }


# molecular profile
@app.get('/molecular_profile')
def get_all_molecular_profiles(limit:int=10,offset:int=0)->dict:
    molecular_profiles=cb.getAllMolecularProfiles()
    length=len(molecular_profiles)
    paginated=molecular_profiles[offset:offset+limit]
    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }

# needed work because of cacertype class
@app.get('/molecular_profile_id/{molecular_profile_id}')
def get_all_molecular_profiles_id(molecular_profile_id: str) -> dict:
    molecular_profile = cb.getMolecularProfile(molecularProfileId=molecular_profile_id)
    result={}
    for key, value in molecular_profile.items():
        if hasattr(value,'__class__') and value.__class__.__name__ == 'CancerStudy':
            study_dict = {}
            for study_attr in dir(value):
                if not study_attr.startswith('_') and not callable(getattr(value, study_attr)):
                    study_dict[study_attr]=getattr(value, study_attr)
            result[key]=study_dict
        else:
            result[key]=value
    
    return result


@app.get('/mutation/molecular_profile/molecularProfileId/{molecular_profile_id}/sampleId/{sample_id}')
def get_mutations_molecular_profile(molecular_profile_id,sample_id,limit:int=10,offset:int=0)-> dict:
    mutations=cb.getMutationsInMolecularProfile(molecular_profile_id,sampleListId=sample_id,projection='DETAILED',append='yes')
    length=len(mutations)
    paginated=mutations[offset:offset+limit]

    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }


# cancer types
@app.get('/cancer/types')
def get_all_cancer_types(limit:int=10,offset:int=0)-> dict:
    cancer_types=cb.getAllCancerTypes()
    length=len(cancer_types)
    paginated=cancer_types[offset:offset+limit]

    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }

# clinical attributes
@app.get('/clinical_attributes')
def get_clinical_attribute(limit:int=10,offset:int=0)->dict:
    clinical_attr=cb.getAllClinicalAttributes()
    length=len(clinical_attr)
    paginated=clinical_attr[offset:offset+limit]

    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }

@app.get('/clinical_attribute/studyId/{study_id}')
def get_clinical_attribute_studyid(study_id,limit:int=10,offset:int=0)->dict:
    clinical_attr=cb.getClinicalAttributesByStudyId(studyId=study_id)
    length=len(clinical_attr)
    paginated=clinical_attr[offset:offset+limit]

    return{
        "total":length,
        "offset":offset,
        "limit":limit,
        "results":paginated
        }


@app.get('/clinical/attribute/studyId/{study_id}/clinicalAttributeId/{clinical_attribute_id}')
def get_clinical_attribute_study_attr(study_id,clinical_attribute_id,limit:int=10,offset:int=0)->dict:
    clinical_attr=cb.getClinicalAttributeInStudy(studyId=study_id,clinicalAttributeId=clinical_attribute_id)
    return dict(clinical_attr)      