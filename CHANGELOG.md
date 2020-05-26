# Release notes for project onedata


CHANGELOG
---------

### 19.02.3

* Minor bugfixes

### 19.02.2

* Bugfixes and stability improvements


### 19.02.1

* Update submodules
* Updated opworker ref
* Updated oneclient ref
* Updated oneclient ref
* Update submodules
* Update submodules
* Update submodules
* Update refs to origin/release/19.02.1
* Updated oneclient ref
* update op_worker ref
* Update submodules
* Update refs to origin/release/19.02.1
* Update refs to origin/release/19.02.1
* Update refs to origin/release/19.02.1
* Updated oneclient ref
* Update refs to origin/develop
* Update refs to origin/develop
* Update submodules
* Update submodules
* Update submodules
* Update refs to origin/release/19.02.1
* Update refs to origin/release/19.02.1
* Update submodules
* Update submodules
* Update refs to origin/release/19.02.1
* Update refs to origin/release/19.02.1
* Updated fs-onedatafs ref
* Updated oneclient ref
* Update submodules
* Update submodules
* Update submodules
* Update submodules
* Releasing new version 19.02.1
* Update submodules refs
* Update submodules
* Update refs to origin/release/19.02.1
* updated bamboos refs s3
* updated bamboos refs s3
* updated bamboos refs s3
* VFS-5884 Fixed onedatafs-jupyter name
* VFS-5884 Added print_package_versions makefile rule
* Update refs to release/19.02.1


### 19.02.1

* VFS-5884 Added print_package_versions makefile rule

##### op-worker

* Bump version to 19.02.1
* VFS-5826 Ensure db start at cluster init
* VFS-5900 GUI update * Added showing special subjects in ACL editor
* VFS-5826 Add missing event during dir creation
* VFS-5891 Clean authorization nonce after its TTL
* VFS-5826 Add events during file creation
* VFS-5826 Change max_read_dir_plus_procs value
* VFS-5826 Emmit attr_changed events on chmod and acl change
* VFS-5826 Change events processing - allow subscriptions per dir

##### onepanel

* VFS-5994 Make 'production' Let's Encrypt mode the default
* VFS-5940 Rename oz-worker's GUI package verification envs to more intuitive

##### oneclient

* VFS-5826 Increased events test connections
* VFS-5826 Added opendir and releasedir to OnedataFS
* VFS-5826 Increased default metadata cache size
* VFS-5826 Added support for opendir and releasedir
* VFS-5826 Added persistent directory cache
* VFS-5826 Added directory subscription cancelling
* VFS-5844 Refactored metadatacache to limit file subscriptions
* VFS-5965 Added option to emulate large available space


### 19.02.0-rc2

* VFS-5742 Disabled http_proxy for normal operation
* VFS-5742 Disabled yum mirrors for package tests
* VFS-5742 Disabled yum proxy for package tests
* VFS-5742 Enabled proxy cache for package tests
* VFS-5742 Enabled proxy cache for docker builds


### 19.02.0-rc1

* VFS-5660 Disabled RANDFILE to enable certificate creation in Docker
* VFS-5660 Added libssl1.0.0 dependency to Docker
* VFS-5657 Fixed Dockerfile for tagged ubuntu packages
* VFS-5657 Enabled bionic packaging tests
* VFS-5535 Added onedatafs-jupyter docker make rule
* VFS-5563 Added onedatafs-jupyter submodule
* VFS-5535 Fixed CentOS onedatafs-jupyter package builds


### 18.02.3

* Releasing new version 18.02.3


### 18.02.2

* Update submodules
* VFS-5436 Fixed oneclient packaging tests
* VFS-5436 Fixed Oneprovider packaging tests
* VFS-5434 Fixed CentOS package tests
* VFS-5053 Updated worker and builder versions


### 18.02.1

* VFS-5154 Fixed Oneprovider packaging tests


### 18.02.0-rc13

* VFS-5001 Changed auth provider selector
* Fix locale settings in Oneprovider docker
* fix fetching token from oz


### 18.02.0-rc12

* Releasing new version 18.02.0-rc12


### 18.02.0-rc11

* Releasing new version 18.02.0-rc11


### 18.02.0-rc10

* Releasing new version 18.02.0-rc10


### 18.02.0-rc9

* VFS-4532 Create new config file instead of using regexps
* VFS-4482 Changed transfer tabs names
* VFS-4367 Make docker entrpoint consistent with onezone.py
* VFS-4367 Expect 409 when configuring existing cluster
* VFS-4367 Do not fail cluster restart when admin credentials are missing
* VFS-4521 Adjusted sysbench performance test parameters
* VFS-4521 change deprecated sysbench options
* VFS-4521 upgrade sysbench performance test


