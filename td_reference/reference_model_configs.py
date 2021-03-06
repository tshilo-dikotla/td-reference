from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'edc_appointment.appointment': ['td_maternal.maternalvisit'],
        'td_infant.appointment': ['td_infant.infantvisit']})

configs = {
    'td_maternal.maternalrando': ['rx'],
    'td_maternal.maternalultrasoundinitial': ['number_of_gestations', 'edd_confirmed'],
    'td_maternal.maternalcontraception': ['srh_referral'],
    'td_maternal.rapidtestresult': ['result_date'],
    'td_maternal.maternalpostpartumdep': ['laugh'],
    'td_maternal.cliniciannotes': ['consent_model'],
    'td_infant.infantcliniciannotes': ['consent_model'],
    'td_infant.infantnvpdispensing': ['nvp_prophylaxis'],
    'td_infant.infantarvproph': ['arv_status'],
    'td_infant.infantfu': ['has_dx', 'physical_assessment'],
    'td_infant.infantfeeding': ['formula_intro_occur'],
    'td_infant.infantbirthdata': ['congenital_anomalities'],
    'td_infant.karabotuberculosishistory': ['put_offstudy']
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
