from djchoices import DjangoChoices

from .dr_20200117 import api_09_20200117, api_51_20200117
from .dr_20200709 import (
    api_03_20200709, api_16_20200709, api_20_20200709, api_48_20200709, api_51_20200709,
    api_53_20200709, api_54_20200709, api_55_20200709, api_56_20200709, api_57_20200709
)


class DesignRuleChoices(DjangoChoices):
    # 17-01-2020
    api_09_20200117 = api_09_20200117
    api_51_20200117 = api_51_20200117
    # 09-07-2020
    api_03_20200709 = api_03_20200709
    api_16_20200709 = api_16_20200709
    api_20_20200709 = api_20_20200709
    api_48_20200709 = api_48_20200709
    api_51_20200709 = api_51_20200709
    api_53_20200709 = api_53_20200709
    api_54_20200709 = api_54_20200709
    api_55_20200709 = api_55_20200709
    api_56_20200709 = api_56_20200709
    api_57_20200709 = api_57_20200709