### 18.02.0-rc8

* Releasing new version 18.02.0-rc8


### 18.02.0-rc7

* VFS-4474 Display error details on configuration error
* VFS-4278 Better detection of bad credentials error in entrypoint
* VFS-4470 Changed asserted transferred files


### 18.02.0-rc6

* Releasing new version 18.02.0-rc6


### 18.02.0-rc5

* VFS-4480 Remove home provider test as it this feature was removed


### 18.02.0-rc4

* VFS-4278 Use nagios to wait for cluster to resume work
* VFS-4278 Fetch batch config only when needed
* VFS-4278 Allow failed configuration for existing provider
* VFS-4278 Remove setting onezone domain from entrypoint
* VFS-4278 Start services on restart


### 18.02.0-rc3

* Releasing new version 18.02.0-rc3


### 18.02.0-rc2

* VFS-4327 Added wt decorator
* VFS-4343 Added tabs in transfer tests
* VFS-4343 Updated transfers tests
* VFS-4365 Backporting scroll improvement and OSX support for GUI tests
* VFS-4327 Added check with stat if file exists


### 18.02.0-rc1

* VFS-2021 Added dockers.config 
* VFS-4376 Tests updated after removing sticky_bit
* VFS-4362 Removing symlinks from logs after env_up teardown
* VFS-4369 fix acceptance tests after removing sticky bit


### 18.02.0-beta6

* Releasing new version 18.02.0-beta6


### 18.02.0-beta5

* VFS-4333 Decresed test logging delay in file creation tests
* VFS-4333 Disabled gdb by default
* VFS-3622 Merged docker-dev with docker. Added possibility to run services from sources.


### 18.02.0-beta4

* Releasing new version 18.02.0-beta4


### 18.02.0-beta3

* VFS-4213 Change the way persistent volume is created to allow for mounting single files inside it


### 18.02.0-beta2

* VFS-4126 Remove obsolete port exposes from Dockerfiles
* VFS-4099 Changed selenium get url to javascript


### 18.02.0-beta1

* Releasing new version 18.02.0-beta1


### 17.06.2

* Releasing new version 17.06.2


### 17.06.1

* Releasing new version 17.06.1


### 17.06.0-rc9

* VFS-3977 Remove oneclient-base from docker-dev image
* VFS-3877 Removed self-contained-html from gui acceptance tests
* VFS-3877 Added tmp_files to gitignore
* VFS-3877 Implemented GUI acceptance tests for transfers
* VFS-3862 Add more verbose log when oneprovider configuration script fails


### 17.06.0-rc8

* VFS-3815 Modified packaging tests for CentOS 7


### 17.06.0-rc7

* Releasing new version 17.06.0-rc7


### 17.06.0-rc6

* Releasing new version 17.06.0-rc6


### 17.06.0-rc5

* Releasing new version 17.06.0-rc5


### 17.06.0-rc4

* VFS-3682 Added self-contained Oneclient packaging


### 17.06.0-rc3

* VFS-3656 Removed support for Ubuntu Wily
* VFS-3517 Added tests checking timestamps after renaming item in GUI to xfail due to VFS-3520
* VFS-3517 Changed amount of time to wait between creating and renaming space
* VFS-3515 add additional logs to performance tests
* VFS-3281 Added extended attributes acceptance tests


### 17.06.0-rc2

* VFS-3434 Multiuser tests implemented
* VFS-3465 flush stdout after prints in performance tests
* VFS-3465 split tests/gui/scenarios into modules and add -s option to performance tests
* VFS-3465 add additional logging to performance tests
* VFS-3434 POSIX privileges mixed tests implemented
* VFS-3434 Added --self-contained-html to test_acceptance_mixed
* VFS-3434 Posix privileges gui steps added


### 17.06.0-rc1

* VFS-3407 Mixed tests (GUI and oneclient)


### 17.06.0-beta6

* VFS-3358 fix steps managing btns in toolbar in data tab in op after changes in gui
* VFS-3284 GUI tests: using new go to your files button
* VFS-3322 add 10000 files creation performance test


### 17.06.0-beta4

* VFS-3347 Add docker-dev build


### 17.06.0-beta3

* VFS-3353 Enable user name/email set in ``update_refs.sh``
* VFS-3340 GUI acceptance tests update: changed timeouts, get support modal tests
* Releasing new version 17.06.0-beta3


### 17.06.0-beta2

* VFS-3348 Update couchbase version to 4.5.1


