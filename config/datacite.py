import json



class DataciteInfo:

    def __init__(self):
        self.datacite = {"datacite": {}}

    # def set_contributors(self):
    #     pass

    def set_creators(self,affiliations,familyname,givenname):
        if self.datacite.keys():
            creators = []
            creators.append({"affiliations":affiliations,"familyname":familyname,
                             "givenname":givenname})
            self.datacite["datacite"].update({"creators":creators})
            return self.datacite


    def set_datacite_description(self,description):
        if self.datacite.keys():
            self.datacite["datacite"].update({"description": description})
            return self.datacite

    def set_identifier(self,identifier,identifierType):
        if self.datacite.keys():
            self.datacite["datacite"].update({"identifier": {"identifier":identifier,
                                                 "identifierType":identifierType}})
            return self.datacite

    def set_publicationYear(self,publicationYear):
        if self.datacite.keys():
            self.datacite["datacite"].update({"publicationYear": publicationYear})
            return self.datacite

    # def set_related_identifiers(self):
    #     pass

    # def set_rightsList(self):
    #     pass

    # def set_subjects(self):
    #     pass

    def set_titles(self,title):
        if self.datacite.keys():
            self.datacite["datacite"].update({"title": title})
            return self.datacite




