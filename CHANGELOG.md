# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Changes are grouped as follows
- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Deprecated` for soon-to-be removed features.
- `Improved` for transparent changes, e.g. better performance.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## [0.3.1] - 2023-09-25
### Improved
- Improved documentation for various methods and README

## [0.3.0] - 2023-09-21
### Added
- Updated `WellsAPI.retrieve_bhp_calcs()` to improve performance. Default retrieval is first page. User must
  determine whether to retrieve all pages by specifying `None`
- Streamline authentication. Example updated in READM E.

## [0.2.0] - 2023-08-16
### Added
- `APIClient` to generalize calls to API. Include generic get and post methods as well as some static methods to
  retrieve metadata
- Remove 'WhitsonClient' generic `get()` and `post()` methods from class -- rather extend functionality from
  `APIClient`. Added properties for fields, wells, projects, and production data.
- Added `FieldsAPI` class to `list()` and `retrieve()` fields from a Whitson project
- Added `ProductionAPI` class to `retrieve()` production data for a specific well from a Whitson project. Added
  placeholders for future methods.
- Added `ProjectsAPI` class to `list()` and `retrieve()` projects from a Whitson project
- Added `WellsAPI` class to `list()` wells from a Whitson project. Also added `run_bhp_calcs()` and
  `retrieve_bhp_calcs()`
- Added Python Dataclasses to conform retrieved data to a specified format

## [0.1.1] - 2023-08-16
### Fixed
- Documentation on PyPI

## [0.1.0] - 2023-08-15
### Added
- `Token` dataclass to hold information about the access token issued by Whitson. Checks to see if the token is expired.
- `ClientConfig` class to request an access token if the `Token` is not specified or is expired.
- `WhitsonClient` class connect to the main endpoints provided by the API. Only `GET` and `POST` are implemented.
