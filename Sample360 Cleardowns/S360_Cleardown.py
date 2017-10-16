import pypyodbc
import os

cnxn = pypyodbc.connect(driver='{SQL Server}', server='localhost', database='Sample360', uid='sa', pwd='imperial')

cur = cnxn.cursor()
cur.execute("TRUNCATE TABLE [sample360].[dbo].[OrderStatusLog];")
cur.execute("TRUNCATE TABLE [sample360].[dbo].[OrderSample];")
cur.execute("DELETE FROM [sample360].[dbo].[_Order];")
cur.execute("DELETE FROM [sample360].[dbo].[Patient];")
cur.execute("TRUNCATE TABLE [sample360].[dbo].[MessageLog];")
cur.execute("TRUNCATE TABLE [sample360].[dbo].[OrderMessage];")
cur.execute("TRUNCATE TABLE [sample360].[dbo].[ResultStatusLog];")
cur.execute("TRUNCATE TABLE [sample360].[dbo].[SampleStatusLog];")
cur.execute("TRUNCATE TABLE [sample360].[dbo].[OrderAnswer];")
cur.execute("TRUNCATE TABLE [sample360_ordercomms].[dbo].[ChannelRaw];")
cur.execute("DELETE FROM [sample360].[dbo].[Alert];")
# cur.excecute("TRUNCATE TABLE [sample360].[dbo].[Alert];")
cur.execute("DELETE FROM [sample360].[dbo].[Roleuser];")
cur.execute("DELETE FROM [sample360].[dbo].[Token];")
cur.execute("DELETE FROM [sample360].[dbo].[_user];")
cur.execute("SET IDENTITY_INSERT [dbo].[_User] ON INSERT [dbo].[_User] ([UserId], [Username], [Password], [Email], "
            "[CreatedBy], [CreatedDate], [AccountStatus], [PasswordLastChangedDate], [LastModified], [Surname], "
            "[Forename], [JobTitleId], [DepartmentId], [AssignmentNumber]) VALUES (CAST(1 AS Numeric(11, 0)), "
            "N'superuser', N'superuser', NULL, NULL, NULL, N'live', NULL, NULL, N'superuser', N'superuser', "
            "CAST(1 AS Numeric(11, 0)), CAST(1 AS Numeric(11, 0)), NULL) SET IDENTITY_INSERT [dbo].[_User] OFF INSERT "
            "[dbo].[RoleUser] ([RoleId], [UserId]) VALUES (CAST(1 AS Numeric(11, 0)), CAST(1 AS Numeric(11, 0)))")
cur.execute("DBCC CHECKIDENT ('[sample360_ordercomms].[dbo].[ChannelRaw]', RESEED, 0);")
cur.execute("DBCC CHECKIDENT ('[Sample360].[dbo].[OrderStatusLog]', RESEED, 0);")
cur.execute("DBCC CHECKIDENT ('[Sample360].[dbo].[_Order]', RESEED, 0);")
cur.execute("DBCC CHECKIDENT ('[Sample360].[dbo].[Patient]', RESEED, 0);")
cur.execute("DBCC CHECKIDENT ('[Sample360].[dbo].[Alert]', RESEED, 0);")
cur.execute("DBCC CHECKIDENT ('[Sample360].[dbo].[OrderSample]', RESEED, 0);")
cur.commit()
cur.close()
cnxn.close()

print("Cleardown Completed.")
neword = input("Would you like to populate with new orders? Y/N: ")
if neword.startswith('y' or 'Y'):
    os.system("start C:\\Users\\lbroley\\PycharmProjects\\HL7_Message_Creation\\topten.bat")

os.close()
#if neword.startswith('y' or 'Y'):
#    os.system("start C:\\sample360\\HL7_Message_Creation\\topten.bat")
