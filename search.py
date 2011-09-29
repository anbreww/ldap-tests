#!/usr/bin/env python
import ldap

sciper = "170951" # me!

# demo script to search for user details
try:
    l = ldap.open("ldap.epfl.ch")
    l.protocol_version = ldap.VERSION3
except ldap.LDAPError, e:
    print e

dn = "o=epfl,c=ch"
scope = ldap.SCOPE_SUBTREE

# retrieve everything. We should refine this
retrieveAttributes = None
searchFilter = "uniqueIdentifier=%s" % sciper

try:
    ldap_result_id = l.search(dn, scope, searchFilter, retrieveAttributes)
    result_set = []
    while 1:
        result_type, result_data = l.result(ldap_result_id, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    print result_set[0][0][1]['displayName']
except ldap.LDAPError, e:
    print e