### 3.0.0-rc16

* VFS-3184 Add copy/remove tests.
* VFS-3017 Check if mtime and ctime are equal after rename (in previous implemetation of rename they were greater).


### 3.0.0-rc15

* Update refs to origin/release/3.0.0-rc15.
* VFS-3197 Enable release docker to log to stdout
* Update refs to origin/feature/VFS-3213-change-storage-verification-mechanism.
* VFS-3051 add clipboard fixture and replace pyperclip uses with it
* VFS-3051 enhance logging capabilities
* VFS-3051 add support for recording tests with multiple browsers
* implement changes to allow splitting acceptance tests on bamboo
* VFS-3051 add support for logs from multiple browsers


### 3.0.0-rc14

* VFS-3101 change Then steps in metadata scenarios
* VFS-3101 refactor metadata steps
* VFS-3101 add ButtonWebObject class
* VFS-3050 add test for 2 providers
* VFS-3050 add steps creating access token and copying providers ip for cdmi use
* VFS-3050 add provisional api for handling cdmi service from tests
* VFS-3050 refactor web_elements.py
* VFS-3050 add test user upload file on 1 provider and download on other
* VFS-3050 add utils for handling of file distribution modal and canvas


### 3.0.0-rc13

* Releasing new version 3.0.0-rc13


### 3.0.0-rc12

* Enable graceful stop on SIGTERM
* Add oneprovider users and groups in Dockerfile
* Update refs to origin/release/3.0.0-rc12.
* VFS-2910 Adjust tests to LUMA refactoring
* VFS-2725 improve logging in acceptance tests, all tests in directory_CRUD addapted to new logging, all of them pass successfully
* VFS-2551 add test to set space as home in oz
* VFS-2551 add tests for data space management
* VFS-2551 add tests for user alies and access tokens


### 3.0.0-rc11

* VFS-2733 Fix provider key/cert filename
* VFS-2739 make msg for assertion more descriptive
* VFS-2739 rewrite msg on assertions
* VFS-2739 use tmpdir pytest fixture instead of os to crete tmpdir and files
* VFS-2739 add msg to assertions
* VFS-2739 change click on file -> select file in shares test
* VFS-2739 add test to select multiple files witch ctrl
* VFS-2739 add cleaning to upload many files test
* VFS-2739 add paging test
* VFS-2733 Add excluded path to docker entrypoint
* VFS-2549 fix checking content of downloaded file step
* VFS-2549 change url->URL, id->ID in gherkin steps
* VFS-2549 add quotes to files/dirs in shares tests steps in gherkin
* VFS-2549 add quotes to file/dir names in data and metadata features
* VFS-2549 add quotation marks to names of groups/spaces/shares/...
* VFS-2549 fix closing notifies
* VFS-2549 fix scenario names in group and share tests
* VFS-2564 add test checking that user can't view left group
* VFS-2616 add test checking if user can view group having it's id
* VFS-2549 fix waiting for notifies to disappear and switching spaces
* VFS-2549 remove import of non existing module file_system
* VFS-2634 refactor share tests
* VFS-2634 fix step fun definitions, add new share tests
* VFS-2634 refactor modals and file list steps, add sidebar list steps
* VFS-2634 fix modal and file list steps


### 3.0.0-rc10

* Releasing new version 3.0.0-rc10
* VFS-2714 print gherkin-reports in acceptance tests after pytest-bdd update


### 3.0.0-rc9

* VFS-2617 Changed metadata submenu to metadata panel


### 3.0.0-rc8

* Releasing new version 3.0.0-rc8
* VFS-2549 Add tests for public readonly share: add file, remove file, jump no breadcrumbs
* VFS-2549 Fix share tests to work with new gui
* VFS-2549 Add 2 new tests for shares: recursive delete, jumping in breadcrumbs
* VFS-2549 Fix share multi test
* VFS-2634 Fix tests to work with new gui, add new share tests
* VFS-2634 Fix share steps, add 2 new scenarios


### 3.0.0-rc7

* VFS-2549 Add share tests for multiple browsers: download, rename, remove


### 3.0.0-rc6

* VFS-2180 Improve links conflict resolution
* VFS-2180 Improve dbsync implementation
* VFS-2180 Use gen_server2 instead of erlang's gen_server module
* VFS-2390 Fix handlers specification in REST API
* VFS-2390 Update rebar to version 3
* Update memory management
* VFS-2180 Allow for concurrent file creation
* VFS-2202 modify README.md
* VFS-2202 fix step name of step creating webdriver instances
* VFS-2202 remake givens to work with multiple browsers
* VFS-2202 add join group test
* VFS-2202 remake use of pytest_selenium_multi fixtures
* VFS-2202 remake firefox profile as factory


