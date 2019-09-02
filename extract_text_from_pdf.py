def extract_values(text):
	"""Extracts client's name, personal ID, nationality, Region code, 
	number of products and transaction volume YTD (in EUR)"""
	
	values = {}
	
	#Extracts name from text.
	first_pos = str.find(text, "Name:")
	second_pos = str.find(text, "Date of birth:")
		
	name_1 = text[first_pos : second_pos]
	name_2 = name_1.replace("Name:", "")
	pure_name = name_2.strip()
		
	values["Name"] = pure_name
		
	#Extracts Date of birth from text.
	first_pos = str.find(text, "Date of birth:")
	second_pos = str.find(text, "Nationality:")
		
	date_of_birth_1 = text[first_pos : second_pos]
	date_of_birth_2 = date_of_birth_1.replace("Date of birth:", "")
	pure_date_of_birth = date_of_birth_2.strip()
		
	values["Date of birth"] = pure_date_of_birth
		
	#Extracts nationality from text.
	first_pos = str.find(text, "Nationality:")
	second_pos = str.find(text, "Region:")
		
	nationality_1 = text[first_pos : second_pos]
	nationality_2 = nationality_1.replace("Nationality:", "")
	pure_nationality = nationality_2.strip()
		
	values["Nationality"] = pure_nationality
		
	#Extracts Region code from text.
	first_pos = str.find(text, "Region code:")
	second_pos = str.find(text, "Engagement details:")
		
	region_code_1 = text[first_pos : second_pos]
	region_code_2 = region_code_1.replace("Region code:", "")
	pure_region_code = region_code_2.strip()
		
	values["Region code"] = pure_region_code
		
	#Extracts Client number from text.
	first_pos = str.find(text, "Client no:")
	second_pos = str.find(text, "Corporate account:")
		
	client_number_1 = text[first_pos : second_pos]
	client_number_2 = client_number_1.replace("Client no:", "")
	pure_client_number = client_number_2.strip()
		
	values["Client number"] = pure_client_number
		
	#Extracts Transaction volume YTD from text.
	first_pos = str.find(text, "Transaction volume YTD:")
	second_pos = len(text)
		
	transaction_volume_1 = text[first_pos : second_pos]
	transaction_volume_2 = transaction_volume_1.replace("Transaction volume YTD:", "")
	pure_transaction_volume = transaction_volume_2.strip()
		
	values["Transaction volume YTD"] = pure_transaction_volume
	
	#Extracts Corporate account from text.
	first_pos = str.find(text, "Corporate account:")
	second_pos = str.find(text, "Products:")
		
	corporate_account_1 = text[first_pos : second_pos]
	corporate_account_2 = corporate_account_1.replace("Corporate account:", "")
	pure_corporate_account = corporate_account_2.strip()
		
	values["Corporate account"] = pure_corporate_account
		
	# Count amount of products
	first_pos = str.find(text, "Products:")
	second_pos = str.find(text, "Transaction volume YTD:")
		
	products_1 = text[first_pos : second_pos]
	products_2 = products_1.replace("Products:", "")
	pure_products = products_2.strip()
			
	number_of_products = 0
		
	if pure_products == "":
		number_of_products = 0
			
	elif pure_products != "":
		number_of_products = 1
			
	if str.find(pure_products, ", ") > 0:
		for letter in pure_name:
			if letter == ",":
				number_of_products += 1
		
	values["Number of products"] = number_of_products
	
	return values
