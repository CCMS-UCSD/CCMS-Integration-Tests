-include Makefile.credentials

test-push:
	act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}

test-schedule:
	act schedule -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -s CCMS_TESTUSER_USERNAME=${CCMS_TESTUSER_USERNAME} -s CCMS_TESTUSER_PASSWORD=${CCMS_TESTUSER_PASSWORD}