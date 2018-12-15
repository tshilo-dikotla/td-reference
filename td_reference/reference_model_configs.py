from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'edc_appointment.appointment': 'td_maternal.maternalvisit'})

configs = {
    'td_maternal.maternalultrasoundinitial': ['number_of_gestations'],
    'td_maternal.maternalcontraception': ['srh_referral'],
    'td_maternal.maternalpostpartumdep': ['maternal_visit'],

}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)
