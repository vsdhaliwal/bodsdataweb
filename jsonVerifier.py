import jsonschema
from jsonschema import validate

ownershipOrControlSchema = {
  "id": "ownership-or-control-statement.json",
  "$schema": "http://json-schema.org/draft-04/schema#",
  "version": "0.3",
  "title": "Ownership or control Statement",
  "description": "An ownership or control statement is made up of an entity, an interested party (a reference to an entity, natural person, arrangement or trust), details of the interest and provenance information for the statement.",
  "type": "object",
  "properties": {
    "statementID": {
    },
    "statementType": {
      "title": "Statement type",
      "description": "This MUST be 'ownershipOrControlStatement'.",
      "type": "string",
      "enum": [
        "ownershipOrControlStatement"
      ]
    },
    "statementDate": {
    },
    "isComponent": {
      "title": "Is component",
      "description": "Does this Ownership-or-control Statement represent a component of a wider indirect ownership-or-control relationship? Where `isComponent` is 'True': (1) the `statementID` of this secondary Ownership-or-control Statement MUST be an element in the `componentStatementIDs` array of that primary Ownership-or-control Statement, (2) this Ownership-or-control Statement MUST come before that primary Ownership-or-control Statement in a BODS package or stream, (3) the replacement of this Ownership-or-control Statement SHOULD be considered when replacing the primary Ownership-or-control Statement, and (4) the primary Ownership-or-control Statement MUST have a `isComponent` value of 'False'. Where `isComponent` is 'False', this Ownership-or-control Statement is the primary declaration of the relationship between the `subject` and the `interestedParty`.",
      "type": "boolean"
    },
    "componentStatementIDs": {
      "title": "Component statement IDs",
      "description": "The identifiers of all component statements that provide detail about the indirect relationship between this Statement's `subject` and `interestedParty`. If this Ownership-or-control Statement has components, it MUST itself have a `isComponent` value of 'False'.",
      "type": "array",
      "items": {
      }
    },
    "subject": {
      "title": "Subject",
      "description": "The subject of an ownership or control relationship.",
      "type": "object",
      "properties": {
        "describedByEntityStatement": {
          "title": "Described by entity statement",
          "description": "Provide the identifier of the statement which describes the entity that the subject of an ownership or control interest.",
          "type": "string"
        }
      },
      "required": [
        "describedByEntityStatement"
      ]
    },
    "interestedParty": {
    },
    "interests": {
      "title": "Interests",
      "description": "A description of the interests held by the interestedParty covered by this statement in the entity covered by this statement.",
      "type": "array",
      "items": {
      }
    },
    "publicationDetails": {
      "title": "Publication details",
      "description": "Information concerning the original publication of this statement.",
    },
    "source": {
      "title": "Source",
      "description": "The source of the information that links the entity and the interested party, or that supports a null statement.",
    },
    "annotations": {
      "title": "Annotations",
      "description": "Annotations about this statement or parts of this statement",
      "type": "array",
      "items": {
      }
    },
    "replacesStatements": {
    }
  },
  "required": [
    "statementID",
    "statementType",
    "isComponent",
    "subject",
    "interestedParty",
    "publicationDetails"
  ],
  "definitions": {
    "InterestedParty": {
      "title": "Interested party",
      "description": "The interested party has some level of ownership or control over the entity referenced in this ownership or control statement. This should be described with reference to either an entity statement or person statement, or, where the interested party is unknown, details of why.",
      "type": "object",
      "properties": {
        "describedByEntityStatement": {
          "title": "Described by entity statement",
          "description": "A reference to a statement describing a registered entity, trust or arrangement that has an ownership or control interest in the subject of this statement. An entityStatement should be used when the direct interests to be described represents known control or ownership by anyone other than a natural person.",
          "type": "string"
        },
        "describedByPersonStatement": {
          "title": "Described by person statement",
          "description": "A reference to a statement describing a natural person who has an ownership or control interest in the subject of this statement.",
          "type": "string"
        },
        "unspecified": {
          "title": "Unspecified or unknown ownership and control",
          "description": "When confirmation has been provided that no interested party exists, where ownership and control information does not need to be provided, or where details of ownership and control are unknown, a `reason` MUST be given. Where an unknown entity is the `subject` of further ownershipOrControlStatements in the same structure, or where there is a natural person with ownership or control but their name or details are not known or cannot be disclosed for some reason, `unspecified` should not be used, but instead a reference to a `personStatement` or `entityStatement` should be provided but identifying details MAY be left blank.",
          "type": "object",
          "properties": {
            "reason": {
              "title": "Reason",
              "description": "The reason that an interested party cannot be specified. From the unspecifiedReason codelist.",
              "type": "string",
              "enum": [
                "noBeneficialOwners",
                "subjectUnableToConfirmOrIdentifyBeneficialOwner",
                "interestedPartyHasNotProvidedInformation",
                "subjectExemptFromDisclosure",
                "interestedPartyExemptFromDisclosure",
                "unknown",
                "informationUnknownToPublisher"
              ],
              "codelist": "unspecifiedReason.csv",
              "openCodelist": False
            },
            "description": {
              "title": "Description",
              "description": "Any supporting information about the absence of a confirmed beneficial owner. This field may be used to provide set phrases from a source system, or for a free-text explanation.",
              "type": "string"
            }
          },
          "required": [
            "reason"
          ]
        }
      }
    }
  }
}

