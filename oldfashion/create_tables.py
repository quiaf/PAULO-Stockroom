-- PUBLIC.DEVICE definition

-- Drop table

-- DROP TABLE PUBLIC.DEVICE;

CREATE TABLE PUBLIC.DEVICE (
	MODEL VARCHAR_IGNORECASE(255) NOT NULL,
	MANUFACTURER VARCHAR_IGNORECASE(255) NOT NULL,
	ATYPE VARCHAR_IGNORECASE(255) NOT NULL,
	ID_MODEL INTEGER NOT NULL AUTO_INCREMENT,
	CONSTRAINT DEVICE_PK PRIMARY KEY (ID_MODEL)
);
CREATE UNIQUE INDEX PRIMARY_KEY_7 ON PUBLIC.DEVICE (ID_MODEL);