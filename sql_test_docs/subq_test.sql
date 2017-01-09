SELECT
PEIA.EXPENDITURE_ITEM_ID AS PA_TRANS_ID,
(
  SELECT DISTINCT
  PERIOD_NAME
  FROM 
  APPS.PA_PERIODS_ALL
  WHERE PCDLA.GL_DATE BETWEEN START_DATE AND END_DATE
) AS PA_GL_PERIOD,
CASE PCDLA.TRANSFER_STATUS_CODE
  WHEN 'A' THEN 'Accepted'
  WHEN 'R' THEN 'Rejected'
  WHEN 'P' THEN 'Pending'
  WHEN 'T' THEN 'Transferred'
  WHEN 'X' THEN 'Rejected In Transfer'
  WHEN 'V' THEN 'Received'
  ELSE 'N/A'
END AS DISTRIBUTION_LINE_STATUS,
(MFB.UNIT_SELLING_PRICE * MFB.QUANTITY * 1.005) AS TOTAL_FCST_EQP_COST_PROJ_CURR,
(SELECT DISTINCT PAPF.FULL_NAME FROM APPS.PER_ALL_PEOPLE_F PAPF, APPS.PA_PROJECT_PLAYERS PPP WHERE PAPF.PERSON_ID = PPP.PERSON_ID AND PPP.PROJECT_ROLE_TYPE = 'PROJECT MANAGER' AND PPP.END_DATE_ACTIVE IS NULL AND PPA.PROJECT_ID = PPP.PROJECT_ID) AS PROJECT_MANAGER


FROM 
APPS.PA_EXPENDITURE_ITEMS_ALL PEIA,
APPS.PA_PROJECTS_ALL PPA,
APPS.PA_TASKS PT,
APPS.PA_TRANSACTION_SOURCES PTS,
APPS.PA_EXPENDITURE_COMMENTS PEC,
APPS.PA_DRAFT_INVOICE_DETAILS_ALL PDIDA,
APPS.PA_DRAFT_INVOICES_ALL PDIA,
APPS.PA_DRAFT_INVOICE_ITEMS PDI,
APPS.AP_INVOICES_ALL AIA,
APPS.GL_CODE_COMBINATIONS GCC,
APPS.HR_ALL_ORGANIZATION_UNITS HAOU,
APPS.HR_ALL_ORGANIZATION_UNITS CC_PRVDR_ORGANIZATION,
APPS.HR_ALL_ORGANIZATION_UNITS CC_RECVR_ORGANIZATION,
APPS.PER_JOBS PJ,
APPS.PA_COST_DISTRIBUTION_LINES_ALL PCDLA,
APPS.PA_PROJECT_CUSTOMERS PPC,
APPS.RA_CUSTOMERS RC,
APPS.AP_INVOICE_DISTRIBUTIONS_ALL AIDA,
APPS.AP_INVOICE_LINES_ALL AILA,

APPS.XLA_AE_HEADERS xah,
APPS.XLA_EVENTS XAE,
APPS.XLA_AE_LINES XAL,
APPS.GL_JE_LINES GLJE,
APPS.GL_LEDGERS GL,
APPS.GL_CODE_COMBINATIONS AP_EXPENSE,
APPS.PA_LOOKUPS PL,
APPS.PA_EXPENDITURES_ALL PEA,
APPS.PER_ALL_PEOPLE_F PAPF,
APPS.PO_VENDORS PV,
APPS.PA_EXPENDITURE_TYPES PET

WHERE 1=1
AND PEIA.PROJECT_ID = PPA.PROJECT_ID(+)
AND PCDLA.SYSTEM_REFERENCE2 = TO_CHAR(AIA.INVOICE_ID(+))
AND PEIA.TASK_ID = PT.TASK_ID(+)
AND PEIA.TRANSACTION_SOURCE = PTS.TRANSACTION_SOURCE(+)
AND PEIA.EXPENDITURE_ITEM_ID = PEC.EXPENDITURE_ITEM_ID(+)
AND PEIA.EXPENDITURE_ITEM_ID = PDIDA.EXPENDITURE_ITEM_ID(+)



AND PDIDA.PROJECT_ID = PDI.PROJECT_ID
AND PDIDA.DRAFT_INVOICE_NUM = PDI.DRAFT_INVOICE_NUM
AND PDIDA.LINE_NUM = PDI.LINE_NUM
AND PDI.DRAFT_INVOICE_NUM = PDIA.DRAFT_INVOICE_NUM
AND PDI.PROJECT_ID = PDIA.PROJECT_ID


AND PDIDA.REV_CODE_COMBINATION_ID = GCC.CODE_COMBINATION_ID(+)
AND PEIA.CC_PRVDR_ORGANIZATION_ID  = HAOU.ORGANIZATION_ID(+)
AND PEIA.JOB_ID = PJ.JOB_ID(+)
AND PEIA.EXPENDITURE_ITEM_ID = PCDLA.EXPENDITURE_ITEM_ID(+)
AND PEIA.PROJECT_ID = PPC.PROJECT_ID(+)
AND PPC.CUSTOMER_ID = RC.CUSTOMER_ID(+)
AND AIA.INVOICE_ID = AILA.INVOICE_ID(+)
AND AILA.INVOICE_ID = AIDA.INVOICE_ID(+)
AND AILA.LINE_NUMBER = AIDA.INVOICE_LINE_NUMBER(+)

AND PCDLA.ACCT_EVENT_ID = XAE.EVENT_ID(+)
AND XAE.EVENT_ID = XAH.EVENT_ID(+)
AND XAH.AE_HEADER_ID = XAL.AE_HEADER_ID(+)
AND XAL.GL_SL_LINK_ID = GLJE.GL_SL_LINK_ID(+)
AND XAH.LEDGER_ID = GL.LEDGER_ID(+)
AND PEIA.ORG_ID = CC_PRVDR_ORGANIZATION.ORGANIZATION_ID(+)
AND PEIA.CC_RECVR_ORGANIZATION_ID = CC_RECVR_ORGANIZATION.ORGANIZATION_ID(+)
AND AIA.ACCTS_PAY_CODE_COMBINATION_ID = AP_EXPENSE.CODE_COMBINATION_ID(+)
AND AIDA.PA_ADDITION_FLAG = PL.LOOKUP_CODE(+)
AND PEIA.EXPENDITURE_ID = PEA.EXPENDITURE_ID
AND PEA.INCURRED_BY_PERSON_ID = PAPF.PERSON_ID(+)
AND PEA.VENDOR_ID = PV.VENDOR_ID(+)
AND PEIA.EXPENDITURE_TYPE = PET.EXPENDITURE_TYPE(+)

--



--AND PEIA.EXPENDITURE_TYPE LIKE 'LABOR PM'
--
--AND ROWNUM <= 10

AND PDIA.RA_INVOICE_NUMBER = 1120006084
--AND PEIA.EXPENDITURE_ITEM_ID = 466639