entityStatementSchema = {
  "id": "entity-statement.json",
  "$schema": "http://json-schema.org/draft-04/schema#",
  "version": "0.3",
  "title": "Entity statement",
  "description": "A statement identifying and describing the entity that is the subject of the ownership or control described in an ownership or control statement.",
  "type": "object",
  "properties": {
    "statementID": {
      "propertyOrder": 1
    },
    "statementType": {
      "title": "Statement type",
      "description": "This MUST be 'entityStatement'.",
      "type": "string",
      "enum": [
        "entityStatement"
      ],
      "propertyOrder": 2
    },
    "statementDate": {
      "propertyOrder": 3
    },
    "isComponent": {
      "title": "Is component",
      "description": "Does this Entity Statement represent a component of an indirect ownership-or-control relationship? Where `isComponent` is 'True': (1) the `statementID` of this Entity Statement MUST be an element in the `componentStatementIDs` array of that primary Ownership-or-control Statement, (2) this Entity Statement MUST come before that primary Ownership-or-control Statement in a BODS package or stream, (3) the replacement of this Entity Statement SHOULD be considered when replacing the primary Ownership-or-control Statement. The primary Ownership-or-control Statement MUST have a `isComponent` value of 'False'.",
      "type": "boolean"
    },
    "entityType": {
      "title": "Type",
      "description": "From the entityType codelist. What kind of entity is this? The 'registeredEntity' code covers any legal entity created through an act of official registration, usually resulting in an identifier being assigned to the entity. The ‘legalEntity’ code covers other bodies with distinct legal personality (international institutions, statutory corporations etc.). The 'arrangement' code covers artificial entities, described in the data model for the purpose of associating one or more natural or legal persons together in an ownership or control relationship, but without implying that the parties to this arrangement have any other form of collective legal identity.",
      "type": "string",
      "enum": [
        "registeredEntity",
        "legalEntity",
        "arrangement",
        "anonymousEntity",
        "unknownEntity",
        "state",
        "stateBody"
      ],
      "codelist": "entityType.csv",
      "openCodelist": False,
      "propertyOrder": 4
    },
    "unspecifiedEntityDetails": {
      "title": "Unspecified entity details",
      "description": "An explanation of why this entity has an `entityType` of 'anonymousEntity' or 'unknownEntity'. A `reason` MUST be specified.",
      "type": "object",
      "properties": {
        "reason": {
          "title": "Reason",
          "description": "The reason that an entity cannot be specified. From the unspecifiedReason codelist.",
          "type": "string",
          "enum": [
            "noBeneficialOwners",
            "subjectUnableToConfirmOrIdentifyBeneficialOwner",
            "interestedPartyHasNotProvidedInformation",
            "subjectExemptFromDisclosure",
            "interestedPartyExemptFromDisclosure",
            "unknown",
            "informationUnknownToPublisher"
          ],
          "codelist": "unspecifiedReason.csv",
          "openCodelist": False
        },
        "description": {
          "title": "Description",
          "description": "Any supporting information about the absence of a specific entity. This field may be used to provide set phrases from a source system, or for a free-text explanation.",
          "type": "string"
        }
      },
      "required": [
        "reason"
      ],
      "propertyOrder": 8
    },
    "name": {
      "title": "Entity name",
      "description": "The declared name of this entity.",
      "type": "string",
      "propertyOrder": 10
    },
    "alternateNames": {
      "title": "Alternative names",
      "description": "An array of other names this entity is known by.",
      "type": "array",
      "items": {
        "type": "string",
        "title": "Name",
        "description": "A name this entity is known by."
      },
      "propertyOrder": 12
    },
    "jurisdiction": {
      "title": "Jurisdiction",
      "description": "The jurisdiction in which this entity was registered (for legal and registered entities, and arrangements). Or the state's jurisdiction (for states and state bodies).",
      "propertyOrder": 15
    },
    "identifiers": {
      "title": "Identifiers",
      "description": "One or more official identifiers for this entity. Where available, official registration numbers should be provided.",
      "type": "array",
      "items": {
      },
      "propertyOrder": 20
    },
    "foundingDate": {
      "title": "Founding date",
      "description": "When was this entity founded, created or registered. Please provide as precise a date as possible in ISO 8601 format. When only the year or year and month is known, these can be given as YYYY or YYYY-MM.",
      "type": "string",
      "pattern": "^([\\+-]?\\d{4}(?!\\d{2}\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
      "propertyOrder": 30
    },
    "dissolutionDate": {
      "title": "Dissolution date",
      "description": "If this entity is no longer active, provide the date on which it was disolved or ceased. Please provide as precise a date as possible in ISO 8601 format. When only the year or year and month is known, these can be given as YYYY or YYYY-MM.",
      "type": "string",
      "pattern": "^([\\+-]?\\d{4}(?!\\d{2}\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
      "propertyOrder": 35
    },
    "addresses": {
      "title": "Addresses",
      "description": "One or more addresses for this entity.",
      "type": "array",
      "items": {
      },
      "propertyOrder": 40
    },
    "uri": {
      "title": "URI",
      "description": "Where a persistent URI (https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) is available for this entity this should be included.",
      "type": "string",
      "format": "uri",
      "propertyOrder": 21
    },
    "replacesStatements": {
      "$ref": "../components.json#/definitions/ReplacesStatements",
      "propertyOrder": 100
    },
    "publicationDetails": {
      "title": "Publication details",
      "description": "Information concerning the original publication of this statement.",
      "propertyOrder": 85
    },
    "source": {
      "title": "Source",
      "description": "The source of information about this entity, or of information that supports an anonymous or unknown entity statement.",
      "propertyOrder": 89
    },
    "annotations": {
      "title": "Annotations",
      "description": "Annotations about this statement or parts of this statement",
      "type": "array",
      "items": {
      },
      "propertyOrder": 90
    },
    "publicListing": {
      "title": "Public listing",
      "description": "Details of a publicly listed company, its securities (shares and other tradable financial instruments related to the entity), and related regulatory filings.",
    },
    "entitySubtype": {
      "type": "object",
      "title": "Subtype",
      "description": "Further information about the type of entity described in the statement.",
      "required": [
        "generalCategory"
      ],
      "properties": {
        "generalCategory": {
          "type": "string",
          "title": "General category",
          "description": "The general category into which the entity fits. The category classification MUST align with the `entityType` classification.",
          "codelist": "entitySubtypeCategory.csv",
          "enum": [
            "stateBody-governmentDepartment",
            "stateBody-stateAgency",
            "stateBody-other"
          ],
          "openCodelist": False
        },
        "localTerm": {
          "type": "string",
          "title": "Local term",
          "description": "The local term for the category of entity. For example, in Finland 'ministeriö' for a government department."
        }
      },
      "propertyOrder": 5
    },
    "formedByStatute": {
      "type": "object",
      "title": "Formed by statute",
      "description": "The law which mandated the formation of the entity described in the statement, where applicable. This information SHOULD be provided where a state has created an agency or other entity with specific legislation.",
      "properties": {
        "name": {
          "type": "string",
          "title": "Statute name",
          "description": "The name of the law."
        },
        "date": {
          "type": "string",
          "title": "Date",
          "description": "The date on which the law was passed. The date SHOULD be in the form YYYY-MM-DD. When only the year or year and month is known, these can be given as YYYY or YYYY-MM.",
          "pattern": "^([\\+-]?\\d{4}(?!\\d{2}\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$"
        }
      },
      "propertyOrder": 18
    }
  },
  "required": [
    "statementID",
    "statementType",
    "isComponent",
    "entityType",
    "publicationDetails"
  ]
}

