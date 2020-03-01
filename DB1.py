import win32com.client.connect
ado_conn = win32com.client.gencache.EnsureDispatch('ADODB.Connection')
ado_conn.ConnectionString = "Provider = Microsoft.ACE.OLEDB.12.0; Data Source = C:\\Users\amruth\Desktop\Hemraj\Read.xlsx; Extended Properties ='Excel 12.0 Xml;HDR=YES'";

ado_conn.Open()

# Now create a RecordSet object and open a table
oRS = win32com.client.gencache.EnsureDispatch('ADODB.Recordset')
oRS.ActiveConnection = ado_conn    # Set the recordset to connect thru oConn

oRS.Open("SELECT * FROM sheet1")