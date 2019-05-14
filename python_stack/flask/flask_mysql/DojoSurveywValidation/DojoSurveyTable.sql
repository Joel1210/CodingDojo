CREATE TABLE [dbo].[DojoSurveyTable]
(
	[Id] INT NOT NULL PRIMARY KEY, 
    [name] CHAR(255) NULL, 
    [dojoloc] CHAR(255) NULL, 
    [lang] CHAR(255) NULL, 
    [comment] NCHAR(10) NULL, 
    [created] TIMESTAMP NOT NULL DEFAULT update_now(), 
    [updated] TIMESTAMP NOT NULL DEFAULT update_now()
)