personStatementSchema = {
  "id": "person-statement.json",
  "$schema": "http://json-schema.org/draft-04/schema#",
  "version": "0.3",
  "type": "object",
  "title": "Person statement",
  "description": "A person statement describes the information known about a natural person at a particular point in time, or from a given submission of information",
  "properties": {
    "statementID": {
      "propertyOrder": 1
    },
    "statementType": {
      "title": "Statement type",
      "description": "This MUST be 'personStatement'.",
      "type": "string",
      "enum": [
        "personStatement"
      ],
      "propertyOrder": 2
    },
    "statementDate": {
      "propertyOrder": 3
    },
    "isComponent": {
      "title": "Is component",
      "description": "Does this Person Statement represent a component of an indirect ownership-or-control relationship? Where `isComponent` is 'true': (1) the `statementID` of this Person Statement MUST be an element in the `componentStatementIDs` array of that primary Ownership-or-control Statement, (2) this Person Statement MUST come before that primary Ownership-or-control Statement in a BODS package or stream, (3) the replacement of this Person Statement SHOULD be considered when replacing the primary Ownership-or-control Statement. The primary Ownership-or-control Statement MUST have a `isComponent` value of 'False'.",
      "type": "boolean"
    },
    "personType": {
      "title": "Person type",
      "description": "Use the personType codelist. The ultimate beneficial owner of a legal entity is always a natural person. Where the beneficial owner has been identified, but information about them cannot be disclosed, use 'anonymousPerson'. Where the beneficial owner has not been clearly identified, use 'unknownPerson'. Where the beneficial owner has been identified use knownPerson. Where a person has the type 'anonymousPerson' or 'unknownPerson' a reason for the absence of information SHOULD be provided in 'unspecifiedPersonDetails')",
      "type": "string",
      "enum": [
        "anonymousPerson",
        "unknownPerson",
        "knownPerson"
      ],
      "propertyOrder": 4,
      "codelist": "personType.csv",
      "openCodelist": False
    },
    "unspecifiedPersonDetails": {
      "title": "Unspecified person details",
      "description": "An explanation of why this person has a `personType` of 'anonymousPerson' or 'unknownPerson'. A `reason` MUST be specified.",
      "type": "object",
      "properties": {
        "reason": {
          "title": "Reason",
          "description": "The reason that an interested party cannot be specified. From the unspecifiedReason codelist.",
          "type": "string",
          "enum": [
            "noBeneficialOwners",
            "subjectUnableToConfirmOrIdentifyBeneficialOwner",
            "interestedPartyHasNotProvidedInformation",
            "subjectExemptFromDisclosure",
            "interestedPartyExemptFromDisclosure",
            "unknown",
            "informationUnknownToPublisher"
          ],
          "codelist": "unspecifiedReason.csv",
          "openCodelist": False
        },
        "description": {
          "title": "Description",
          "description": "Any supporting information about the absence of a confirmed beneficial owner. This field may be used to provide set phrases from a source system, or for a free-text explanation.",
          "type": "string"
        }
      },
      "required": [
        "reason"
      ],
      "propertyOrder": 5
    },
    "names": {
      "title": "Names",
      "description": "One or more known names for this individual.",
      "type": "array",
      "items": {
      },
      "propertyOrder": 10
    },
    "identifiers": {
      "title": "Identifiers",
      "description": "One or more official identifiers for this perrson. Where available, official registration numbers should be provided.",
      "type": "array",
      "items": {
      },
      "propertyOrder": 20
    },
    "nationalities": {
      "title": "Nationality",
      "description": "An array of ISO 2-Digit country codes representing nationalities held by this individual.",
      "type": "array",
      "items": {
      },
      "propertyOrder": 30
    },
    "placeOfBirth": {
      "title": "Place of birth",
      "propertyOrder": 40
    },
    "birthDate": {
      "title": "Date of birth",
      "description": "The date of birth for this individual. Please provide as precise a date as possible in ISO 8601 format. When only the year or year and month is known, these can be given as YYYY or YYYY-MM.",
      "type": "string",
      "pattern": "^([\\+-]?\\d{4}(?!\\d{2}\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
      "propertyOrder": 35
    },
    "deathDate": {
      "title": "Death date",
      "description": "If this individual is no longer alive, provide their date of death. Please provide as precise a date as possible in ISO 8601 format. When only the year or year and month is known, these can be given as YYYY or YYYY-MM.",
      "type": "string",
      "pattern": "^([\\+-]?\\d{4}(?!\\d{2}\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
      "propertyOrder": 36
    },
    "placeOfResidence": {
      "title": "Place of residence",
      "propertyOrder": 50
    },
    "taxResidencies": {
      "title": "Tax residency",
      "description": "An array of ISO 2-Digit country codes representing the tax residencies held by this individual.",
      "type": "array",
      "items": {
      },
      "propertyOrder": 55
    },
    "addresses": {
      "title": "Addresses",
      "description": "One or more addresses for this entity.",
      "type": "array",
      "items": {
      },
      "propertyOrder": 60
    },
    "publicationDetails": {
      "title": "Publication details",
      "description": "Information concerning the original publication of this statement.",
      "propertyOrder": 85
    },
    "source": {
      "title": "Source",
      "description": "The source of information about this person, or of information that supports an unknown or anonymous person statement.",
      "propertyOrder": 89
    },
    "annotations": {
      "title": "Annotations",
      "description": "Annotations about this statement or parts of this statement",
      "type": "array",
      "items": {
      },
      "propertyOrder": 90
    },
    "replacesStatements": {
    },
    "politicalExposure": {
      "type": "object",
      "title": "Political exposure",
      "description": "Information about whether, and how, the person described by this statement is politically exposed. Use this property only if politically exposed person (PEP) declarations are expected as part of beneficial ownership declarations.",
      "required": [
        "status"
      ],
      "properties": {
        "status": {
          "type": "string",
          "title": "Politically exposed person (PEP) status",
          "description": "This value is 'isPep' or 'isNotPep' according to whether the person described by this statement has the status of politically exposed person (PEP). An 'unknown' value means a PEP status declaration is expected but missing; the reason for the missing data SHOULD be supplied in the details array.",
          "enum": [
            "isPep",
            "isNotPep",
            "unknown"
          ]
        },
        "details": {
          "type": "array",
          "title": "Politically exposed person (PEP) details",
          "description": "One or more descriptions of this person's Politically Exposed Person (PEP) status.",
          "items": {
          }
        }
      }
    }
  },
  "required": [
    "statementID",
    "statementType",
    "personType",
    "isComponent",
    "publicationDetails"
  ]
}



