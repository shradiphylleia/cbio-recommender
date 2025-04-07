from cbio_py import cbio_mod as cb

#  tested this becuase dict had class CancerType which was not serializable
def get_all_molecular_profiles_id(molecular_profile_id: str) -> dict:
    molecular_profile =cb.getMolecularProfile(molecularProfileId=molecular_profile_id)
    return molecular_profile

molecular_profile=get_all_molecular_profiles_id("all_stjude_2015_mutations")
print(molecular_profile)


def get_clinical_attribute_study_attr(study_id,clinical_attribute_id)->dict:
    clinical_attr=cb.getClinicalAttributeInStudy(studyId=study_id,clinicalAttributeId=clinical_attribute_id)
    return clinical_attr

ans=get_clinical_attribute_study_attr(study_id='acbc_mskcc_2015',clinical_attribute_id='ADJUVANT_CHEMO')
print(ans)




