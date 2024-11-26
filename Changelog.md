# Changelog

## [v11.0.0] - 2024-11-12

---



## [v11.1.0] - 2024-11-15

### Added

- Added ci via github actions
- Added cd via github actions and uploading to dockerhub under deadbacteria8 user

### Fixed


- Fixed Docker-compose by using uploaded images. Updated gunicorn command in boot.sh

- Fixed typo in cd_build.yml workflow
- Fixed filepath to dockerfile
- Added checkout so we can build dockerfile


## [v11.1.0] - 2024-11-17

### Added

- Added Followers to the app, you can now follow other users and receive updates in your feed.

## [v11.1.1] - 2024-11-17

### Fixed

- Fixed minor pylint errors in main/routes and unit/models/test_follow

## [v11.1.2] - 2024-11-17

### Fixed

- Docker issue with building inside azure vm due to image being arm64 and not amd


## [v11.1.3] - 2024-11-17

### Fixed

- Docker validation


## [v11.1.4] - 2024-11-17

### Fixed

- Docker platform fix for amd64. Now using newer docker image


## [v11.1.5] - 2024-11-17

### Fixed

- Using mysql 5.7 in docker instead of 8 due to performance issues


## [v11.1.6] - 2024-11-27

### Added

- Added automation deploy with ansible
- Updated boot.sh and use of docker image in ansible because we are no health_checks possible like docker when in seperate vms.