ownership_or_control_statement = {
    "statementID": "fbfd0547-d0c6-4a00-b559-5c5e91c34f5c",
    "statementType": "ownershipOrControlStatement",
    "isComponent": False,
    "statementDate": "2017-11-18",
    "subject": {
      "describedByEntityStatement": "1dc0e987-5c57-4a1c-b3ad-61353b66a9b7"
    },
    "interestedParty": {
      "describedByPersonStatement": "019a93f1-e470-42e9-957b-03559861b2e2"
    },
    "interests": [
      {
        "type": "shareholding",
        "directOrIndirect": "direct",
        "beneficialOwnershipOrControl": True,
        "startDate": "2016-04-06",
        "share": {
          "exact": 100,
          "minimum": 100,
          "maximum": 100
        }
      }
    ],
    "publicationDetails": {
      "publicationDate": "2018-02-13",
      "bodsVersion": "0.3",
      "publisher": {
        "name": "CHRINON LTD"
      }
    }
  }

entity_statement = {
    "statementID": "1dc0e987-5c57-4a1c-b3ad-61353b66a9b7",
    "statementType": "entityStatement",
    "isComponent": False,
    "statementDate": "2017-11-18",
    "entityType": "registeredEntity",
    "name": "CHRINON LTD",
    "foundingDate": "2010-11-18",
    "identifiers": [
      {
        "scheme": "GB-COH",
        "id": "07444723"
      }
    ],
    "publicationDetails": {
      "publicationDate": "2018-02-13",
      "bodsVersion": "0.3",
      "publisher": {
        "name": "CHRINON LTD"
      }
    }
  }

