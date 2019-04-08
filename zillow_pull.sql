USE zillow;

SELECT *
FROM properties_2016 p
LEFT OUTER JOIN airconditioningtype act ON act.airconditioningtypeid = p.airconditioningtypeid
LEFT OUTER JOIN architecturalstyletype ast ON ast.architecturalstyletypeid = p.architecturalstyletypeid
LEFT OUTER JOIN buildingclasstype bct ON bct.buildingclasstypeid = p.buildingclasstypeid
LEFT OUTER JOIN heatingorsystemtype hst ON hst.heatingorsystemtypeid = p.heatingorsystemtypeid
LEFT OUTER JOIN propertylandusetype plu ON plu.propertylandusetypeid = p.propertylandusetypeid
LEFT OUTER JOIN storytype st ON st.storytypeid = p.storytypeid
LEFT OUTER JOIN typeconstructiontype tct ON tct.typeconstructiontypeid = p.typeconstructiontypeid
LEFT OUTER JOIN unique_properties up ON up.parcelid = p.parcelid
LIMIT 500;