import os

config = {
    "buildbot_json_path": "buildprops.json",
    "host_utils_url": "http://talos-remote.pvt.build.mozilla.org/tegra/tegra-host-utils.Linux.742597.zip",
    "robocop_package_name": "org.mozilla.roboexample.test",
    "device_ip": "127.0.0.1",
    "default_sut_port1": "20701",
    "default_sut_port2": "20700", # does not prompt for commands
    "tooltool_manifest_path": "testing/config/tooltool-manifests/androidarm/releng.manifest",
    "tooltool_cache": "/builds/tooltool_cache",
    "tooltool_servers": ["http://tooltool.pvt.build.mozilla.org/build/"],
    ".avds_dir": "/home/cltbld/.android",
    "emulator_process_name": "emulator64-arm",
    "emulator_cpu": "cortex-a9",
    "exes": {
        'adb': '/tools/android-sdk18/platform-tools/adb',
        'python': '/tools/buildbot/bin/python',
        'virtualenv': ['/tools/buildbot/bin/python', '/tools/misc-python/virtualenv.py'],
        'tooltool.py': "/tools/tooltool.py",
    },
    "env": {
        "DISPLAY": ":0.0",
        "PATH": "%(PATH)s:/tools/android-sdk18/tools:/tools/android-sdk18/platform-tools",
        "MINIDUMP_SAVEPATH": "%(abs_work_dir)s/../minidumps"
    },
    "default_actions": [
        'clobber',
        'read-buildbot-config',
        'setup-avds',
        'start-emulators',
        'download-and-extract',
        'create-virtualenv',
        'install',
        'run-tests',
        'stop-emulators',
    ],
    "emulators": [
        {
            "name": "test-1",
            "device_id": "emulator-5554",
            "http_port": "8854", # starting http port to use for the mochitest server
            "ssl_port": "4454", # starting ssl port to use for the server
            "emulator_port": 5554,
            "sut_port1": 20701,
            "sut_port2": 20700
        },
        {
            "name": "test-2",
            "device_id": "emulator-5556",
            "http_port": "8856", # starting http port to use for the mochitest server
            "ssl_port": "4456", # starting ssl port to use for the server
            "emulator_port": 5556,
            "sut_port1": 20703,
            "sut_port2": 20702
        },
        {
            "name": "test-3",
            "device_id": "emulator-5558",
            "http_port": "8858", # starting http port to use for the mochitest server
            "ssl_port": "4458", # starting ssl port to use for the server
            "emulator_port": 5558,
            "sut_port1": 20705,
            "sut_port2": 20704
        },
        {
            "name": "test-4",
            "device_id": "emulator-5560",
            "http_port": "8860", # starting http port to use for the mochitest server
            "ssl_port": "4460", # starting ssl port to use for the server
            "emulator_port": 5560,
            "sut_port1": 20707,
            "sut_port2": 20706
        }
    ],
    "test_suite_definitions": {
        "jsreftest-1": {
            "category": "reftest",
            "extra_args": ["../jsreftest/tests/jstests.list",
                "--total-chunks=6", "--this-chunk=1",
                "--extra-profile-file=jsreftest/tests/user.js"]
        },
        "jsreftest-2": {
            "category": "reftest",
            "extra_args": ["../jsreftest/tests/jstests.list",
                "--total-chunks=6", "--this-chunk=2",
                "--extra-profile-file=jsreftest/tests/user.js"]
        },
        "jsreftest-3": {
            "category": "reftest",
            "extra_args": ["../jsreftest/tests/jstests.list",
                "--total-chunks=6", "--this-chunk=3",
                "--extra-profile-file=jsreftest/tests/user.js"]
        },
        "jsreftest-4": {
            "category": "reftest",
            "extra_args": ["../jsreftest/tests/jstests.list",
                "--total-chunks=6", "--this-chunk=4",
                "--extra-profile-file=jsreftest/tests/user.js"]
        },
        "jsreftest-5": {
            "category": "reftest",
            "extra_args": ["../jsreftest/tests/jstests.list",
                "--total-chunks=6", "--this-chunk=5",
                "--extra-profile-file=jsreftest/tests/user.js"]
        },
        "jsreftest-6": {
            "category": "reftest",
            "extra_args": ["../jsreftest/tests/jstests.list",
                "--total-chunks=6", "--this-chunk=6",
                "--extra-profile-file=jsreftest/tests/user.js"]
        },
        "mochitest-1": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=1", "--run-only-tests=android23.json"],
        },
        "mochitest-2": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=2", "--run-only-tests=android23.json"],
        },
        "mochitest-3": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=3", "--run-only-tests=android23.json"],
        },
        "mochitest-4": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=4", "--run-only-tests=android23.json"],
        },
        "mochitest-5": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=5", "--run-only-tests=android23.json"],
        },
        "mochitest-6": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=6", "--run-only-tests=android23.json"],
        },
        "mochitest-7": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=7", "--run-only-tests=android23.json"],
        },
        "mochitest-8": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=8", "--run-only-tests=android23.json"],
        },
        "mochitest-9": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=9", "--run-only-tests=android23.json"],
        },
        "mochitest-10": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=10", "--run-only-tests=android23.json"],
        },
        "mochitest-11": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=11", "--run-only-tests=android23.json"],
        },
        "mochitest-12": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=12", "--run-only-tests=android23.json"],
        },
        "mochitest-13": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=13", "--run-only-tests=android23.json"],
        },
        "mochitest-14": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=14", "--run-only-tests=android23.json"],
        },
        "mochitest-15": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=15", "--run-only-tests=android23.json"],
        },
        "mochitest-16": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=16", "--this-chunk=16", "--run-only-tests=android23.json"],
        },
        "mochitest-gl-1": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=2", "--this-chunk=1", "--test-manifest=gl.json"],
        },
        "mochitest-gl-2": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=2", "--this-chunk=2", "--test-manifest=gl.json"],
        },
        "reftest-1": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=1",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-2": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=2",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-3": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=3",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-4": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=4",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-5": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=5",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-6": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=6",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-7": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=7",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-8": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=8",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-9": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=9",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-10": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=10",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-11": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=11",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-12": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=12",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-13": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=13",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-14": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=14",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-15": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=15",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-16": {
            "category": "reftest",
            "extra_args": ["--total-chunks=16", "--this-chunk=16",
                "tests/layout/reftests/reftest.list"]
        },
        "crashtest-1": {
            "category": "reftest",
            "extra_args": ["--total-chunks=2", "--this-chunk=1",
                "tests/testing/crashtest/crashtests.list"]
        },
        "crashtest-2": {
            "category": "reftest",
            "extra_args": ["--total-chunks=2", "--this-chunk=2",
                "tests/testing/crashtest/crashtests.list"]
        },
        "xpcshell-1": {
            "category": "xpcshell",
            "extra_args": ["--total-chunks=3", "--this-chunk=1",
                # XXX --manifest is superceded by testing/config/mozharness/android_arm_config.py.
                # Remove when Gecko 35 no longer in tbpl.
                "--manifest=tests/xpcshell_android.ini"]
        },
        "xpcshell-2": {
            "category": "xpcshell",
            "extra_args": ["--total-chunks=3", "--this-chunk=2",
                # XXX --manifest is superceded by testing/config/mozharness/android_arm_config.py.
                # Remove when Gecko 35 no longer in tbpl.
                "--manifest=tests/xpcshell_android.ini"]
        },
        "xpcshell-3": {
            "category": "xpcshell",
            "extra_args": ["--total-chunks=3", "--this-chunk=3",
                # XXX --manifest is superceded by testing/config/mozharness/android_arm_config.py.
                # Remove when Gecko 35 no longer in tbpl.
                "--manifest=tests/xpcshell_android.ini"]
        },
        "robocop-1": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=4", "--this-chunk=1", "--robocop-path=../..",
                "--robocop-ids=fennec_ids.txt", "--robocop=robocop.ini"],
        },
        "robocop-2": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=4", "--this-chunk=2", "--robocop-path=../..",
                "--robocop-ids=fennec_ids.txt", "--robocop=robocop.ini"],
        },
        "robocop-3": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=4", "--this-chunk=3", "--robocop-path=../..",
                "--robocop-ids=fennec_ids.txt", "--robocop=robocop.ini"],
        },
        "robocop-4": {
            "category": "mochitest",
            "extra_args": ["--total-chunks=4", "--this-chunk=4", "--robocop-path=../..",
                "--robocop-ids=fennec_ids.txt", "--robocop=robocop.ini"],
        },
    }, # end of "test_definitions"
    # test harness options are located in the gecko tree
    "in_tree_config": "config/mozharness/android_arm_config.py",
    "download_minidump_stackwalk": True,
    "default_blob_upload_servers": [
         "https://blobupload.elasticbeanstalk.com",
    ],
    "blob_uploader_auth_file" : os.path.join(os.getcwd(), "oauth.txt"),
}
