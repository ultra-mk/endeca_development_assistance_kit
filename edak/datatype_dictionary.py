ORACLE_COLUMNS_TO_ENDECA = {'FULFILLMENT_DATE':'mdex:dateTime', 'GL_DATE' : 'mdex:dateTime',
				'SHIP_QUANTITY': 'mdex:int', 'UNIT_PRICE':'mdex:double'}

ENDECA_TO_XML = {'mdex:double': 'number', 'mdex:string': 'string', 'mdex:boolean': 'boolean',
                            'mdex:dateTime': 'date', 'mdex:int': 'integer',
                            'mdex:long': 'long'}