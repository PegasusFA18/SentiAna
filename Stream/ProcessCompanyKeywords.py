class Company:

    def __init__(self, name='', keywords=[], active=True):
        self.name = name
        self.keywords = keywords
        self.active = active





def import_text_file(filename):
    return open(filename, 'r').read()




def format_text_to_company_objects(text):
    companies = text.split('\n\n')
    company_list = []

    for company in companies:
        print(company)
        split_company = company.split(':')
        name = split_company[0]
        keyword_string = split_company[1]
        keywords = keyword_string.split(',')

        company_object = Company(name=name, keywords=keywords, active=True)
        company_list.append(company_object)

    return company_list




def find_company(company_name):
    list_of_companies = load_companies_from_file('keywords.txt')

    for company in list_of_companies:
        if company_name.lower() in company.name.lower():
            return company
        elif company.name.lower() in company_name.lower():
            return company

    return None




def load_companies_from_file(filename):
    text = import_text_file(filename)
    list_of_companies = format_text_to_company_objects(text)

    return list_of_companies




if __name__ == '__main__':
    list_of_companies = load_companies_from_file('keywords.txt')

    # for comp in list_of_companies:
    #     print(comp.keywords)
