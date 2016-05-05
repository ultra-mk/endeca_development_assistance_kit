# Endeca Development Assistance Kit

I develop Oracle Endeca apps for my day job. A typical project requires building an ETL job, configuring an Endeca Data Domain, defining views in the Endeca application and creating custom attributes. I need the same data fields in a variety of file types and formats.

# Example

Consider the following. A customer wants an Endeca application that shows them PO Number, all the lines on a PO, the item number and the item description.

A SQL query to build this would look as follows.

	SELECT PHA.PO_HEADER_ID,
	PLA.LINE_NUM, PLA.ITEM_ID, PLA.ITEM_DESCRIPTION
	FROM APPS.PO_HEADERS_ALL PHA
	INNER JOIN APPS.PO_LINES_ALL PLA
	ON PHA.PO_HEADER_ID = PLA.PO_HEADER_ID;


Pretty simple right?

Depending on the requirements of the project, I might need define a view in Endeca using these fields. That would look like this in Endeca Query Language (EQL).

	DEFINE Purchase_Order_View as SELECT
	PO_HEADER_ID AS "PO_HEADER_ID",
	PO_LINE_NUM AS "PO_LINE_NUM",
	ITEM_DESCRIPTION AS "ITEM_DESCRIPTION"

OK. Not that tricky. But now you've got the same stuff in two places. And what happens if you write `PO_NUMBER` rather than `PO_HEADER_ID`? The view will break and you have to backtrack to the ETL job to find the name of the data element. Maybe not a big deal, but suppose you have 70-80 data elements.....

Sometimes I have to define custom display names in the database itself. That means I need to write the following PLSQL (keep in mind this is for a single custom attribute.) In this example, I want 'PO_HEADER_ID' to be rendered simply as 'Purchase Order'.

This command creates the custom attribute.

	SET DEFINE OFF;
	REM INSERTING into APPS.FND_EID_PDR_ATTRS_B
	Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE,
	EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG,
	DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG,
	MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,
	CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,
	ATTR_VALUE_SET_FLAG,VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)
	values ( 204,'purchase_header_id','mdex:string',1,'2.3', 'MSI', 'N','N','N','N','N','N','N',0,0, 
	SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);
	COMMIT;

This command (partially) sets the display name. This command is repeated for every language that Oracle supports.

	SET DEFINE OFF;
	REM INSERTING into APPS.FND_EID_PDR_ATTRS_TL
	Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN)
	values ( 204,'purchase_header_id','D','US','Purchase Order ','Purchase Order ','Purchase Order ','Purchase Order ',0,SYSDATE,0,SYSDATE,0);
	COMMIT;


The bottom line here is that the same data gets used a bunch of different ways, and if PO_HEADER_ID is written as PO_ID in a single place, everything will be horrible forever and ever. This toolset was created to save me hours of needless frustration. All you need to do is fill out a spreadsheet with the attributes you need and the display names, and you can get all the EQL and PLSQL that you need. Feed those files where they need to go, and presto! you've got views, and custom attributes and display names.
