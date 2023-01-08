from staketaxcsv.xprt.config_xprt import localconfig
from staketaxcsv.common.progress import Progress

SECONDS_PER_PAGE = 4


class ProgressXprt(Progress):

    def __init__(self):
        super().__init__(localconfig)

    def set_estimate(self, count_pages):
        self.add_stage("default", count_pages, SECONDS_PER_PAGE)
