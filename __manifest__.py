# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright (c) 2022  - Aissa BAMMOUNE - www.my-site.com

{
    'name': 'Algeria - Accounting',
    'description': """
This is the module to manage the accounting chart for Algeria in Odoo.
========================================================================

This module applies to companies based in Algeria.
.

**Email:** probamais@gmail.com
""",
    'author': 'Aissa BAMMOUNE',
    'maintainer': 'Aissa BAMMOUNE',
    'website': 'http://www.my-site.com/',
    'depends': ['account','l10n_dz_region'],
    'category': 'Localization',
    'version': '12.0.1.0.1',
    'license': 'AGPL-3',
    'data': [
#        'data/wizard_data.xml',
        'data/plan_comptable_data.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_template_data.xml',
#        'data/account.account.tag.csv',
#        'data/account.account.template.csv',
#        'data/account.chart.template.csv',
#        'data/account.fiscal.position.tax.template',
#        'data/account.fiscal.position.template',
#        'data/account.tax.template.csv',
        'views/l10n_dz_view.xml',
#        'data/account_chart_template_data.yml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}