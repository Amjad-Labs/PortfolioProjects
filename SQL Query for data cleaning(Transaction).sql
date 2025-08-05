--Cleaning Data in SQL Querys
----------------------------------
USE Storedb

--Creating a Cleaned Table
-----------------------------------------------------------------------------

CREATE TABLE Cleaned_Transaction(  --(Using this because Select into is blocked)
	Customer_ID INT,
	Name VARCHAR(100),
	Transaction_ID VARCHAR(20),
	Product VARCHAR(100),
	Purchase_Date VARCHAR(50), --(Because it's varchar in original table)
	Quantity INT,
	Price INT,
	Total INT,
	Status VARCHAR(50));

INSERT INTO Cleaned_Transaction
SELECT * FROM Transactions;

--Standardizeing Date Format
--------------------------------------

ALTER TABLE Cleaned_Transaction
ADD Formatted_Purchase_Date VARCHAR(50);

UPDATE Cleaned_Transaction
SET Formatted_Purchase_Date =
	CASE
		WHEN ISDATE(Purchase_Date) =1
		THEN FORMAT(CONVERT(Date,Purchase_Date),'dd/MM/yyyy')
			ELSE NULL
		END;

-- Fixing Status column
-----------------------------------

UPDATE Cleaned_Transaction
SET [Status] = CASE
	WHEN [Status] IS NULL THEN 
	'Unknown'
	WHEN LOWER([Status])  IN 
	('returned','return') THEN
	'Returned'
	WHEN LOWER([Status]) IN
	('processing','process') THEN
	'Processing'
	WHEN LOWER([Status]) IN 
	('delivered','deliverd') THEN
	'Delivered'
	WHEN LOWER([Status]) IN 
	('cancelled','canceled') THEN
	'Cancelled'
		ELSE [Status]
	END;

-- Fixing Product Name or "Capitalization"
--------------------------------------

UPDATE Cleaned_Transaction
SET [Product] = 
    CASE 
        WHEN CHARINDEX(' ', LTRIM([Product])) > 0 THEN
            CONCAT(
                UPPER(LEFT(LTRIM([Product]), 1)),
                LOWER(SUBSTRING(LTRIM([Product]), 2, CHARINDEX(' ', LTRIM([Product])) - 1)),
                ' ',
                UPPER(SUBSTRING(LTRIM([Product]), CHARINDEX(' ', LTRIM([Product])) + 1, 1)),
                LOWER(SUBSTRING(
                    LTRIM([Product]),
                    CHARINDEX(' ', LTRIM([Product])) + 2,
                    LEN(LTRIM([Product]))
                ))
            )
        ELSE
            UPPER(LEFT(LTRIM([Product]), 1)) + LOWER(SUBSTRING(LTRIM([Product]), 2, LEN([Product])))
    END
WHERE [Product] IS NOT NULL;


-- Calculate and Fix Missing Totals
-------------------------------------------
UPDATE Cleaned_Transaction
SET Total = Quantity * Price
WHERE Total IS NULL AND Quantity IS NOT NULL AND Price IS NOT NULL;

--Handling Missing Data
----------------------------------------

DELETE FROM Cleaned_Transaction
WHERE Product IS NULL
	OR Quantity IS NULL
	OR Price IS NULL 
	OR Total IS NULL 
	OR Formatted_Purchase_Date IS NULL
		-- I am removing all nulls without care because this table is for showing trends.

-- Removing Duplicates Rows
With RowCTE as (
	select * , ROW_NUMBER() OVER (
		PARTITION BY Customer_ID, Transaction_ID, Product, Purchase_date
		ORDER BY (SELECT NULL))
		AS rn
FROM Cleaned_Transaction
)
DELETE FROM RowCTE WHERE rn > 1;

--Final cleaned table
SELECT*
FROM Cleaned_Transaction