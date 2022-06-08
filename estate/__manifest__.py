# -*- coding: utf-8 -*-
{
  'name':'estate',
  
  'depends': ['base_setup', 'web'],
  'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_type.xml',
        'views/property_tag.xml',
        'views/estate_offer.xml',
        'views/resuser.xml'

    ],
    'application': True


}