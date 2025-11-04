{
    'name': 'Delivery Restriction on Holidays and Weekends',
    'version': '19.0.1',
    'summary':
        """
  Auto-adjusts delivery dates in sales orders to skip weekends and holidays, ensuring accurate, business-day-based scheduling.

    """,
    'description': """
    ✔ Automatically skips weekends and public holidays when calculating delivery dates  
    ✔ Ensures delivery schedules are based only on working business days  
    ✔ Respects configured company holidays and product/customer lead times  
    ✔ Improves delivery accuracy and customer satisfaction

    This module adjusts sales order delivery dates by excluding weekends and configured company holidays. If a computed delivery date falls on a non-working day, it is automatically moved to the next business day, ensuring reliable and accurate delivery scheduling.
    """,

    'category': 'Sales',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com/',
    'license': 'OPL-1',
    'price': 55.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['base', 'sale_management', 'account', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/company_holiday.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
