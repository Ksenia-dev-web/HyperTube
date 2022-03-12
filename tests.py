# -*- coding: utf-8 -*-
from hstest import dynamic_test

from test.base import HyperTubeTest


class HyperTubeTestRunner(HyperTubeTest):

    funcs = [
        # 1 task
        HyperTubeTest.check_create_videos,
        # 2 task
        HyperTubeTest.check_main_header,
        HyperTubeTest.check_main_page_login_link,
        HyperTubeTest.check_main_page_upload_link,
        HyperTubeTest.check_main_page_video_links,
        HyperTubeTest.check_main_page_video_count,
        # 3 task
        HyperTubeTest.check_main_page_search,
        HyperTubeTest.check_main_page_tag_filtering,
        # 4 task
        HyperTubeTest.check_signup,
        HyperTubeTest.check_login,
        # 5 task
        HyperTubeTest.check_uploading_video,
        HyperTubeTest.check_forbid_anonymous_upload,
        HyperTubeTest.check_upload_page_main_link,
    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    HyperTubeTestRunner().run_tests()
