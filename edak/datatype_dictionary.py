ORACLE_COLUMNS_TO_ENDECA = {'FULFILLMENT_DATE':'mdex:dateTime', 'GL_DATE' : 'mdex:dateTime',
				'SHIP_QUANTITY': 'mdex:int', 'UNIT_PRICE':'mdex:double', 'ORDERED_QUANTITY':'mdex:int',
				 'PROMISE_DATE': 'mdex:dateTime', 'SCHEDULE_SHIP_DATE' :'mdex:dateTime', 'REQUEST_DATE':'mdex:dateTime',
				 'SHIPPED_QUANTITY' : 'mdex:int', 'ACTUAL_SHIPMENT_DATE':'mdex:dateTime',
				 'ACTUAL_ARRIVAL_DATE' : 'mdex:dateTime', 'ULTIMATE_DROPOFF_DATE': 'mdex:dateTime', 'PROMISED_DATE':'mdex:dateTime',
				 'LEAD_TIME':'mdex:int', 'POSTPROCESSING_LEAD_TIME' : 'mdex:int', 'FULL_LEAD_TIME' : 'mdex:int', 
				 'PREPROCESSING_LEAD_TIME' : 'mdex:int', 'DELIVERY_LEAD_TIME':'mdex:int', 'SCHEDULE_ARRIVAL_DATE' : 'mdex:dateTime',
				 'TOTAL_UNSHIPPED_QTY' : 'mdex:int', 'CONVERSION_RATE' : 'mdex:double', 'BOOKED_DATE' : 'mdex:dateTime',
				 'OFFER_START_DATE' :'mdex:dateTime', 'OFFER_END_DATE': 'mdex:dateTime', 'ULTILIZED_AMOUNT' : 'mdex:double',
				 'COMMITTED_AMOUNT' : 'mdex:double','EARNED_AMOUNT' : 'mdex:double', 'UOM_CONVERSION_FACTOR' : 'mdex:double',
				 'INPUT_COST_FUNCTIONAL' : 'mdex:double', 'ITEM_COST' : 'mdex:double', 'CURRENCY_CONVERSION':'mdex:double',
				 'INPUT_COST_USD' :'mdex:double', 'TOTAL_COST_USD':'mdex:double', 'INPUT_COST_USD_PER_EA' : 'mdex:double',
				 'GLOBAL_COST_USD':'mdex:double', 'GLOBAL_COST_USD_PER_EA':'mdex:double', 'FINAL_COST_FUNCTIONAL':'mdex:double',
				 'FINAL_COST_USD': 'mdex:double', 'FINAL_COST_USD_PER_EA': 'mdex:double'}

ENDECA_TO_XML = {'mdex:double': 'number', 'mdex:string': 'string', 'mdex:boolean': 'boolean',
                            'mdex:dateTime': 'date', 'mdex:int': 'integer',
                            'mdex:long': 'long'}