person_statement = {
    "statementID": "019a93f1-e470-42e9-957b-03559861b2e2",
    "statementType": "personStatement",
    "isComponent": False,
    "statementDate": "2017-11-18",
    "personType": "knownPerson",
    "nationalities": [
      {
        "code": "GB",
        "name": "United Kingdom of Great Britain and Northern Ireland (the)"
      }
    ],
    "names": [
      {
        "type": "individual",
        "fullName": "Christopher Taggart",
        "givenName": "Christopher",
        "familyName": "Taggart"
      },
      {
        "type": "alternative",
        "fullName": "Chris Taggart"
      }
    ],
    "birthDate": "1964-04",
    "addresses": [
      {
        "type": "service",
        "address": "Aston House, Cornwall Avenue, London",
        "country": "GB",
        "postCode": "N3 1LF"
      }
    ],
    "publicationDetails": {
      "publicationDate": "2018-02-13",
      "bodsVersion": "0.3",
      "publisher": {
        "name": "CHRINON LTD"
      }
    }
  }

try:
    validate(ownership_or_control_statement, ownershipOrControlSchema)
    print("Validation successful! The data conforms to the schema.")
    validate(entity_statement, entityStatementSchema)
    print("Validation successful! The data conforms to the schema.")
    validate(person_statement, personStatementSchema)
    print("Validation successful! The data conforms to the schema.")
except jsonschema.exceptions.ValidationError as e:
    print(f"Validation failed. Error: {e.message}")
