-- MySQL Script generated by MySQL Workbench
-- Wed 10 May 2017 10:06:12 PM PKT
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `PortfolioType`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PortfolioType` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `PortfolioType` (
  `portfolioTypeid` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`portfolioTypeid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `PortfolioStatus`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PortfolioStatus` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `PortfolioStatus` (
  `portfoliostatusid` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  PRIMARY KEY (`portfoliostatusid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Team`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Team` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Team` (
  `teamid` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`teamid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `ResourceType`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ResourceType` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `ResourceType` (
  `resourceTypeid` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(100) NULL,
  PRIMARY KEY (`resourceTypeid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Resource`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Resource` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Resource` (
  `resourceid` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `active` TINYINT NOT NULL DEFAULT 1,
  `teamid` INT NOT NULL,
  `resourceTypeid` INT NOT NULL,
  PRIMARY KEY (`resourceid`),
  CONSTRAINT `fk_Resource_Team1`
    FOREIGN KEY (`teamid`)
    REFERENCES `Team` (`teamid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Resource_ResourceType1`
    FOREIGN KEY (`resourceTypeid`)
    REFERENCES `ResourceType` (`resourceTypeid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Portfolio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Portfolio` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Portfolio` (
  `portfolioid` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL COMMENT '	',
  `portfolioTypeid` INT NOT NULL,
  `details` TEXT NULL,
  `rank` BIGINT NOT NULL DEFAULT 1,
  `portfoliostatusid` INT NOT NULL,
  `owner` INT NOT NULL,
  PRIMARY KEY (`portfolioid`, `owner`),
  CONSTRAINT `fk_portfolios_portfolioType`
    FOREIGN KEY (`portfolioTypeid`)
    REFERENCES `PortfolioType` (`portfolioTypeid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Portfolio_PortfolioStatus1`
    FOREIGN KEY (`portfoliostatusid`)
    REFERENCES `PortfolioStatus` (`portfoliostatusid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Portfolio_Resource1`
    FOREIGN KEY (`owner`)
    REFERENCES `Resource` (`resourceid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Sprint`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sprint` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Sprint` (
  `sprintid` INT NOT NULL AUTO_INCREMENT,
  `details` VARCHAR(100) NULL,
  `startDate` DATE NULL,
  `End` DATE NULL,
  PRIMARY KEY (`sprintid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `portfolioReleases`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `portfolioReleases` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `portfolioReleases` (
  `portfolioid` INT NOT NULL,
  `releaseId` INT NOT NULL AUTO_INCREMENT,
  `planStartDate` DATE NULL,
  `actualStartDate` DATE NULL,
  `teamid` INT NOT NULL,
  `planEndDate` DATE NULL,
  `actualEndDate` DATE NULL,
  `details` VARCHAR(100) NULL DEFAULT ' ',
  PRIMARY KEY (`releaseId`),
  CONSTRAINT `fk_portfoliReleases_Team1`
    FOREIGN KEY (`teamid`)
    REFERENCES `Team` (`teamid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `UserStory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `UserStory` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `UserStory` (
  `userStoryid` INT NOT NULL AUTO_INCREMENT,
  `details` VARCHAR(100) NULL,
  `resourceid` INT NOT NULL,
  `resourceid1` INT NOT NULL,
  `sprintid` INT NOT NULL,
  `releaseId` INT NOT NULL,
  PRIMARY KEY (`userStoryid`),
  CONSTRAINT `fk_UserStory_Resource1`
    FOREIGN KEY (`resourceid1`)
    REFERENCES `Resource` (`resourceid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UserStory_Sprint1`
    FOREIGN KEY (`sprintid`)
    REFERENCES `Sprint` (`sprintid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UserStory_portfolioReleases1`
    FOREIGN KEY (`releaseId`)
    REFERENCES `portfolioReleases` (`releaseId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `TaskStatus`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TaskStatus` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `TaskStatus` (
  `taskStatusid` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  PRIMARY KEY (`taskStatusid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `ProgressRatio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProgressRatio` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `ProgressRatio` (
  `progressRatioid` INT NOT NULL AUTO_INCREMENT,
  `descriptions` VARCHAR(100) NULL,
  PRIMARY KEY (`progressRatioid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Task`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Task` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Task` (
  `taskid` BIGINT NOT NULL AUTO_INCREMENT,
  `userStoryid` INT NULL,
  `estmatedStart` DATE NULL,
  `estimatedDuration` INT NULL,
  `actualStart` DATE NULL,
  `actualDuration` INT NULL,
  `taskStatusid` INT NULL,
  `progressRatioid` INT NOT NULL DEFAULT 0,
  `nextTaskId` BIGINT NULL,
  `previousTaskId` BIGINT NULL,
  `resourceid` INT NOT NULL,
  PRIMARY KEY (`taskid`),
  CONSTRAINT `fk_Task_UserStory1`
    FOREIGN KEY (`userStoryid`)
    REFERENCES `UserStory` (`userStoryid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Task_TaskStatus1`
    FOREIGN KEY (`taskStatusid`)
    REFERENCES `TaskStatus` (`taskStatusid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Task_ProgressRatio1`
    FOREIGN KEY (`progressRatioid`)
    REFERENCES `ProgressRatio` (`progressRatioid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Task_Resource1`
    FOREIGN KEY (`resourceid`)
    REFERENCES `Resource` (`resourceid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `WorkLog`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `WorkLog` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `WorkLog` (
  `workLogid` INT NOT NULL AUTO_INCREMENT,
  `startTime` VARCHAR(100) NULL,
  `endTime` VARCHAR(100) NULL,
  `Duration` VARCHAR(100) NULL,
  `taskid` BIGINT NOT NULL,
  PRIMARY KEY (`workLogid`),
  CONSTRAINT `fk_WorkLog_Task1`
    FOREIGN KEY (`taskid`)
    REFERENCES `Task` (`taskid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `TaskLinksLabel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `TaskLinksLabel` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `TaskLinksLabel` (
  `taskLinksLabelid` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(100) NULL,
  PRIMARY KEY (`taskLinksLabelid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `externalLInks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `externalLInks` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `externalLInks` (
  `externalLInksid` INT NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(100) NULL,
  `taskid` BIGINT NOT NULL,
  `linksLabelid` INT NOT NULL,
  PRIMARY KEY (`externalLInksid`),
  CONSTRAINT `fk_externalLInks_Task1`
    FOREIGN KEY (`taskid`)
    REFERENCES `Task` (`taskid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_externalLInks_LinksLabel1`
    FOREIGN KEY (`linksLabelid`)
    REFERENCES `TaskLinksLabel` (`taskLinksLabelid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `PortFoliLables`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PortFoliLables` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `PortFoliLables` (
  `portFoliLablesid` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(100) NULL,
  `portfolioid` INT NOT NULL,
  PRIMARY KEY (`portFoliLablesid`),
  CONSTRAINT `fk_PortFoliLables_Portfolio1`
    FOREIGN KEY (`portfolioid`)
    REFERENCES `Portfolio` (`portfolioid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `Dictionary`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Dictionary` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `Dictionary` (
  `Key` VARCHAR(100) NOT NULL,
  `shortTitle` VARCHAR(100) NULL,
  `LongTitle` VARCHAR(100) NULL,
  `ContextHelp` VARCHAR(100) NULL,
  PRIMARY KEY (`Key`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `PortFoliLinksLabel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PortFoliLinksLabel` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `PortFoliLinksLabel` (
  `portFoliLinksLabelid` INT NOT NULL AUTO_INCREMENT,
  `label` VARCHAR(100) NULL,
  `Url` VARCHAR(100) NULL,
  PRIMARY KEY (`portFoliLinksLabelid`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `PortfolioLInks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `PortfolioLInks` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `PortfolioLInks` (
  `portFoliLinksid` INT NOT NULL AUTO_INCREMENT,
  `portfolioid` INT NOT NULL,
  `portFoliLinksLabelid` INT NOT NULL,
  PRIMARY KEY (`portFoliLinksid`),
  CONSTRAINT `fk_PortfolioLInks_Portfolio1`
    FOREIGN KEY (`portfolioid`)
    REFERENCES `Portfolio` (`portfolioid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PortfolioLInks_PortFoliLinksLabel1`
    FOREIGN KEY (`portFoliLinksLabelid`)
    REFERENCES `PortFoliLinksLabel` (`portFoliLinksLabelid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