### 3.0.0-rc5

* Update interfaces
* Increase system performance
* VFS-2534 Improve events processing
* Update one panel for extended configuration options
* VFS-2527 Use sbin/init as docker entrypoint
* VFS-2449 fix step names and activating input box
* VFS-2476 Add events profiling tests
* VFS-2449 fix entering text to input box
* VFS-2449 add msg to wait(...).until(..., msg=...)
* VFS-2450 fail test instead of skipping if setting up environment fails
* VFS-2454 add download test for firefox
* VFS-2454 add download test for chrome


### 3.0.0-rc4

* Add ONEPANEL_DEBUG_MODE env variable to release docker entrypoint


### 3.0.0-RC3

* VFS-2156 Update release docker
* VFS-2156 Update packages tests
* VFS-2395 Fix given step for checking provider's name in file distribution
* VFS-2395 Fix given for data spaces and renamed some steps for spaces tests
* VFS-2395 Added scrolling to element when clicking settings icon.
* VFS-2395 Refactorize functions for creating space in onezone


### 3.0.0-RC2

* Turn off HSTS by default, allow configuration via app.config
* Update file consistency management
* Enable metadata caching
* Extend support for user-defined metadata
* Update Web_GUI and REST API
* added NO_CACHE option to makefile
* Enable Symmetric Multiprocessing
* Use environment variables for packages build


### 3.0.0-RC1

* Tests refactoring
* Several op_worker stability improvements
* Extend op_worker system monitoring
* Update session management
* VFS-2316 Update etls.
* Improve client stability
* VFS-1963 Improve automatic storage discovery
* VFS-2270 Print out the hostname of client's provider.


### 3.0.0-beta8

* Additional GUI model relations
* Update ACL and protocol
* Change error on sync fail
* Add file redirection to rename


### 3.0.0-beta7

* Improve GUI
* Improve dbsync reliability and performance
* Adjust to new client API


### 3.0.0-beta6

* Add prefetching
* Add support for S3
* Add quota implementation
* Extend REST api



### 3.0.0-beta5

* Metadata synchronization between providers improved.
* Support for nested groups.


### 3.0.0-beta4

* Rename redeisgned.


### 3.0.0-beta3

* GUI update
* Provider proxy channel added
* Faster proxy for oneclient
* LUMA integrated
* Code covering


### 3.0.0-beta1

* New oneclient with faster proxy and SMB
* New op_worker with subscriptions and new GUI
* VFS-1804 Add redirection point to oneprovider config.
* VFS-1804 Adjust packaging tests config files.
* VFS-1757 Fix onedata deinstallation.
* Update environment descriptions, remove bamboos compilation.
* VFS-1788 Use onezone artifact during onedata packages tests.


### 3.0.0-alpha3

* VFS-1677 -  using get_cookie function instead of hardcoding cookie in get_token.escript
* VFS-1684 - bring env up by calling run_env_up_script in cucumber tests
* VFS-1677-cucumber test generator sketch
* VFS-1684 - add build_onepanel target to Makefile
* VFS-1657 Add system update to release dockers.
* VFS-1544 makefile rebranding
* VFS-1544 onezone rebranding


### 3.0.0-aplha

* VFS-1621 Add release dockerfile.
* Add vivid repo to pkg.py script.
* Do not exit when deployment of one package fails.
* VFS-1583- save logs from acceptance_tests
* VFS-1583-add timestamps to logdir names
* VFS-1583-save logs from cucumber tests in tests/cucumber/logs
* VFS-1628 Remove unnecessary options and sign rpms without asking for password in pkg.py script.
* VFS-1603 Bump fedora-systemd version to comply with parent image - fedora 23.
* VFS-1603 Fix RPM package installation test.
* VFS-1628 Improve pkg.py script.
* Increasing timeouts in appmock tcp tests
* VFS-1603 Adjust pkg.py script to wily deb package.
* VFS-1603 Fix oneprovider deinstallation.
* VFS-1603 Adjust tests to the new packages.
* VFS-1505 Enabling and improving timestamps tests


### 3.0.0-prealpha1

* Dockerized environment provided.
* Acceptance tests in GHERKIN.
* Unit, integration and acceptance tests provided.
* Appmock for tests provided.
* Onepanel for simple installation provided.
* Global Registry provided.
* Oneclient provided.
* Oneprovider composed of op-worker and cluster-manager provided.




________

Generated by sr-release. 
