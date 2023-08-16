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

## [0.1.1] - 2023-08-16
### Fixed
- Documentation on PyPI

## [0.1.0] - 2023-08-15
### Added
- `Token` dataclass to hold information about the access token issued by Whitson. Checks to see if the token is expired.
- `ClientConfig` class to request an access token if the `Token` is not specified or is expired.
- `WhitsonClient` class connect to the main endpoints provided by the API. Only `GET` and `POST` are implemented.
